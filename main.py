import tkinter as tk
import functions as func

window = tk.Tk()
window.title("PassGen")
window.geometry("420x420")

title = tk.Label(window, text="PassGen", font=("Arial", 15))
title.pack()

options = ['lowercase', 'uppercase', 'lowercase/uppercase', 'none']

clicked = tk.StringVar()
clicked.set('lowercase/uppercase')

chars = tk.OptionMenu(window, clicked, *options)

chars.pack()

numbers = tk.IntVar()
symbols = tk.IntVar()

numbers_checkbox = tk.Checkbutton(window, text="Numbers", variable=numbers, onvalue=1, offvalue=0)
numbers_checkbox.pack()

symbols_checkbox = tk.Checkbutton(window, text="Symbols", variable=symbols, onvalue=1, offvalue=0)
symbols_checkbox.pack()

length = tk.Entry(window)
length.pack()
submit = tk.Button(window, text="Submit", command=lambda: [
                                                    password.delete("1.0", tk.END),
                                                    password.insert(tk.END, func.generate_password(length.get(), [clicked.get(), numbers.get(), symbols.get()]))
                                                    ])
submit.pack(pady=10)

password = tk.Text(window)
password.pack()

window.mainloop()