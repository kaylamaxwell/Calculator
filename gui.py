from tkinter import *
import math
from tkinter import messagebox


class GUI:
    def __init__(self, root) -> None:
        """
        Function to set up gui window
        :param root: Tkinter window
        """
        self.output_string: Variable = StringVar()
        self.output_string.set("0")
        self.first_number: str = ""
        self.second_number: str = ""
        self.operator_clicked: bool = False
        self.operator_string: str = ''

        self.seven_button = Button(root, text="7", height=3, width=7, command=lambda: self.change("7"), font='bold')
        self.eight_button = Button(root, text="8", height=3, width=7, command=lambda: self.change("8"), font='bold')
        self.nine_button = Button(root, text="9", height=3, width=7, command=lambda: self.change("9"), font='bold')
        self.divide_button = Button(root, text="/", height=3, width=7, command=lambda: self.operator('/'), font='bold')
        self.four_button = Button(root, text="4", height=3, width=7, command=lambda: self.change("4"), font='bold')
        self.five_button = Button(root, text="5", height=3, width=7, command=lambda: self.change("5"), font='bold')
        self.six_button = Button(root, text="6", height=3, width=7, command=lambda: self.change("6"), font='bold')
        self.multiply_button = Button(root, text="*", height=3, width=7, command=lambda: self.operator('*'),
                                      font='bold')
        self.one_button = Button(root, text="1", height=3, width=7, command=lambda: self.change("1"), font='bold')
        self.two_button = Button(root, text="2", height=3, width=7, command=lambda: self.change("2"), font='bold')
        self.three_button = Button(root, text="3", height=3, width=7, command=lambda: self.change("3"), font='bold')
        self.subtract_button = Button(root, text="-", height=3, width=7, command=lambda: self.operator('-'),
                                      font='bold')
        self.zero_button = Button(root, text="0", height=3, width=7, command=lambda: self.change("0"), font='bold')
        self.decimal_button = Button(root, text=".", height=3, width=7, command=lambda: self.change("."), font='bold')
        self.equal_button = Button(root, text="=", height=3, width=7, command=self.execute, font='bold')
        self.plus_button = Button(root, text="+", height=3, width=7, command=lambda: self.operator('+'), font='bold')
        self.output_label = Label(root, textvariable=self.output_string, bg="light gray", fg="black", height=3,
                                  width=40, anchor="e", font=('bold', 24))
        self.clear_button = Button(root, text="CLR", height=3, width=7, command=self.clear, font='bold')
        self.power_button = Button(root, text="**", height=3, width=7, command=lambda: self.operator('**'), font='bold')
        self.sqrt_button = Button(root, text="Sqrt", height=3, width=7, command=self.calculate_sqrt, font='bold')
        self.pi_button = Button(root, text="Pi", height=3, width=7, command=self.pi, font='bold')
        self.tan_button = Button(root, text="Tan", height=3, width=7, command=self.calculate_tan, font='bold')
        self.cos_button = Button(root, text="Cos", height=3, width=7, command=self.calculate_cos, font='bold')
        self.sin_button = Button(root, text="Sin", height=3, width=7, command=self.calculate_sin, font='bold')
        self.delete_button = Button(root, text="Del", height=3, width=7, command=self.delete, font='bold')

        self.seven_button.grid(row=1, column=0)
        self.eight_button.grid(row=1, column=1)
        self.nine_button.grid(row=1, column=2)
        self.divide_button.grid(row=1, column=3)
        self.four_button.grid(row=2, column=0)
        self.five_button.grid(row=2, column=1)
        self.six_button.grid(row=2, column=2)
        self.multiply_button.grid(row=2, column=3)
        self.one_button.grid(row=3, column=0)
        self.two_button.grid(row=3, column=1)
        self.three_button.grid(row=3, column=2)
        self.subtract_button.grid(row=3, column=3)
        self.zero_button.grid(row=4, column=0)
        self.decimal_button.grid(row=4, column=1)
        self.equal_button.grid(row=4, column=2)
        self.plus_button.grid(row=4, column=3)
        self.output_label.grid(row=0, column=0, columnspan=4)
        self.clear_button.grid(row=5, column=3)
        self.delete_button.grid(row=5, column=2)
        self.power_button.grid(row=5, column=0)
        self.sqrt_button.grid(row=5, column=1)
        self.pi_button.grid(row=6, column=0)
        self.tan_button.grid(row=6, column=1)
        self.cos_button.grid(row=6, column=2)
        self.sin_button.grid(row=6, column=3)

    def operator(self, item) -> None:
        """
        Sets the operator to the mathematical function pressed
        :param item: Math function
        :return: Math function
        """
        if self.second_number != '':
            self.execute()
        self.operator_string = item
        self.operator_clicked = True

    def pi(self) -> None:
        """
        Button for pi calculation
        :return: Pi
        """
        if not self.operator_clicked:
            self.first_number += str(math.pi)
            self.output_string.set(self.first_number)
        else:
            self.second_number += str(math.pi)
            self.output_string.set(self.first_number + self.operator_string + self.second_number)

    def calculate_sqrt(self) -> None:
        """
        Calculates square root of a number
        :return: square root of the number
        """
        result = math.sqrt(float(self.output_string.get()))
        self.output_string.set(result)

    def change(self, item) -> None:
        """
        Updates the output label with whatever button is pressed
        :param item: button
        :return: updated output label
        """
        if not self.operator_clicked:
            self.first_number += item
            self.output_string.set(self.first_number)
        else:
            self.second_number += item
            self.output_string.set(self.first_number + self.operator_string + self.second_number)

    def execute(self) -> None:
        """
        Performs the calculation
        :return:  result
        """
        first_float = float(self.first_number)
        second_float = float(self.second_number)
        result = 0

        if self.operator_string == '+':
            result = first_float + second_float
        elif self.operator_string == '-':
            result = first_float - second_float
        elif self.operator_string == '*':
            result = first_float * second_float
        elif self.operator_string == '/':
            if second_float == 0:
                messagebox.showerror("ERROR", "Cannot divide by zero")
                result = 0
            else:
                result = first_float / second_float
        elif self.operator_string == '**':
            result = first_float ** second_float
        elif self.operator_string == 'Sqrt':
            result = math.sqrt(first_float)
        elif self.operator_string == 'sin':
            result = math.sin(math.radians(first_float))
        elif self.operator_string == 'cos':
            result = math.cos(math.radians(first_float))
        elif self.operator_string == 'tan':
            result = math.tan(math.radians(first_float))

        self.output_string.set(result)
        self.first_number = str(result)
        self.second_number = ''
        self.operator_clicked = False

    def calculate_tan(self) -> None:
        """
        Calculates the tan of the current number
        :return: tan result
        """
        result = math.tan(math.radians(float(self.output_string.get())))
        self.output_string.set(result)

    def calculate_sin(self) -> None:
        """
        Calculates the sin of the current number
        :return: sin result
        """
        result = math.sin(math.radians(float(self.output_string.get())))
        self.output_string.set(result)

    def calculate_cos(self) -> None:
        """
        Calculates the cos of the current number
        :return: cos result
        """
        result = math.cos(math.radians(float(self.output_string.get())))
        self.output_string.set(result)

    def clear(self) -> None:
        """
        Clears the output label
        :return: Cleared output label
        """
        self.first_number = ""
        self.second_number = ""
        self.operator_string = ""
        self.operator_clicked = False
        self.output_string.set("0")

    def delete(self) -> None:
        """
        Deletes the last entry of the output label
        :return: last entry of the output label -1
        """
        current_value = self.output_string.get()
        if current_value == "0":
            return

        new_value = current_value[:-1]
        if not new_value:
            new_value = "0"
        self.output_string.set(new_value)
