from Tkinter import *
tk=Tk()
tk.geometry('1794x700')
tk.title("Jeu du Pendu")
Canvas=Canvas(tk, bg="deep sky blue", width=1794, height=700)
tk.resizable(False, False)
Canvas.place(x=0,y=0)

message1 = Label( tk, text="Bienvenue au jeu du Pendu!", font='Times 50 bold', bg='deep sky blue', fg='black')
message1.place(anchor='n', relx=0.5, rely=0.1, relwidth=0.8, relheight=0.180)

message2 = Label( tk, text="Pour commencer appuyez sur JOUER", font='Times 20 bold', bg='deep sky blue', fg='black')
message2.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.8, relheight=0.355)

button1 = Button(tk, text="JOUER", font='Times 10 bold', bg='spring green', fg='white', height=1, width=1)
button1.place(anchor='n', relx=0.3, rely=0.6, relwidth=0.8, relheight=0.355)

button2 = Button(tk, text="RÈGLES DU JEU", font='Times 10 bold', bg='firebrick1', fg='white', height=1, width=1)
button2.place(anchor='n', relx=0.6, rely=0.6, relwidth=0.8, relheight=0.355)
