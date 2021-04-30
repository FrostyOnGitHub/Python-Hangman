from tkinter import *
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



def regles():
    message3 = Label( tk, text="Votre but est de trouver le mot mystere avant que le dessin du pendu soit finit.", font='Times 50 bold', bg='deep sky blue', fg='black')
    message3.place(anchor='n', relx=0.5, rely=0.1, relwidth=0.8, relheight=0.180)
    message4 = Label( tk, text="Vous pouvez appuyez sur les lettres ainsi que les touches sur votre clavier pour jouer. Bonne chance!", font='Times 20 bold', bg='deep sky blue', fg='black')
    message4.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.8, relheight=0.355)
    button3= Button(tk, text="Retour", font='Times 10 bold', bg='white', fg='black', height=1, width=1, command = jouer)
    button3=place(anchor='n', relx=0.3, rely=0.6, relwidth=0.4, relheight=0.2)
    
def jouer():
    
    Canvas=Canvas(tk, bg="white", width=1794, height=300)
    Canvas.place(x=0,y=400)
    line = Canvas.create_line(0,150,1794,150)
    line = Canvas.create_line(138,300,138,0)
    line = Canvas.create_line(2*138,300,2*138,0)
    line = Canvas.create_line(3*138,300,3*138,0)
    line = Canvas.create_line(4*138,300,4*138,0)
    line = Canvas.create_line(5*138,300,5*138,0)
    line = Canvas.create_line(6*138,300,6*138,0)
    line = Canvas.create_line(7*138,300,7*138,0)
    line = Canvas.create_line(8*138,300,8*138,0)
    line = Canvas.create_line(9*138,300,9*138,0)
    line = Canvas.create_line(10*138,300,10*138,0)
    line = Canvas.create_line(11*138,300,11*138,0)
    line = Canvas.create_line(12*138,300,12*138,0)
    line = Canvas.create_line(13*138,300,13*138,0)
    #on crée le tableau de tableau auquel on assigne un 0 partout (pour l'ordinateur 0= case vide)
    board=[]
    for i in range(2):
        board.append([])
        for j in range(13):
          board[i].append(0)
          
    def afficher():
        for i in range(2):
            for j in range(13):
                if(board[j][i] == 1):
                    croix(i,j)
                elif(board[j][i] == 2):
                    cercle(i,j)

    def croix(i,j):
        line2 = Canvas.create_line(i*138,j*138,(i+1)*138,(j+1)*138,width=2,fill="red",tag="croix")
        line3 = Canvas.create_line(i*138,j*138,(i)*138,(j+1)*138,(i+1)*138,j*138,width=2,fill="red",tag="croix")
        
        def cercle(i,j):
            circle = Canvas.create_oval(i*138,j*138,(i+1)*138,(j+1)*138,width=2,tag="cercle")
            
button1 = Button(tk, text="JOUER", font='Times 20 bold', bg='spring green', fg='black', height=1, width=1, command = jouer)
button1.place(anchor='n', relx=0.3, rely=0.6, relwidth=0.4, relheight=0.2)

button2 = Button(tk, text="RÈGLES DU JEU", font='Times 20 bold', bg='firebrick1', fg='black', height=1, width=1, command=regles)
button2.place(anchor='n', relx=0.7, rely=0.6, relwidth=0.4, relheight=0.2)

Canvas.update()
tk.mainloop()
