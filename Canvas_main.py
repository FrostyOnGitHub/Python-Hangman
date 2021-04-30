from tkinter import *
tk=Tk()
tk.geometry('1794x700')
tk.configure(bg="deep sky blue")
tk.title("Jeu du Pendu")
Canvas=Canvas(tk, bg="deep sky blue", width=1794, height=700)
tk.resizable(False, False)
Canvas.place(x=0,y=0)
letters=[]
message1 = Label( tk, text="Bienvenue au jeu du Pendu!", font='Times 50 bold', bg='deep sky blue', fg='black')
message1.place(anchor='n', relx=0.5, rely=0.1, relwidth=0.8, relheight=0.180)

message2 = Label( tk, text="Pour commencer appuyez sur JOUER", font='Times 20 bold', bg='deep sky blue', fg='black')
message2.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.8, relheight=0.355)



def regles():
    message3 = Label( tk, text="Votre but est de trouver le mot mystere avant que le dessin du pendu soit finit.", font='Times 50 bold', bg='deep sky blue', fg='black')
    message3.place(anchor='n', relx=0.5, rely=0.1, relwidth=0.8, relheight=0.180)
    message4 = Label( tk, text="Vous pouvez appuyez sur les lettres ainsi que les touches sur votre clavier pour jouer. Bonne chance!", font='Times 20 bold', bg='deep sky blue', fg='black')
    message4.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.8, relheight=0.355)
    button3= Button(tk, text="Retour", font='Times 10 bold', bg='white', fg='black', height=1, width=1, command = jouer)
    button3=place(anchor='n', relx=0.3, rely=0.6, relwidth=0.4, relheight=0.2)
    
def check():
    if checking = 1:
        
def setup():
    for i in range(26):
        letters.append(chr(97+i))
        
        
def jouer():
    
    Canvas=Canvas(tk, bg="deep sky blue", width=1780, height=470)
    tk.configure(bg="deep sky blue")
    Canvas.place(x=0,y=0)


    button1 = Button(tk, text="A", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.050, rely=0.68, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="B", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.150, rely=0.68, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="C", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.247, rely=0.68, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="D", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.345, rely=0.68, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="E", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.443, rely=0.68, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="F", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.540, rely=0.68, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="G", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.638, rely=0.68, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="H", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.736, rely=0.68, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="I", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.833, rely=0.68, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="J", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.930, rely=0.68, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="K", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.050, rely=0.78, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="L", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.150, rely=0.78, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="M", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.247, rely=0.78, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="N", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.345, rely=0.78, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="O", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.443, rely=0.78, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="P", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.540, rely=0.78, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="Q", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.638, rely=0.78, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="R", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.736, rely=0.78, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="S", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.833, rely=0.78, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="T", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.930, rely=0.78, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="U", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.247, rely=0.88, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="V", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.345, rely=0.88, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="W", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.443, rely=0.88, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="X", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.540, rely=0.88, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="Y", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.638, rely=0.88, relwidth=0.1, relheight=0.1)

    button1 = Button(tk, text="Z", font='Times 20 bold', bg='black', fg='white', height=1, width=1)
    button1.place(anchor='n', relx=0.736, rely=0.88, relwidth=0.1, relheight=0.1)

            
button1 = Button(tk, text="JOUER", font='Times 20 bold', bg='spring green', fg='black', activebackground= "green" height=1, width=1, command = jouer)
button1.place(anchor='n', relx=0.3, rely=0.6, relwidth=0.4, relheight=0.2)

button2 = Button(tk, text="RÈGLES DU JEU", font='Times 20 bold', bg='firebrick1', fg='black', activebackground="red", height=1, width=1, command=regles)
button2.place(anchor='n', relx=0.7, rely=0.6, relwidth=0.4, relheight=0.2)

Canvas.update()
