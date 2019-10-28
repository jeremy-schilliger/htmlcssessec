from tkinter import *
import Pong
from tkinter import *
import random
import time
window = Tk()

sub = " "

def submit_function():
    if sub == 'Yes':
        pong_function()
    else:
        print("Maybe next time..")

def pong_function():   

    # Define ball properties and functions
    class Ball:
        def __init__(self, canvas, color, size, paddle):
            self.canvas = canvas
            self.paddle = paddle
            self.id = canvas.create_oval(10, 10, size, size, fill=color)
            self.canvas.move(self.id, 245, 100)
            self.xspeed = random.randrange(-3,3)
            self.yspeed = -1
            self.hit_bottom = False
            self.score = 0

        def draw(self):
            self.canvas.move(self.id, self.xspeed, self.yspeed)
            pos = self.canvas.coords(self.id)
            if pos[1] <= 0:
                self.yspeed = 3
            if pos[3] >= 400:
                self.hit_bottom = True
            if pos[0] <= 0:
                self.xspeed = 3
            if pos[2] >= 500:
                self.xspeed = -3
            if self.hit_paddle(pos) == True:
                self.yspeed = -3
                self.xspeed = random.randrange(-3,3)
                self.score += 1

        def hit_paddle(self, pos):
            paddle_pos = self.canvas.coords(self.paddle.id)
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                    return True
            return False

    # Define paddle properties and functions
    class Paddle:
        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_rectangle(0,0, 100, 10, fill=color)
            self.canvas.move(self.id, 200, 300)
            self.xspeed = 0
            self.canvas.bind_all('<KeyPress-Left>', self.move_left)
            self.canvas.bind_all('<KeyPress-Right>', self.move_right)

        def draw(self):
            self.canvas.move(self.id, self.xspeed, 0)
            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.xspeed = 0
            if pos[2] >= 500:
                self.xspeed = 0

        def move_left(self, evt):
            self.xspeed = -2
        def move_right(self, evt):
            self.xspeed = 2

    # Create window and canvas to draw on
    tk = Tk()
    tk.title("Ball Game")
    canvas = Canvas(tk, width=500, height=400, bd=0, bg='papaya whip')
    canvas.pack()
    label = canvas.create_text(5, 5, anchor=NW, text="Score: 0")
    tk.update()
    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, 'red', 25, paddle)

    # Animation loop
    while ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        canvas.itemconfig(label, text="Score: "+str(ball.score))
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

    # Game Over
    go_label = canvas.create_text(250,200,text="GAME OVER",font=("Helvetica",30))
    tk.update()


window.title('WANT TO PLAY A LITTLE GAME ?')
window.geometry('700x700')

entry_label = Label(window, text='Do you want to play a game of pong? (One player)', font=(None, 15), fg='blue', height=2)
entry_label.grid(row=0, column=0, sticky=N)

textentry = Entry(window, width=20, text='Yes / No', bg='white')
textentry.grid(row=2, column=0, sticky=N)

answer = '-'
answer = Label(window, text=answer, fg='black')
answer.grid(row=3, column=0, sticky=S)

submit = Button(window, text='PLAY', width=9, command=pong_function)
submit.grid(row=6, column=0, columnspan=2, sticky=S)

img = PhotoImage(file="D:\Perso\School\ESSEC S3\Python\PingPong\ping.png")
panel = Label(window, image = img)
panel.grid(row=7, column=0, sticky=S)

answer = 'Commands :     Use the arrows to move. Don\'t let the ball fall !'
answer = Label(window, text=answer, fg='black')
answer.grid(row=9, column=0, sticky=S)



menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label = 'File', menu=filemenu)
filemenu.add_command(label='Exit', command=window.destroy)

### SEARCH : arc / image / line / polygon

window.mainloop()