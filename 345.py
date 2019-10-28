from tkinter import *
window = Tk()

window.title("J\'aime les fruits !")
window.geometry('800x600')

menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label = 'File', menu=filemenu)
filemenu.add_command(label='Exit the smoothie', command=window.destroy)

canvas = Canvas(window, width=800, height=15, bg="antiquewhite")
canvas.pack()
canvas.grid(row=2, column=0)

entry_label = Label(window, text='Which fruit(s) do I put in my smoothie today ?', font=(None, 15), fg='red')
entry_label.grid(row=1, column=0, sticky=N)

def onefruit_function():
    straw_label = Label(window, text='Strawberry !', bg='white', fg='red')
    straw_label.grid(row=6, column=0, sticky=N)
    img = PhotoImage(file='image.png')
    panel = Label(window, image = img)
    panel.grid(row= 5, column = 0)
    mainloop()

def twofruit_function():
    twofruits_label = Label(window, text='Banana and Cranberries !', bg='white', fg='red')
    twofruits_label.grid(row=7, column=0, sticky=N)
    imgb = PhotoImage(file='banana.png')
    panel = Label(window, image = imgb)
    panel.grid(row= 5, column = 0)
    imgc = PhotoImage(file='cranberry.png')
    panel = Label(window, image = imgc)
    panel.grid(row= 6, column = 0)
    mainloop()

straw = Button(window, text='Only 1 fruit', width=12, command=onefruit_function)
straw.grid(row=3, column=0, columnspan=2, sticky=S)

twofruits = Button(window, text='More !', width=12, command=twofruit_function)
twofruits.grid(row=4, column=0, columnspan=2, sticky=S)

window.mainloop()
