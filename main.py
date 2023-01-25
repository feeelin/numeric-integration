import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.function = ''
        self.f = StringVar()
        self.functionLabel = Label(text='Enter the function in Python format')
        self.functionEnter = Entry(textvariable=self.f)
        self.functionButton = Button(command=self.update, text='Upload function')

        self.functionLabel.pack(pady=5)
        self.functionEnter.pack(padx=100, pady=5)
        self.functionButton.pack(pady=5)

        self.a = DoubleVar()
        self.b = DoubleVar()
        self.chosenMethod = StringVar()
        self.methods = ('Rectangle method', 'Trapezoid method', "Simpson's method")
        self.answer = DoubleVar()

        self.title('Numeric integration')
        self.aLabel = Label(text='Enter a lower border')
        self.aEnter = Entry(textvariable=self.a)
        self.bLabel = Label(text='Enter a upper border')
        self.bEnter = Entry(textvariable=self.b)
        self.chooseLabel = Label(text='Chose a method')
        self.enterButton = Button(text='Calculate', command=self.integrate, width=17)
        self.answerLabel = Entry(textvariable=self.answer, state=tk.DISABLED)
        self.methodsChoose = ttk.Combobox(self, textvariable=self.chosenMethod, width=17)
        self.methodsChoose['values'] = self.methods

        self.plotButton = Button(text='Graph', command=self.plot)

        self.aLabel.pack(padx=100, pady=5)
        self.aEnter.pack(padx=100, pady=5)
        self.bLabel.pack(padx=100, pady=5)
        self.bEnter.pack(padx=100, pady=5)
        self.chooseLabel.pack(padx=100, pady=5)
        self.methodsChoose.pack(padx=100, pady=5)
        self.enterButton.pack(padx=100, pady=5)
        self.answerLabel.pack(padx=100, pady=5)
        self.plotButton.pack(pady=5)

    def integrate(self):
        a1 = float(self.a.get())
        b1 = float(self.b.get())
        dx = (b1 - a1) / 10000

        if self.chosenMethod.get() == 'Rectangle method':
            y = 0
            x = a1
            while x < b1:
                y = y + eval(self.function.format(x))
                x = x + dx
            y = y * dx
            self.answer.set(y)

        elif self.chosenMethod.get() == 'Trapezoid method':
            y = 0
            x = a1 + dx
            while x < b1:
                y = y + (x ** 2)
                x = x + dx
            y = (y + (((eval(self.function.format(a1))) + (eval(self.function.format(a1)))) / 2)) * dx
            self.answer.set(y)

        elif self.chosenMethod.get() == "Simpson's method":
            y1 = 0
            x = a1 + dx
            while x < (b1 - dx):
                y1 = y1 + eval(self.function.format(x))
                x = x + 2 * dx
            y2 = 0
            x = a1 + (2 * dx)
            while x < (b1 - (2 * dx)):
                y2 = y2 + eval(self.function.format(x))
                x = x + (2 * dx)
            y = ((b1 - a1) / 30000) * (eval(self.function.format(a1)) + eval(self.function.format(a1)) + (4 * y1) +
                                       (2 * y2))
            self.answer.set(y)

    def plot(self):
        x_arr = []
        y_arr = []

        start = float(self.a.get())
        stop = float(self.b.get())

        while start <= stop:
            x_arr.append(start)
            y_arr.append(eval(self.function.format(start)))
            start += 0.1

        plt.subplots(num=f"Graph of the function {self.f.get()}")
        plt.plot(x_arr, y_arr)
        plt.title(f"Graph of the function {self.f.get()} in the interval from {self.a.get()} to {self.b.get()}")
        plt.ylabel('X')
        plt.xlabel('Y')
        plt.show()

    def update(self):
        self.function = ''
        f_arr = list(self.f.get())

        for i in f_arr:
            if i == 'x':
                self.function += '{}'
            elif i == ' ' or i == 'y' or i == '=':
                continue
            else:
                self.function += i

        self.plotButton.pack(pady=5)


if __name__ == '__main__':
    window = MainWindow()
    window.mainloop()
