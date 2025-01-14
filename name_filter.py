import pandas as pd


def filter_dataframe(df, column_name, allowed_values):
    mask = df[column_name].apply(lambda x: any(value in x for value in allowed_values))
    filtered_df = df[mask]
    return filtered_df


df = pd.read_csv('vacancies_2024.csv')
profession_names = ['backend-программист', 'backend', 'бэкэнд', 'бэкенд', 'бекенд', 'бекэнд', 'back end', 'бэк энд', 'бэк енд', 'django', 'flask', 'laravel', 'yii', 'symfony']
filtered_df = filter_dataframe(df, 'name', profession_names)
filtered_df['published_at'] = filtered_df['published_at'].apply(lambda x: x[0:7])

filtered_df.to_csv('backend_vacancies.csv', index=False)
