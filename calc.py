import tkinter as tk

LABEL_COLOR = "#25265E"
GRAY = '#F0EAEA'
OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LARGE_FONT_STYLE = ("Arial", 35, "bold")
SMALL_FONT_STYLE = ("Arial", 15)
DIGITS_FONT_STYLE = ("Arial", 20, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

window = tk.Tk()
window.geometry('325x475')
window.resizable(0, 0)
window.title('Calculator')

display_frame = tk.Frame(window, bg=GRAY, height=221)
display_frame.pack(expand=True, fill='both')

button_frame = tk.Frame(window)
button_frame.pack(expand=True, fill='both')

total_expression = ''
current_expression = ''

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
operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}


def update_label():
    display_label.config(text=current_expression[:11])


def update_total_label():
    expression = total_expression
    for operator, symbol in operations.items():
        expression = expression.replace(operator, f' {symbol} ')
    display_total_label.config(text=expression)


def add_to_expression(value):
    global current_expression
    current_expression += str(value)
    update_label()


def append_operator(operator):
    global current_expression
    global total_expression
    current_expression += operator
    total_expression += current_expression
    current_expression = ''
    update_total_label()
    update_label()


def evaluate():
    global current_expression
    global total_expression
    total_expression += current_expression
    update_total_label()
    try:
        current_expression = str(eval(total_expression))
        total_expression = ''
    except Exception as e:
        current_expression = 'Error'
    finally:
        update_label()


def clear():
    global current_expression
    global total_expression
    current_expression = ''
    total_expression = ''
    update_total_label()
    update_label()


def delete():
    global current_expression
    global total_expression
    if total_expression[:-1]:
        total_expression = total_expression[:-1]
        current_expression = total_expression
        total_expression = ''
        update_total_label()
        update_label()
    else:
        current_expression = current_expression[:-1]
        update_label()


def bind_key():
    window.bind("<Return>", lambda event: evaluate())
    for key in digits:
        window.bind(str(key), lambda event, digit=key: add_to_expression(digit))

    for key in operations:
        window.bind(key, lambda event, operator=key: append_operator(operator))


for digit, grid_value in digits.items():
    button = tk.Button(button_frame, text=digit, bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                       borderwidth=0, command=lambda n=digit: add_to_expression(n))
    button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
i = 0
for operator, symbol in operations.items():
    button = tk.Button(button_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                       borderwidth=0, command=lambda o=operator: append_operator(o))
    button.grid(row=i, column=4, sticky=tk.NSEW)
    i += 1
for x in range(1, 5):
    button_frame.rowconfigure(x, weight=1)
    button_frame.columnconfigure(x, weight=1)
    bind_key()

clear_button = tk.Button(button_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                         borderwidth=0, command=clear)
clear_button.grid(row=0, column=1, columnspan=2, sticky=tk.NSEW)

delete_button = tk.Button(button_frame, text="\u232B", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                          borderwidth=0, command=delete)
delete_button.grid(row=0, column=3, sticky=tk.NSEW)

equal_button = tk.Button(button_frame, text='=', bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                         borderwidth=0, command=evaluate)
equal_button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

window.mainloop()
