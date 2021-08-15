import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
LABEL_COLOR = "#25265E"
GRAY = '#F0EAEA'
WHITE = "#FFFFFF"

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

digits = {
    7: (1, 1), 8: (1, 2), 9: (1, 3),
    4: (2, 1), 5: (2, 2), 6: (2, 3),
    1: (3, 1), 2: (3, 2), 3: (3, 3),
    0: (4, 2), '.': (4, 1)
}
for digit, grid_value in digits.items():
    button = tk.Button(button_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                       borderwidth=0)
    button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

window.mainloop()
