# интерфейс приложения
# импорт
import tkinter as tk

# основное окно
root = tk.Tk()  # переменная корневого окна
root_wight = root.winfo_screenwidth()  # ширина пользовательского дисплея
root_height = root.winfo_screenheight()  # высота пользовательского дисплея
# разрешение основного окна
root.geometry(f'{root_wight}x{root_height}+0+0')  # оно принимает размеры пользовательского дисплея
root.title('Pip-Boy')  # название окна
root.config(bg='black')  # настройка корневого окна
fullscreen = False  # отслеживание полноэкранного режима

# объявляем фреймы
frame_hello = tk.Frame(bg='black')  # фрейм приветствия
frame_special = tk.Frame(bg='black')  # фрейм S.P.E.C.I.A.L.
frame_create = tk.Frame(bg='black')  # фрейм создания персонажа
frame_simulation = tk.Frame(bg='black')  # фрейм симуляции боя

# кнопки верхнего меню
# кнопка перехода к S.P.E.C.I.A.L.
tk.Button(text='S.P.E.C.I.A.L.', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/75)),
          activebackground='#25ff00', borderwidth=0).grid(row=0, column=0, sticky='nsew')
# кнопка перехода к созданию
tk.Button(text='СОЗДАНИЕ', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/75)),
          activebackground='#25ff00', borderwidth=0).grid(row=0, column=1, sticky='nsew')
# кнопка перехода к симуляции
tk.Button(text='СИМУЛЯЦИЯ', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/75)),
          activebackground='#25ff00', borderwidth=0).grid(row=0, column=2, sticky='nsew')
# кнопка перехода к настройкам
tk.Button(text='НАСТРОЙКИ', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/75)),
          activebackground='#25ff00', borderwidth=0).grid(row=0, column=3, sticky='nsew')
# кнопка выхода
tk.Button(text='ВЫХОД', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/75)),
          activebackground='#25ff00', borderwidth=0, command=lambda: root.quit()).grid(row=0, column=4, sticky='nsew')

# расчёт ширины ячеек
for i in range(5):  # ширина окна делится на количество ячеек
    root.grid_columnconfigure(i, minsize=round(root_wight/5))  # минимальный размер ячейки - 1/5 окна

root.mainloop()  # цикл корневого окна
