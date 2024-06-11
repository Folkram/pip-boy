# интерфейс приложения
# импорт
import tkinter as tk


# блок функций
def show_special():  # функция, отображающая фрейм S.P.E.C.I.A.L.
    frame_hello.grid_forget()  # фрейм приветствия скрывается
    frame_special.grid(row=1, rowspan=2, column=0, columnspan=5)  # располагаем фрейм S.P.E.C.I.A.L. в корневом окне


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
          activebackground='#25ff00', borderwidth=0, command=show_special).grid(row=0, column=0, sticky='nsew')
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

# заполнение фреймов
# фрейм приветствия (отображается при запуске программы)
title_hello = 'Вас приветствует ваш Pip-Boy 3000!'  # заголовок
# основной текст
text_hello = ('Персональный процессор производства «РобКо Индастриз». В рамках партнёрства с «Волт-Тек» они были выданы'
              ' многим обитателям Убежищ, хотя из-за производственных ограничений и продолжающейся разработки разные'
              ' Убежища получали поставки разных версий. Чаще всего встречаются версии Пип-Бой 2000 и Пип-бой 3000,'
              ' которые предназначены для крепления на запястье владельца. Многие модели были разработаны с'
              ' биометрическими замками, предотвращающими их снятие, пока владелец ещё жив.\n'
              '\nС гордостью представляем вам удобный инструмент для работы с вашим пип-боем. С верху представлены'
              ' разделы к которым вы можете перейти по нажатию. Раздел S.P.E.C.I.A.L. даёт справочную информацию об'
              ' одноимённой системе улучшений с подробным описанием каждого атрибута. Раздел СОЗДАНИЕ предоставит вам'
              ' удобный функционал по распределению ваших навыков в системе S.P.E.C.I.A.L.. Раздел СИМУЛЯЦИЯ позволит'
              ' вам испытать ваши силы в симуляции. Раздел НАСТРОЙКИ позволит вам настроить пип-бой под ваши нужды.'
              ' Кнопка ВЫХОД позволит вам легко выйти из системы')

# размещение заголовка фрейма приветствия
tk.Label(frame_hello, text=title_hello, fg='#25ff00', bg='black', wraplength=root_wight, justify='left',
         font=('Fallout Regular', round(root_wight/50))).grid(row=2, column=1, columnspan=3, pady=round(root_wight/50))

# размещение основного текста фрейма приветствия
tk.Label(frame_hello, text=text_hello, fg='#25ff00', bg='black', wraplength=root_wight, justify='left',
         font=('Fallout Regular', round(root_wight/75))).grid(row=3, column=0, columnspan=5)

frame_hello.grid(row=1, rowspan=2, column=0, columnspan=5)  # расположение фрейма приветствия в корневом окне

# фрейм S.P.E.C.I.A.L. (отображается при нажатии на кнопку S.P.E.C.I.A.L.)
title_special = 'S.P.E.C.I.A.L.'  # заголовок
# основной текст
text_special = ('S.P.E.C.I.A.L - Это система которая делает вас уникальными! В наличии имеются 7 атрибутов,'
                ' которые будет возможность прокачивать. Атрибуты это Сила, Восприятие, Выносливость, Харизма,'
                ' Интеллект, Ловкость и Удача. Помимо этих основных атрибутов, будут так-же доступны дополнительные'
                ' параметры, которые можно улучшать отдельно. По достижению нового уровня (когда начисляются очки),'
                ' у вас будет возможность открыть любую особую способность, которая даст вам уникальный навык. Далее'
                ' будет подробно описан каждый атрибут, за что он отвечает и на что влияет в вашем выживании в'
                ' пустошах!')

# размещение заголовка фрейма S.P.E.C.I.A.L.
tk.Label(frame_special, text=title_special, fg='#25ff00', bg='black', wraplength=root_wight, justify='left',
         font=('Fallout Regular', round(root_wight/50))).grid(row=2, column=1, columnspan=3, pady=round(root_wight/50))

# размещение основного текста фрейма S.P.E.C.I.A.L.
tk.Label(frame_special, text=text_special, fg='#25ff00', bg='black', wraplength=root_wight, justify='left',
         font=('Fallout Regular', round(root_wight/75))).grid(row=3, column=0, columnspan=5)

# расчёт ширины ячеек
for i in range(5):  # ширина окна делится на количество ячеек
    root.grid_columnconfigure(i, minsize=round(root_wight/5))  # минимальный размер ячейки - 1/5 окна

root.mainloop()  # цикл корневого окна
