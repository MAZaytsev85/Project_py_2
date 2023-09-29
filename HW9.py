import pandas as pd

data = pd.read_csv("california_housing_train.csv")

print(f"Cредняя стоимость дома, где кол-во людей от 0 до 500 --> {data[(data['population'] < 500) & (data['population'] > 0)] ['median_house_value'].mean()}")

print(f"Максимальная households в зоне минимального значения population --> {data[data['population'] == data['population'].min()]['households'].max()}")