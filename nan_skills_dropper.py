import pandas as pd


df = pd.read_csv('backend_vacancies_for_key_skills_stat.csv.csv')
df = df.dropna(subset=['key_skills'], how='all')

df.to_csv('backend_vacancies_for_key_skills_stat.csv')
