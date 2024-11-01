import tkinter as tk
from tkinter import messagebox
import pandas as pd
from fpdf import FPDF
import os

# Создаем основное окно приложения
root = tk.Tk()
root.title("Приложение для работы с Excel и PDF")
root.geometry("400x300")

# Функция для экспорта данных в Excel
def export_to_excel():
    # Получаем данные из полей ввода
    data = {
        "Имя": entry_name.get(),
        "Возраст": entry_age.get(),
        "Город": entry_city.get()
    }
    df = pd.DataFrame([data])

    # Сохранение данных в Excel
    df.to_excel("output.xlsx", index=False)
    messagebox.showinfo("Успех", "Данные успешно сохранены в Excel!")

# Функция для экспорта данных в PDF
def export_to_pdf():
    # Получаем данные из полей ввода
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Данные пользователя", ln=True, align="C")

    pdf.cell(200, 10, txt=f"Имя: {entry_name.get()}", ln=True)
    pdf.cell(200, 10, txt=f"Возраст: {entry_age.get()}", ln=True)
    pdf.cell(200, 10, txt=f"Город: {entry_city.get()}", ln=True)

    # Сохранение данных в PDF
    pdf.output("output.pdf")
    messagebox.showinfo("Успех", "Данные успешно сохранены в PDF!")

# Поля для ввода данных
tk.Label(root, text="Имя:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="Возраст:").pack(pady=5)
entry_age = tk.Entry(root)
entry_age.pack(pady=5)

tk.Label(root, text="Город:").pack(pady=5)
entry_city = tk.Entry(root)
entry_city.pack(pady=5)

# Кнопки для экспорта
btn_excel = tk.Button(root, text="Сохранить в Excel", command=export_to_excel)
btn_excel.pack(pady=10)

btn_pdf = tk.Button(root, text="Сохранить в PDF", command=export_to_pdf)
btn_pdf.pack(pady=10)

# Запуск основного цикла
root.mainloop()
