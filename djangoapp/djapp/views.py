from django.shortcuts import render
import re
import requests


def index(request):
    return render(request, 'index.html')


def statistics(request):
    return render(request, 'statistics.html')


def usability(request):
    return render(request, 'usability.html')


def cities(request):
    return render(request, 'cities.html')


def skills(request):
    return render(request, 'skills.html')


def last_vacs(request):
    class HHAPI:

        def __init__(self, search_text: str):
            self.text = search_text

        def __get_full_vacancies__(self, date: str, count_vac: int) -> list:
            url = 'https://api.hh.ru/vacancies'
            return requests.get(url, dict(text=self.text,
                                          specialization=1,
                                          # date_from=f"{date}T00:00:00",
                                          # date_to=f"{date}T23:00:00",
                                          per_page=count_vac,
                                          page=1)).json()["items"]

        def get_data_vacancies(self, date: str, count_vac: int):
            data = self.__get_full_vacancies__(date, count_vac)
            result_list = []
            for vac in data:
                url_vac = f'https://api.hh.ru/vacancies/{vac["id"]}'
                resp = requests.get(url_vac).json()
                if resp['salary']:
                    description = ' '.join(re.sub(re.compile('<.*?>'), '', resp['description'])
                                           .strip()
                                           .split())
                    description = description[:100] + '...' if len(description) >= 100 else description
                    result_list.append({'name': resp['name'],
                                        'description': description,
                                        'key_skills': ', '.join(list(map(lambda x: x['name'], resp['key_skills']))),
                                        'employer': resp['employer']['name'],
                                        'salary': f"{resp['salary']['from']} - {resp['salary']['to']} {resp['salary']['currency']}",
                                        'area': resp['area']['name'],
                                        'published_at': resp['published_at'][:10],
                                        'alternate_url': resp['alternate_url']})

            return result_list

    hh = HHAPI('django')
    vacs = hh.get_data_vacancies('2025-01-19', 10)
    return render(request, 'last_vacs.html', {'vacs': vacs,})