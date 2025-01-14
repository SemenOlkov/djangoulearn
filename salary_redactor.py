import pandas as pd


def calculate_average_salary(row):
    salary_from = row['salary_from']
    salary_to = row['salary_to']

    if pd.notna(salary_from) and pd.notna(salary_to):
        return (salary_from + salary_to) / 2
    elif pd.isna(salary_from) and pd.notna(salary_to):
        return salary_to / 2
    elif pd.notna(salary_from) and pd.isna(salary_to):
        return salary_from


vacancy_df = pd.read_csv('backend_vacancies.csv')
currency_df = pd.read_csv('corrected_currency.csv')
currency_df.set_index('date')

df_filtered = vacancy_df.dropna(subset=['salary_from', 'salary_to'], how='all')

df_filtered['salary'] = df_filtered.apply(calculate_average_salary, axis=1)
# df_filtered['salary'] = int(df_filtered['salary'] * currency_df.loc[df_filtered['published_at'], df_filtered['salary_currency']])
index_dict = dict()
for index in currency_df.index:
    index_dict[currency_df.loc[index, 'date']] = index


rows = list()
count = 1
for index in df_filtered.index:
    row = df_filtered.loc[index]
    date_row = currency_df.loc[index_dict[row['published_at']]]
    if row['salary_currency'] in currency_df.columns.to_list():
        row['salary'] *= date_row[row['salary_currency']] if row['salary_currency'] != 'RUR' else 1
    dict_row = row.to_dict()
    dict_row['id'] = count
    count += 1
    rows.append(dict_row)

df = pd.DataFrame(rows)[['name', 'key_skills', 'salary_from', 'salary_to', 'salary_currency', 'area_name', 'published_at', 'salary']]
df = df.drop(columns=['salary_from', 'salary_to', 'salary_currency', 'name', 'key_skills'])
df['salary'] = round(df['salary'])
df['published_at'] = df['published_at'].apply(lambda x: x[0:4])

df.to_csv('backend_vacancies_for_salary_stat.csv', index=False)
