import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('backend_vacancies.csv')
df['published_at_slice'] = df['published_at'].str[:4]
published_at_counts = dict(sorted(df['published_at_slice'].value_counts().items(), key=lambda item: item[0]))
years = list(published_at_counts.keys())
average_salaries = list(published_at_counts.values())
plt.figure(figsize=(8, 5))
plt.plot(years, average_salaries, marker='o')

plt.title('Динамика количества вакансий по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.grid()
plt.tight_layout()
plt.show()

df.drop(columns=['published_at_slice'], inplace=True)
area_name_counts = dict(sorted(df['area_name'].value_counts().items(), key=lambda item: item[1], reverse=True))
c = 0
for x in area_name_counts:
    c += area_name_counts[x]

for x in area_name_counts:
    area_name_counts[x] = round(area_name_counts[x] / c, 4)


cities = list(area_name_counts.keys())[0:14]
average_salaries = list(area_name_counts.values())[0:14]
plt.figure(figsize=(8, 5))
plt.xticks(fontsize=5)
plt.bar(cities, average_salaries)
plt.title(f'Доля вакансий по городам')
plt.xlabel('Город')
plt.ylabel('Доля вакансий')
plt.grid()
plt.tight_layout()
plt.show()

published_at_counts = dict(sorted(published_at_counts.items(), key=lambda item: item[0], reverse=True))
print("""<tr>
    <th>Год</th>
    <th>Количество вакансий</th>
</tr>""")
for x in published_at_counts:
    print(f"""<tr>
    <td>{x}</td>
    <td>{published_at_counts[x]}</td>
</tr>""")

print("""<tr>
    <th>№</th>
    <th>Город</th>
    <th>Доля вакансий</th>
</tr>""")

for index, x in enumerate(area_name_counts):
    print(f"""<tr>
    <td>{index + 1}</td>
    <td>{x}</td>
    <td>{area_name_counts[x]}</td>
</tr>""")
