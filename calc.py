import tkinter as tk

GRAY = '#F0EAEA'

window = tk.Tk()
window.geometry('375x667')
window.resizable(0, 0)
window.title('Calculator')


def display_frame():
    frame = tk.Frame(window, bg=GRAY, height=221)
    frame.pack(expand=True, fill='both')


def button_frame():
    frame = tk.Frame(window)
    frame.pack(expand=True, fill='both')


display_frame()
button_frame()
window.mainloop()
