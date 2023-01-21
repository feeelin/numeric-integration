import tkinter as tk
from tkinter import *
from tkinter import ttk


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.a = DoubleVar()
        self.b = DoubleVar()
        self.chosenMethod = StringVar()
        self.methods = ('Метод прямоугольника', 'Метод трапеции', 'Метод Симпсона')
        self.answer = DoubleVar()

        self.title('Численное дифференцирование')

        self.aLabel = Label(text='Введите нижний предел')
        self.aEnter = Entry(textvariable=self.a)
        self.bLabel = Label(text='Введите верхний предел')
        self.bEnter = Entry(textvariable=self.b)
        self.chooseLabel = Label(text='Выберите метод')

        self.enterButton = Button(text='Рассчитать', command=self.integrate, width=17)

        self.answerLabel = Entry(textvariable=self.answer, state=tk.DISABLED)

        self.methodsChoose = ttk.Combobox(self, textvariable=self.chosenMethod, width=17)
        self.methodsChoose['values'] = self.methods

        self.aLabel.pack(padx=100, pady=5)
        self.aEnter.pack(padx=100, pady=5)
        self.bLabel.pack(padx=100, pady=5)
        self.bEnter.pack(padx=100, pady=5)
        self.chooseLabel.pack(padx=100, pady=5)
        self.methodsChoose.pack(padx=100, pady=5)
        self.enterButton.pack(padx=100, pady=5)
        self.answerLabel.pack(padx=100, pady=5)

    def integrate(self):
        a1 = float(self.a.get())
        b1 = float(self.b.get())
        dx = (b1 - a1) / 10000

        if self.chosenMethod.get() == 'Метод прямоугольника':
            y = 0
            x = a1
            while x < b1:
                y = y + x * 2
                x = x + dx
            y = y * dx
            self.answer.set(y)

        elif self.chosenMethod.get() == 'Метод трапеции':
            y = 0
            x = a1 + dx
            while x < b1:
                y = y + (x ** 2)
                x = x + dx
            y = (y + (((a1 ** 2) + (b1 ** 2)) / 2)) * dx
            self.answer.set(y)

        elif self.chosenMethod.get() == 'Метод Симпсона':
            y1 = 0
            x = a1 + dx
            while x < (b1 - dx):
                y1 = y1 + (x ** 2)
                x = x + 2 * dx
            y2 = 0
            x = a1 + (2 * dx)
            while x < (b1 - (2 * dx)):
                y2 = y2 + (x ** 2)
                x = x + (2 * dx)
            y = ((b1 - a1) / 30000) * ((a1 ** 2) + (b1 ** 2) + (4 * y1) + (2 * y2))
            self.answer.set(y)


if __name__ == '__main__':
    window = MainWindow()
    window.mainloop()
