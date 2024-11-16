import os
import pandas as pd
import matplotlib.pyplot as plt

def create_period(df: pd.DataFrame, start_date: str, end_date: str):
    """Функция для построения графика изменения курса за весь период."""
    plt.figure(figsize=(12, 7))
    plt.plot(df['date'], df['value'], marker='o', linestyle='-', color='#1f77b4', label='Курс', markersize=6)
    title = f'Изменение курса за период с {start_date} по {end_date}' if start_date and end_date else 'Изменение курса за весь период'
    plt.title(title, fontsize=18)
    plt.xlabel('Дата', fontsize=14)
    plt.ylabel('Курс', fontsize=14)
    plt.xticks(rotation=45)

    # Аннотируем значения на графике
    for i, value in enumerate(df['value']):
        plt.text(df['date'].iloc[i], value, f'{value:.2f}', fontsize=9, ha='right', va='bottom')

    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(loc='upper left', fontsize=12)
    plt.tight_layout()
    plt.show(block=True)
