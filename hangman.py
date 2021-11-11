from tkinter import *
import random
from words import words
from tkinter import messagebox
#import PIL
#from PIL import Image
#from PIL import ImageTk

root = Tk()
root.minsize(500, 200)
root.configure(bg="black")
w = Label(root, text='Welcome to Hangman Game!! \n You have 8 chances to guess the word ',bg="black",  fg = "white", font=('Piazolla', 15), width='0', height="0")
w.grid(row=0, column=0, columnspan=10)
root.title("Hangman Game")
e = Entry(root, width=100, borderwidth=4)
e.insert(0, "USED LETTERS: ")
e.grid(row=5, column=0, columnspan=10, padx=10, pady=10)

lives = []
win_count = []
final_word = []

my_img = [PhotoImage(file = "h1.png"), PhotoImage(file = "h2.png"), PhotoImage(file = 'h3.png'), PhotoImage(file = 'h4.png'), PhotoImage(file = 'h5.png'), PhotoImage(file ='h6.png'), PhotoImage(file = 'h7.png'), PhotoImage(file = 'h8.png')]

word = random.choice(words)
for j in word:
    final_word.append(j)

button_a = Button(root, text='a',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('a', win_count, lives))
button_b = Button(root, text='b',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('b', win_count, lives))
button_c = Button(root, text='c',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('c', win_count, lives))
button_d = Button(root, text='d',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('d', win_count, lives))
button_e = Button(root, text='e',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('e', win_count, lives))
button_f = Button(root, text='f',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('f', win_count, lives))
button_g = Button(root, text='g',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('g', win_count, lives))
button_h = Button(root, text='h',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('h', win_count, lives))
button_i = Button(root, text='i',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('i', win_count, lives))
button_j = Button(root, text='j',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('j', win_count, lives))
button_k = Button(root, text='k',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('k', win_count, lives))
button_l = Button(root, text='l',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('l', win_count, lives))
button_m = Button(root, text='m',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('m', win_count, lives))
button_n = Button(root, text='n',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('n', win_count, lives))
button_o = Button(root, text='o',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('o', win_count, lives))
button_p = Button(root, text='p',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('p', win_count, lives))
button_q = Button(root, text='q',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('q', win_count, lives))
button_r = Button(root, text='r',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('r', win_count, lives))
button_s = Button(root, text='s',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('s', win_count, lives))
button_t = Button(root, text='t',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('t', win_count, lives))
button_u = Button(root, text='u',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('u', win_count, lives))
button_v = Button(root, text='v',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('v', win_count, lives))
button_w = Button(root, text='w',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('w', win_count, lives))
button_x = Button(root, text='x',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('x', win_count, lives))
button_y = Button(root, text='y',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('y', win_count, lives))
button_z = Button(root, text='z',font= ('mambo',15), padx=10, pady=10, bg="#F1C40F",border = 5, command=lambda: button_click('z', win_count, lives))

button_a.grid(row=2, column=1)
button_b.grid(row=2, column=2)
button_c.grid(row=2, column=3)
button_d.grid(row=2, column=4)
button_e.grid(row=2, column=5)
button_f.grid(row=2, column=6)
button_g.grid(row=2, column=7)
button_h.grid(row=2, column=8)
button_i.grid(row=2, column=9)
button_j.grid(row=2, column=10)
button_k.grid(row=3, column=2)
button_l.grid(row=3, column=3)
button_m.grid(row=3, column=4)
button_n.grid(row=3, column=5)
button_o.grid(row=3, column=6)
button_p.grid(row=3, column=7)
button_q.grid(row=3, column=8)
button_r.grid(row=3, column=9)
button_s.grid(row=4, column=2)
button_t.grid(row=4, column=3)
button_u.grid(row=4, column=4)
button_v.grid(row=4, column=5)
button_w.grid(row=4, column=6)
button_x.grid(row=4, column=7)
button_y.grid(row=4, column=8)
button_z.grid(row=4, column=9)


a = len(word)
for i in range(a):
    s = Label(root, text=" _ ", bg="black", fg="#abd4ef", font=("arial", 18))
    s.grid(row=8, column=i)


def button_click(letter, win_count, lives):
    current = e.get()
    e.insert(18, '  ' + letter)
    flag1 = []

    if len(lives) < 8:
        for i in range(len(word)):
            if letter == final_word[i]:
                u = Label(root, text=letter, font=('arial', 18))
                u.grid(row=6, column=i)
                win_count.append(1)
            else:
                flag1.append(1)
        if len(flag1) == len(word):
            lives.append(1)
            my_lable  = Label(root, bg="black")
            my_lable.grid(row = 1, column = 50, rowspan = 3)
            my_lable.config(image = my_img[len(lives)-1])

    if len(lives) == 8:
        pop = messagebox.showinfo(title='result', message='You Lost :(  \n Word was ' + word)
        root.destroy()

    if len(win_count) == len(word):
        answer = messagebox.showinfo(title='result', message='Yeah!! You WON!!')
        root.destroy()


root.mainloop()