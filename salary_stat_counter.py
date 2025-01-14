import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('backend_vacancies_for_salary_stat.csv')

average_salary_by_year = dict(sorted(df.groupby('published_at')['salary'].mean().round().items(), key=lambda item: item[0], reverse=True))
years = list(average_salary_by_year.keys())
average_salaries = list(average_salary_by_year.values())
plt.figure(figsize=(8, 5))
plt.plot(years, average_salaries, marker='o')

plt.title('Динамика зарплат по годам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата')
plt.grid()
plt.tight_layout()
plt.show()


average_salary_by_city = dict(sorted(df.groupby('area_name')['salary'].mean().round().items(), key=lambda item: item[1], reverse=True))
counter = 0
count = 1
while counter < len(average_salary_by_city):
    if len(average_salary_by_city) - counter >= 10:
        cities = list(average_salary_by_city.keys())[counter:counter + 10]
        average_salaries = list(average_salary_by_city.values())[counter:counter + 10]
        plt.figure(figsize=(8, 5))
        plt.xticks(fontsize=5)
        plt.bar(cities, average_salaries)
        plt.title(f'Динамика зарплат по городам {count}')
        plt.xlabel('Город')
        plt.ylabel('Средняя зарплата')
        plt.grid()
        plt.tight_layout()
        plt.show()
        counter += 10
        count += 1
    else:
        cities = list(average_salary_by_city.keys())[counter:len(average_salary_by_city)]
        average_salaries = list(average_salary_by_city.values())[counter:len(average_salary_by_city)]
        plt.figure(figsize=(8, 5))
        plt.bar(cities, average_salaries)
        plt.title(f'Динамика зарплат по городам {count}')
        plt.xlabel('Город')
        plt.ylabel('Средняя зарплата')
        plt.grid()
        plt.tight_layout()
        plt.show()
        break


print("""<tr>
    <th>Год</th>
    <th>Средняя зарплата</th>
</tr>""")
for x in average_salary_by_year:
    print(f"""<tr>
    <td>{x}</td>
    <td>{average_salary_by_year[x]}</td>
</tr>""")

print("""<tr>
    <th>№</th>
    <th>Город</th>
    <th>Средняя зарплата</th>
</tr>""")

for index, x in enumerate(average_salary_by_city):
    print(f"""<tr>
    <td>{index + 1}</td>
    <td>{x}</td>
    <td>{average_salary_by_city[x]}</td>
</tr>""")
