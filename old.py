import tkinter
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Численное дифференцирование')
window.geometry('400x200')
tkinter.Text(window, font="Calibri 20", bg="Black")

a = DoubleVar()
aLabel = Label(
    text='Введите нижний предел'
)
aLabel.pack()

aEnter = Entry(
    textvariable=a
)
aEnter.pack()

b = DoubleVar()
bLabel = Label(
    text='Введите верхний предел'
)
bLabel.pack()

bEnter = Entry(
    textvariable=b, )
bEnter.pack()

chooseLabel = Label(
    text='Выберите метод'
)
chooseLabel.pack()

chosenMethod = StringVar()
methods = ('Метод прямоугольника', 'Метод трапеции', 'Метод Симпсона')
methodsChoose = ttk.Combobox(
    window, textvariable=chosenMethod, width=17
)
methodsChoose['values'] = methods
methodsChoose.pack()

answer = DoubleVar()


def diff():
    a1 = float(aEnter.get())
    b1 = float(bEnter.get())
    dx = (b1-a1)/10000
    if methodsChoose.get() == 'Метод прямоугольника':
        y = 0
        x = a1
        while x < b1:
            y = y + x*2
            x = x+dx
        y = y*dx
        answer.set(y)
        #answer.set((((a1 + b1) / 2) ** 2) * (b1 - a1))
    elif methodsChoose.get() == 'Метод трапеции':
        y = 0
        x = a1 + dx
        while x < b1:
            y = y+(x**2)
            x = x + dx
        y = (y+(((a1**2)+(b1**2))/2))*dx
        answer.set(y)
        #answer.set((((a1 ** 2) + (b1 ** 2)) / 2) * (b1 - a1))
    elif methodsChoose.get() == 'Метод Симпсона':
        y1 = 0
        x = a1 + dx
        while x < (b1-dx):
            y1 = y1 + (x**2)
            x = x + 2*dx
        y2 = 0
        x = a1 + (2 * dx)
        while x < (b1 - (2*dx)):
            y2 = y2 + (x**2)
            x = x + (2*dx)
        y = ((b1-a1)/(30000)) * ((a1**2) + (b1**2) + (4 * y1) + (2*y2))
        answer.set(y)

        #local = ((a1 ** 2) + (4 * (((a1 + b1) / 2) ** 2)) + (b1 ** 2))
        #answer.set(((b1 - a1) * local) * (1 / 6))


enterButton = Button(
    text='Рассчитать',
    command=diff,
    width=17
)
enterButton.pack()

answerLabel = Entry(
    textvariable=answer,
    state=tkinter.DISABLED
)
answerLabel.pack()

if __name__ == '__main__':
    window.mainloop()
