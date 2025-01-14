import pandas as pd
import matplotlib.pyplot as plt


def get_right_form(count):
    if count % 10 == 1:
        return 'упоминание'
    if count % 10 in [2, 3, 4] and count % 100 not in [10, 11, 12, 13, 14]:
        return 'упоминания'
    return 'упоминаний'

df = pd.read_csv('backend_vacancies_for_key_skills_stat.csv')
skills_dict = {
    '2015': [],
    '2016': [],
    '2017': [],
    '2018': [],
    '2019': [],
    '2020': [],
    '2021': [],
    '2022': [],
    '2023': [],
    '2024': [],
}

for index, row in df.iterrows():
    skills_dict[row['published_at'][0:4]].extend(row['key_skills'].split('\n'))

top_skills_by_years_dict = dict()
for x in skills_dict:
    count_list = list()
    unique_skills = set(skills_dict[x])
    for skill in unique_skills:
        count_list.append(f'{skills_dict[x].count(skill)} - {skill}')
    count_list = list(sorted(count_list, key=lambda x: int(x[:x.find(' ')]), reverse=True))
    top_skills_by_years_dict[x] = count_list[:20]

for x in top_skills_by_years_dict:
    skills = list()
    counts = list()
    for elem in top_skills_by_years_dict[x]:
        skills.append(elem[elem.rfind(' ') + 1:])
        counts.append(int(elem[:elem.find(' ')]))
    plt.figure(figsize=(8, 5))
    plt.xticks(fontsize=5)
    plt.bar(skills, counts, width=0.5)
    plt.title(f'Топ-20 востребованных навыков за {x}')
    plt.xlabel('Навык')
    plt.ylabel('Количество упоминаний в вакансиях')
    plt.grid()
    plt.tight_layout()
    plt.show()

print("""<tr>
    <th>№</th>
    <th>2015</th>
    <th>2016</th>
    <th>2017</th>
    <th>2018</th>
    <th>2019</th>
    <th>2020</th>
    <th>2021</th>
    <th>2022</th>
    <th>2023</th>
    <th>2024</th>
</tr>""")
count = 1
for x in range(20):
    print('<tr>', end='\n   ')
    print(f'<td>{count}</td>', end='\n    ')
    count += 1
    for y in top_skills_by_years_dict:
        elem = top_skills_by_years_dict[y][x]
        print(f"<td>{elem[elem.rfind(' ') + 1:]} - {elem[:elem.find(' ')]} {get_right_form(int(elem[:elem.find(' ')]))}</td>", end='\n   ')
    print('</tr>')