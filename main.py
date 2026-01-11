import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from tkinter import ttk

class FinancialCircleApp:
    def __init__(self, master):
        self.master = master
        master.title("Financial Circle")

        self.variables = []  # Список для хранения переменных
        self.percents = []   # Список для хранения процентов

        # Поля для ввода переменной и процента
        self.variable_label = ttk.Label(master, text="Переменная:")
        self.variable_label.grid(row=0, column=0, pady=6)

        self.variable_entry = ttk.Entry(master)
        self.variable_entry.grid(row=0, column=1, pady=6)

        self.percent_label = ttk.Label(master, text="Процент:")
        self.percent_label.grid(row=1, column=0, pady=6)

        self.percent_entry = ttk.Entry(master)
        self.percent_entry.grid(row=1, column=1, pady=6)

        self.name_entry = ttk.Label(master, text="Название круга:")
        self.name_entry.grid(row=2, column=0, pady=6)

        self.name_label = ttk.Entry(master)
        self.name_label.grid(row=2, column=1, pady=6)

        # Кнопка "Добавить"
        self.add_button = ttk.Button(master, text="Добавить", command=self.add_variable)
        self.add_button.grid(row=3, columnspan=2, pady=6)

        # Кнопка "Построить круг"
        self.plot_button = ttk.Button(master, text="Построить круг", command=self.plot_circle)
        self.plot_button.grid(row=4, columnspan=2, pady=6)

        self.clear_button = ttk.Button(master, text="очистить переменные", command=self.clear_circle)
        self.clear_button.grid(row=5, columnspan=2, pady=6)

        self.table = PrettyTable()
        self.table.field_names = self.variables
        self.table.add_row(self.percents)
        self.circle_sys = ttk.Label(self.master, text=self.table)
        self.circle_sys.grid(row=6, column=0)

    def add_variable(self):
        variable = self.variable_entry.get()
        percent_str = self.percent_entry.get()

        try:
            percent = float(percent_str)
            if not (0 <= percent <= 100):
                raise ValueError("Процент должен быть от 0 до 100")
            self.variables.append(variable)
            self.percents.append(percent)
            self.variable_entry.delete(0, tk.END)  # Очистка поля
            self.percent_entry.delete(0, tk.END)   # Очистка поля
            messagebox.showinfo("Успех", f"Переменная '{variable}' с процентом {percent}% добавлена.")

            self.table = PrettyTable()
            self.table.field_names = self.variables
            self.table.add_row(self.percents)
            self.circle_sys.config(text=self.table)


        except ValueError as e:
            messagebox.showerror("Ошибка ввода", str(e))

    def plot_circle(self):
        if not self.variables:
            messagebox.showwarning("Предупреждение", "Вы не добавили ни одной переменной.")
            return

        total_percent = sum(self.percents)
        if total_percent > 100:
            messagebox.showerror("Ошибка", "Сумма процентов не должна превышать 100.")
            return

        # Если сумма процентов меньше 100, добавляем "Другие"
        if total_percent < 100:
            self.variables.append("Другие")
            self.percents.append(100 - total_percent)

        self.draw_circle()

    def draw_circle(self):
        plt.figure(figsize=(6, 6))
        plt.pie(self.percents, labels=self.variables, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')  # Делает круг круглым
        plt.title(self.name_label.get())
        plt.show()
        try:
            self.ind = self.variables.index("Другие")
            self.variables.pop(self.ind)
            self.percents.pop(self.ind)
        except:
            pass
    
    def clear_circle(self):
        self.variables = []
        self.percents = []
        messagebox.showinfo("Успех", "переменные очищены")

        self.table = PrettyTable()
        self.table.field_names = self.variables
        self.table.add_row(self.percents)
        self.circle_sys.config(text=self.table)


if __name__ == "__main__":
    root = tk.Tk()

    # Import the tcl file
    root.tk.call('source', 'Forest-ttk-theme-master/forest-dark.tcl')

    # Set the theme with the theme_use method
    ttk.Style().theme_use('forest-dark')

    app = FinancialCircleApp(root)
    root.mainloop()
