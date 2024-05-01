from gui import *


def main():
    root = Tk()
    root.geometry("500x500")
    root.title("Calculator")
    root.resizable(False, False)
    calculator_gui = GUI(root)
    for i in range(6):
        Grid.columnconfigure(root, i, weight=1)
        Grid.rowconfigure(root, i, weight=1)
    Grid.rowconfigure(root, 6, weight=1)
    root.mainloop()


if __name__ == "__main__":
    main()
