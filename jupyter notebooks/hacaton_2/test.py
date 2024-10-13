import pandas as pd
import os

def check_csv_columns(directory, columns_set):
    # Получаем список всех файлов в директории
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            # Загружаем CSV в DataFrame
            df = pd.read_csv(file_path, low_memory=False)

            # Проверяем, существует ли хотя бы одно название из columns_set
            if not any(col in df.columns for col in columns_set):
                print(f"В файле '{filename}' отсутствуют указанные столбцы.")
                print("Названия всех столбцов:", df.columns.tolist())

                return
            else:
                print(f"В файле '{filename}' найдены указанные столбцы.")
                

# Пример вызова функции
columns_to_check = {'Организации','Affiliations'}
check_csv_columns('data/2024', columns_to_check)
#df = pd.read_csv('data/2021/china_2021_dec_(24, 31).csv')
#print(df['Affiliations'])