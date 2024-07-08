import pandas as pd
import numpy as np

# Зададим имена столбцов и данные
subjects = ['Имя', 'Математика', 'Физика', 'Химия', 'Биология', 'История']
names = ['Алексей', 'Ирина', 'Владимир', 'Анна', 'Ольга', 'Дмитрий', 'Мария', 'Сергей', 'Елена', 'Николай']

# Генерируем случайные оценки по шкале 2-5 для каждого ученика
data = {
    'Имя': names,
    'Математика': np.random.randint(2, 6, size=10),
    'Физика': np.random.randint(2, 6, size=10),
    'Химия': np.random.randint(2, 6, size=10),
    'Биология': np.random.randint(2, 6, size=10),
    'История': np.random.randint(2, 6, size=10),
}

# Создаем DataFrame
df = pd.DataFrame(data)

# Сохраняем DataFrame в CSV файл
csv_file = 'ученики_оценки.csv'
df.to_csv(csv_file, index=False, encoding='utf-8')

print(f'CSV файл "{csv_file}" создан.')

# Загрузка данных из CSV файла
df = pd.read_csv(csv_file)

# Вывод первых нескольких строк DataFrame
print("Первые строки DataFrame:")
print(df.head())

# Вычисляем средние оценки по каждому предмету
average_scores = df.mean(numeric_only=True)
print("\nСредние оценки по предметам:")
print(average_scores)

# Вычисляем медианные оценки по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианные оценки по предметам:")
print(median_scores)

# Вычисляем Первый квартиль  Q1 и Третий квартиль Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)

print("\nQ1 для оценок по математике:", Q1_math)
print("Q3 для оценок по математике:", Q3_math)

# Вычисляем Межквартальный размах IQR
IQR_math = Q3_math - Q1_math
print("IQR для оценок по математике:", IQR_math)

# Вычисляем стандартное отклонение STD для каждого предмета
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по предметам:")
print(std_deviation)
