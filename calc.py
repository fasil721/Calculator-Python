import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
LABEL_COLOR = "#25265E"
GRAY = '#F0EAEA'

window = tk.Tk()
window.geometry('375x667')
window.resizable(0, 0)
window.title('Calculator')

display_frame = tk.Frame(window, bg=GRAY, height=221)
display_frame.pack(expand=True, fill='both')

button_frame = tk.Frame(window)
button_frame.pack(expand=True, fill='both')

total_expression = "0"
current_expression = "0"
display_total_label = tk.Label(display_frame, text=total_expression, anchor=tk.E, bg=GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
display_total_label.pack(expand=True, fill='both')

display_label = tk.Label(display_frame, text=current_expression, anchor=tk.E, bg=GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
display_label.pack(expand=True, fill='both')

window.mainloop()
