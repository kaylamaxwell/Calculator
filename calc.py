from tkinter import *
import math
from tkinter import messagebox



root = Tk()
output_string = StringVar()
output_string.set("0")
first_number = ""
second_number = ""
first_float = 0
second_float = 0.0
operator_clicked = False
operator_string = ''

root.geometry("400x400")
root.resizable(False, False)
for i in range(4):
    Grid.columnconfigure(root, i, weight=1)
    Grid.rowconfigure(root, i, weight=1)

Grid.rowconfigure(root, 4, weight=1)


def operator(item):
    global operator_clicked
    global operator_string
    global first_number
    global second_number
    if second_number != '':
        execute()
    operator_string = item
    operator_clicked = True
    output_string.set(first_number + operator_string)


def change(item):
    global first_number
    global second_number
    global operator_clicked
    global operator_string
    global output_string
    if not operator_clicked:
        first_number += item
        output_string.set(first_number)
    else:
        second_number += item
        output_string.set(first_number + operator_string + second_number)


def pi_button():
    output_string.set(str(math.pi))


def sqrt_button():
    result = math.sqrt(float(output_string.get()))
    output_string.set(result)


def execute():
    global first_number
    global second_number
    first_float = float(first_number)
    second_float = float(second_number)
    if operator_string == '+':
        result = first_float + second_float
        output_string.set(result)
    elif operator_string == '-':
        result = first_float - second_float
        output_string.set(result)
    elif operator_string == '*':
        result = first_float * second_float
        output_string.set(result)
    elif operator_string == '/':
        if second_float == 0:
            output_string.set("Cannot divide by zero")
            messagebox.showerror("ERROR", "Cannot divide by zero")
            output_string.set('0')
            return
        else:
            result = first_float / second_float
            output_string.set(result)
    elif operator_string == '**':
        expression = f"{first_float} ** {second_float}"
        result = eval(expression)
        output_string.set(result)
    elif operator_string == 'Sqrt':
        result = math.sqrt(first_float)
        output_string.set(result)
    elif operator_string == 'sin':
        result = math.sin(math.radians(output_string.get()))
        output_string.set(result)
    elif operator_string == 'cos':
        result = math.cos(math.radians(output_string.get()))
        output_string.set(result)
    elif operator_string == 'tan':
        result = math.tan(math.radians(output_string.get()))
        output_string.set(result)
    first_number = str(result)
    second_number = ''


def tan():
    result = math.tan(math.radians(float(output_string.get())))
    output_string.set(result)


def sin():
    result = math.sin(math.radians(float(output_string.get())))
    output_string.set(result)


def cos():
    result = math.cos(math.radians(float(output_string.get())))
    output_string.set(result)


def clear():
    global first_number
    global second_number
    global operator_string
    global output_string
    global operator_clicked
    operator_clicked = False
    operator_string = ''
    first_number = ''
    second_number = ''
    output_string.set("0")


def delete():
    current_value = output_string.get()
    if current_value == "0":
        return

    new_value = current_value[:-1]
    if not new_value:
        new_value = "0"

    output_string.set(new_value)


seven_button = Button(root, text="7", height=3, width=7, command=lambda: change("7"), font='bold')
eight_button = Button(root, text="8", height=3, width=7, command=lambda: change("8"), font='bold')
nine_button = Button(root, text="9", height=3, width=7, command=lambda: change("9"), font='bold')
divide_button = Button(root, text="/", height=3, width=7, command=lambda: operator('/'), font='bold')
four_button = Button(root, text="4", height=3, width=7, command=lambda: change("4"), font='bold')
five_button = Button(root, text="5", height=3, width=7, command=lambda: change("5"), font='bold')
six_button = Button(root, text="6", height=3, width=7, command=lambda: change("6"), font='bold')
multiply_button = Button(root, text="*", height=3, width=7, command=lambda: operator('*'), font='bold')
one_button = Button(root, text="1", height=3, width=7, command=lambda: change("1"), font='bold')
two_button = Button(root, text="2", height=3, width=7, command=lambda: change("2"), font='bold')
three_button = Button(root, text="3", height=3, width=7, command=lambda: change("3"), font='bold')
subtract_button = Button(root, text="-", height=3, width=7, command=lambda: operator('-'), font='bold')
zero_button = Button(root, text="0", height=3, width=7, command=lambda: change("0"), font='bold')
decimal_button = Button(root, text=".", height=3, width=7, command=lambda: change("."), font='bold')
equal_button = Button(root, text="=", height=3, width=7, command=execute, font='bold')
plus_button = Button(root, text="+", height=3, width=7, command=lambda: operator('+'), font='bold')
output_label = Label(root, textvariable=output_string, bg="white", fg="black", height=3, width=40, anchor="e", font = 'bold')
clear_button = Button(root, text="CLR", height=3, width=7, command=clear, font='bold')
power_button = Button(root, text="**", height=3, width=7, command=lambda: operator('**'), font='bold')
sqrt_button = Button(root, text="Sqrt", height=3, width=7, command=sqrt_button, font='bold')
pi_button = Button(root, text="Pi", height=3, width=7, command=pi_button, font='bold')
tan_button = Button(root, text="Tan", height=3, width=7, command=tan, font='bold')
cos_button = Button(root, text="Cos", height=3, width=7, command=cos, font='bold')
sin_button = Button(root, text="Sin", height=3, width=7, command=sin, font='bold')
delete_button = Button(root, text="Del", height=3, width=7, command=delete, font='bold')

power_button.grid(row=5, column=0)
sqrt_button.grid(row=5, column=1)
pi_button.grid(row=5, column=2)
tan_button.grid(row=6, column=2)
cos_button.grid(row=6, column=0)
sin_button.grid(row=6, column=1)
seven_button.grid(row=1, column=0)
eight_button.grid(row=1, column=1)
nine_button.grid(row=1, column=2)
divide_button.grid(row=1, column=3)
four_button.grid(row=2, column=0)
five_button.grid(row=2, column=1)
six_button.grid(row=2, column=2)
multiply_button.grid(row=2, column=3)
one_button.grid(row=3, column=0)
two_button.grid(row=3, column=1)
three_button.grid(row=3, column=2)
subtract_button.grid(row=3, column=3)
zero_button.grid(row=4, column=0)
decimal_button.grid(row=4, column=1)
equal_button.grid(row=4, column=2)
plus_button.grid(row=4, column=3)
output_label.grid(row=0, column=0, columnspan=4)
clear_button.grid(row=5, column=3)
delete_button.grid(row=5, column=2)

root.title("Calculator")
root.mainloop()
