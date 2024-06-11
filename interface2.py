# интерфейс приложения
# импорт
import tkinter as tk


# блок функций
def show_special():  # функция, отображающая фрейм S.P.E.C.I.A.L.
    frame_hello.grid_forget()  # фрейм приветствия скрывается
    frame_setting.grid_forget()  # фрейм настройки скрывается
    frame_special.grid(row=1, rowspan=3, column=0, columnspan=7)  # располагаем фрейм S.P.E.C.I.A.L. в корневом окне


def show_setting():  # функция, отображающая фрейм настройки
    frame_hello.grid_forget()  # фрейм приветствия скрывается
    frame_special.grid_forget()  # фрейм S.P.E.C.I.A.L. скрывается
    frame_setting.grid(row=1, rowspan=3, column=0, columnspan=5)  # располагаем фрейм настройки в корневом окне


def fullscreen_mode():  # функция, отвечающая за полноэкранный режим
    global fullscreen  # добавляем флаг полноэкранного режима
    fullscreen = not fullscreen  # меняем значение флага на противоположное
    root.attributes("-fullscreen", fullscreen)  # включаем или выключаем полноэкранный режим

    # изменение подписи кнопки в зависимости от статуса полноэкранного режима
    if fullscreen:
        b_fullscreen['text'] = 'ВКЛ'
    else:
        b_fullscreen['text'] = 'ВЫКЛ'


# основное окно
root = tk.Tk()  # переменная корневого окна
root_wight = root.winfo_screenwidth()  # ширина пользовательского дисплея
root_height = root.winfo_screenheight()  # высота пользовательского дисплея
# разрешение основного окна
root.geometry(f'{root_wight}x{root_height}+0+0')  # оно принимает размеры пользовательского дисплея
root.title('Pip-Boy')  # название окна
root.config(bg='black')  # настройка корневого окна
root.iconbitmap('logo.ico')
fullscreen = False  # отслеживание полноэкранного режима

# объявляем фреймы
frame_menu = tk.Frame(bg='#25ff00')  # фрейм верхнего меню
frame_hello = tk.Frame(bg='black')  # фрейм приветствия
frame_special = tk.Frame(bg='#25ff00')  # фрейм S.P.E.C.I.A.L.
frame_create = tk.Frame(bg='black')  # фрейм создания персонажа
frame_simulation = tk.Frame(bg='black')  # фрейм симуляции боя
frame_setting = tk.Frame(bg='black')  # фрейм настройки

# заполнение фреймов
# фрейм верхнего меню (отображается всегда)
# расчёт ширины ячеек фрейма
for i in range(5):  # ширина окна делится на количество ячеек
    frame_menu.grid_columnconfigure(i, minsize=round(root_wight/5))  # минимальный размер ячейки - 1/5 окна

# кнопки верхнего меню
# кнопка перехода к S.P.E.C.I.A.L.
(tk.Button(frame_menu, text='S.P.E.C.I.A.L.', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/75)),
           activebackground='#25ff00', borderwidth=0, command=show_special)
 .grid(row=0, column=0, pady=(0, round(root_wight/500)), padx=(0, round(root_wight/1000)), sticky='news'))
# кнопка перехода к созданию
(tk.Button(frame_menu, text='СОЗДАНИЕ', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/75)),
           activebackground='#25ff00', borderwidth=0)
 .grid(row=0, column=1, pady=(0, round(root_wight/500)), padx=round(root_wight/1000), sticky='news'))
# кнопка перехода к симуляции
(tk.Button(frame_menu, text='СИМУЛЯЦИЯ', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/75)),
           activebackground='#25ff00', borderwidth=0)
 .grid(row=0, column=2, pady=(0, round(root_wight/500)), padx=round(root_wight/1000), sticky='news'))
# кнопка перехода к настройкам
(tk.Button(frame_menu, text='НАСТРОЙКИ', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/75)),
           activebackground='#25ff00', borderwidth=0, command=show_setting)
 .grid(row=0, column=3, pady=(0, round(root_wight/500)), padx=round(root_wight/1000), sticky='news'))
# кнопка выхода
(tk.Button(frame_menu, text='ВЫХОД', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/75)),
           activebackground='#25ff00', borderwidth=0, command=lambda: root.quit())
 .grid(row=0, column=4, pady=(0, round(root_wight/500)), padx=(round(root_wight/1000), 0), sticky='news'))

frame_menu.grid(row=0, column=0, columnspan=5)  # отображение верхнего меню в корневом окне

# фрейм приветствия (отображается при запуске программы)
# расчёт ширины ячеек фрейма
for i in range(5):  # ширина окна делится на количество ячеек
    frame_hello.grid_columnconfigure(i, minsize=round(root_wight/5))  # минимальный размер ячейки - 1/5 окна

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
         font=('Fallout Regular', round(root_wight/50)), pady=round(root_wight/50)).grid(row=2, column=1, columnspan=3)

# размещение основного текста фрейма приветствия
tk.Label(frame_hello, text=text_hello, fg='#25ff00', bg='black', wraplength=root_wight, justify='left',
         font=('Fallout Regular', round(root_wight/75))).grid(row=3, column=0, columnspan=5)

