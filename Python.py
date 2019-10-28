from tkinter import *

window = Tk()

def exit_function():
    pass

window.title('Hello World')
window.geometry('500x500')

entry_label = Label(window, text='Label', bg='black', fg='white')
entry_label.grid(row=1, column=0, sticky=N)

textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky=S)

exit = Button(window, text='Exit', width=6, command=exit_function())
exit.grid(row=3, column=0, sticky=S)

window.mainloop()

#text_file = open('animals.txt', 'r')
#text_file = open('animals.txt', 'a')
#text_file.write('Hello there')
#lines = text_file.read()
#print(lines)
#text_file.close()