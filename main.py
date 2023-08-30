import tkinter as tk
import functions as func

def toggle_checkbox():
    if characters.get() == 1:
        lowercase_checkbox.config(state=tk.NORMAL)
        uppercase_checkbox.config(state=tk.NORMAL)
    else:
        lowercase_checkbox.config(state=tk.DISABLED)
        uppercase_checkbox.config(state=tk.DISABLED)

window = tk.Tk()
window.title("PassGen")
window.geometry("420x420")

title = tk.Label(window, text="PassGen", font=("Arial", 15))
title.pack()

characters = tk.IntVar()
lowercase = tk.IntVar()
uppercase = tk.IntVar()
numbers = tk.IntVar()
symbols = tk.IntVar()

characters_checkbox = tk.Checkbutton(window, text="Characters", variable=characters, onvalue=1, offvalue=0, command=toggle_checkbox)
characters_checkbox.pack()

lowercase_checkbox = tk.Checkbutton(window, text="Lowercase", variable=lowercase, onvalue=1, offvalue=0, state=tk.DISABLED)
lowercase_checkbox.pack()

uppercase_checkbox = tk.Checkbutton(window, text="Uppercase", variable=uppercase, onvalue=1, offvalue=0, state=tk.DISABLED)
uppercase_checkbox.pack()

numbers_checkbox = tk.Checkbutton(window, text="Numbers", variable=numbers, onvalue=1, offvalue=0)
numbers_checkbox.pack()

symbols_checkbox = tk.Checkbutton(window, text="Symbols", variable=symbols, onvalue=1, offvalue=0)
symbols_checkbox.pack()

length = tk.Entry(window)
length.pack()
submit = tk.Button(window, text="Submit", command=lambda: [
                                                    password.delete("1.0", tk.END),
                                                    password.insert(tk.END, func.generate_password(length.get(), [characters.get(), numbers.get(), symbols.get()], [lowercase.get(), uppercase.get()]))
                                                    ])
submit.pack(pady=10)

password = tk.Text(window)
password.pack()

window.mainloop()