import tkinter as tk
from tkinter import filedialog

from cipher import encrypt, decrypt

window = tk.Tk()

window.geometry('550x250')
window.columnconfigure([0, 1, 2], minsize=50, weight=1)


def open_file():
    file_path = filedialog.askopenfilename()
    label_path['text'] = file_path if file_path else 'Выберите файл'
    label_path['fg'] = 'black'


def save_file():
    if label_path.cget('text') == 'Выберите файл':
        label_path['fg'] = 'red'
    elif not input_pass.get():
        label_pass['fg'] = 'red'
    else:
        if method.get():
            result, status = encrypt(label_path.cget('text'), input_pass.get(), del_file.get())
        else:
            ext = input_ext.get() if input_ext.get() else '.txt'
            result, status = decrypt(label_path.cget('text'), input_pass.get(), ext, del_file.get())

        show_label_info(result, status)


def show_input_ext():
    label_ext.place(x=32, y=150)
    input_ext.grid(row=6, column=1, padx=10, pady=27, sticky="nsew")


def hide_input_ext():
    label_ext.place_forget()
    input_ext.grid_forget()


def show_label_info(text, status):
    label_info.place(x=200, y=2)
    label_info['text'] = text
    label_info['fg'] = 'green' if status else 'red'


method = tk.BooleanVar()
method.set(True)

del_file = tk.BooleanVar()
del_file.set(False)

open_btn = tk.Button(text='Выбрать файл', width=20, command=open_file)
open_btn.grid(row=0, column=0, padx=30, pady=15, sticky="nsew", )

btn_delete = tk.Checkbutton(text='Удалить исходный файл?', width=25, variable=del_file)
btn_delete.grid(row=0, column=1, sticky="nsew")

label_path = tk.Label(text='Выберите файл')
label_path.place(x=32, y=45)

label_method = tk.Label(text='Выберите метод')
label_method.grid(row=2, column=0, pady=15, sticky="nsew")

radio_dec_btn = tk.Radiobutton(text='Зашифровать файл', variable=method, value=True, command=hide_input_ext)
radio_dec_btn.grid(row=2, column=1, pady=15, sticky="nsew")

radio_enc_btn = tk.Radiobutton(text='Дешифровать файл', variable=method, value=False, command=show_input_ext)
radio_enc_btn.grid(row=2, column=3, pady=15, padx=10, sticky="nsew")

label_pass = tk.Label(text='Укажите пароль')
label_pass.grid(row=3, column=0, pady=5, sticky="nsew")

input_pass = tk.Entry()
input_pass.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")

label_ext = tk.Label(text='Укажите расширение для файла (если не указать, файл сохраниться с расширением .txt)')
input_ext = tk.Entry()
input_ext.insert(0, '.txt')

save_btn = tk.Button(text='Сохранить файл', command=save_file)
save_btn.grid(row=8, column=1, padx=10, sticky="nsew")

label_info = tk.Label()

window.mainloop()
