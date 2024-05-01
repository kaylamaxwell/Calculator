from gui import *


def main():
    root = Tk()
    root.geometry("400x400")
    root.title("Calculator")
    root.resizable(False, False)
    calculator_gui = GUI(root)
    for i in range(4):
        Grid.columnconfigure(root, i, weight=1)
        Grid.rowconfigure(root, i, weight=1)
    Grid.rowconfigure(root, 4, weight=1)
    root.mainloop()


if __name__ == "__main__":
    main()