frame_hello.grid(row=1, rowspan=2, column=0, columnspan=5)  # расположение фрейма приветствия в корневом окне

# фрейм S.P.E.C.I.A.L. (отображается при нажатии на кнопку S.P.E.C.I.A.L.)
# расчёт ширины ячеек фрейма
for i in range(7):  # ширина окна делится на количество ячеек
    frame_special.grid_columnconfigure(i, minsize=round(root_wight/7))  # минимальный размер ячейки - 1/7 окна

# верхнее меню (содержит 7 атрибутов)
# сила
(tk.Button(frame_special, text='СИЛА', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/90)),
           activebackground='#25ff00', borderwidth=0, command=show_special)
 .grid(row=1, column=0, pady=(0, round(root_wight / 500)), padx=(0, round(root_wight / 1000)), sticky='news'))
# восприятие
(tk.Button(frame_special, text='ВОСПРИЯТИЕ', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/90)),
           activebackground='#25ff00', borderwidth=0, command=show_special)
 .grid(row=1, column=1, pady=(0, round(root_wight / 500)), padx=round(root_wight / 1000), sticky='news'))
# выносливость
(tk.Button(frame_special, text='ВЫНОСЛИВОСТЬ', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/90)),
           activebackground='#25ff00', borderwidth=0, command=show_special)
 .grid(row=1, column=2, pady=(0, round(root_wight / 500)), padx=round(root_wight / 1000), sticky='news'))
# харизма
(tk.Button(frame_special, text='ХАРИЗМА', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/90)),
           activebackground='#25ff00', borderwidth=0, command=show_special)
 .grid(row=1, column=3, pady=(0, round(root_wight / 500)), padx=round(root_wight / 1000), sticky='news'))
# интеллект
(tk.Button(frame_special, text='ИНТЕЛЛЕКТ', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/90)),
           activebackground='#25ff00', borderwidth=0, command=show_special)
 .grid(row=1, column=4, pady=(0, round(root_wight / 500)), padx=round(root_wight / 1000), sticky='news'))
# ловкость
(tk.Button(frame_special, text='ЛОВКОСТЬ', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/90)),
           activebackground='#25ff00', borderwidth=0, command=show_special)
 .grid(row=1, column=5, pady=(0, round(root_wight / 500)), padx=round(root_wight / 1000), sticky='news'))
# удача
(tk.Button(frame_special, text='УДАЧА', bg='black', fg='#25ff00', font=('Fallout Regular', round(root_wight/90)),
           activebackground='#25ff00', borderwidth=0, command=show_special)
 .grid(row=1, column=6, pady=(0, round(root_wight / 500)), padx=(round(root_wight / 1000), 0), sticky='news'))

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
(tk.Label(frame_special, text=title_special, fg='#25ff00', bg='black', wraplength=root_wight, justify='left',
          font=('Fallout Regular', round(root_wight/50)), pady=round(root_wight/50))
 .grid(row=2, column=0, columnspan=7, sticky='news'))

# размещение основного текста фрейма S.P.E.C.I.A.L.
tk.Label(frame_special, text=text_special, fg='#25ff00', bg='black', wraplength=root_wight, justify='left',
         font=('Fallout Regular', round(root_wight/75))).grid(row=3, column=0, columnspan=7, sticky='news')

# фрейм настройки
# расчёт ширины ячеек фрейма
for i in range(5):  # ширина окна делится на количество ячеек
    frame_setting.grid_columnconfigure(i, minsize=round(root_wight/5))  # минимальный размер ячейки - 1/5 окна

title_setting = 'НАСТРОЙКИ'  # заголовок

tk.Label(frame_setting, text=title_setting, fg='#25ff00', bg='black', wraplength=root_wight, justify='left',
         font=('Fallout Regular', round(root_wight/50)), pady=round(root_wight/50)).grid(row=1, column=0, columnspan=5)

# настройка полноэкранного режима
# подпись
tk.Label(frame_setting, text='Полноэкранный режим -> ', fg='#25ff00', bg='black',
         font=('Fallout Regular', round(root_wight/75))).grid(row=2, column=0)
# кнопка (объявляется через переменную для изменения её подписи)
b_fullscreen = tk.Button(frame_setting, text='ВЫКЛ', fg='#25ff00', bg='black',
                         font=('Fallout Regular', round(root_wight/75)), borderwidth=0, activebackground='#25ff00',
                         command=fullscreen_mode)
b_fullscreen.grid(row=2, column=1, sticky='w')  # размещение кнопки

# текущее разрешение экрана
# подпись
tk.Label(frame_setting, text='Текущее разрешение -> ', fg='#25ff00', bg='black',
         font=('Fallout Regular', round(root_wight/75))).grid(row=3, column=0)
# значение
tk.Label(frame_setting, text=f'{root_wight}x{root_height}', fg='#25ff00', bg='black',
         font=('Fallout Regular', round(root_wight/75))).grid(row=3, column=1, sticky='w')

root.mainloop()  # цикл корневого окна
