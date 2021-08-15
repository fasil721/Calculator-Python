import tkinter as tk

GRAY = '#F0EAEA'

window = tk.Tk()
window.geometry('375x500')
window.resizable(0, 100)
window.title('Calculator')

display_frame = tk.Frame()
display_frame = tk.Frame(window, bg=GRAY, height=100)
display_frame.pack(expand=True, fill='both')

button_frame = tk.Frame()
button_frame = tk.Frame(window)
button_frame.pack(expand=True, fill='both')

window.mainloop()
