fiveLetterWords= []
f = open("germinal.txt",'r') 
ligne = f.readline()
while ligne!='':
    ligne = ligne.replace(',','')
    ligne = ligne.replace('.','')
    ligne = ligne.replace(';','')
    ligne = ligne.replace(':','')
    ligne = ligne.replace("'",' ') 
    ligne = ligne.replace('  ',' ')
    ligne = ligne.replace('\n','')
    t=ligne.split(' ') 
    ligne = f.readline()
    
    for word in t:
        if len(word) > 4:
            isgood= True
            for s in word:
                if not (97<= ord(s) and ord(s)<= 97+26):
                    isgood= False
            if isgood:
                fiveLetterWords.append(word)
print(fiveLetterWords)


from tkinter import *
import random as r
import tkinter.messagebox
tk=Tk()
tk.geometry('1794x700')
tk.configure(bg="deep sky blue")
tk.title("Jeu du Pendu")
Canvas=Canvas(tk, bg="deep sky blue", width=1794, height=700)
tk.resizable(False, False)
letters=[]
game_phase=[0]


    
    
def setup():
    for i in range(26):
        letters.append(chr(97+i))
        
def addLetter(guess) :
    
    for i in range(len(letters)) :
        if letters[i] == guess :
            placed = 0
            for j in range(len(toGuess)):
                if guess == toGuess[j] :
                    word[j] = guess
                    placed += 1
                    
            letters.remove(i)
            
            if placed != 0 :
                break
            else :
                lives -= 1
                

    

def phase1():
    game_phase[0]=0
    Canvas.place(x=0,y=0)
    
    message1.place(anchor='n', relx=0.5, rely=0.1, relwidth=0.8, relheight=0.180)

    
    message2.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.8, relheight=0.355)
    
     
    button1.place(anchor='n', relx=0.3, rely=0.6, relwidth=0.4, relheight=0.2)

   
    button2.place(anchor='n', relx=0.7, rely=0.6, relwidth=0.4, relheight=0.2)
   

def phase1_end() :
    message1.destroy()
    message2.destroy()
    #button1.destroy()
    button2.destroy()
    

    
def phase2():

    game_phase[0]=1
   
    message3.place(anchor='n', relx=0.5, rely=0.1, relwidth=0.8, relheight=0.180)
   
    message4.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.8, relheight=0.355)
    
    button1.place(anchor='n', relx=0.5, rely=0.6, relwidth=0.8, relheight=0.2)
    
    #phase2_effacer()
    
    
     
def phase3():
    game_phase[0]=2
    Canvas=Canvas(tk, bg="deep sky blue", width=1780, height=470)
    tk.configure(bg="deep sky blue")
    Canvas.place(x=0,y=0)
    
button1 = Button(tk, text="JOUER", font='Times 20 bold', bg='green', fg='black', activebackground= "green" ,height=1, width=1, command=phase3)
button2 = Button(tk, text="RÈGLES DU JEU", font='Times 20 bold', bg='firebrick1', fg='black', activebackground="red", height=1, width=1, command= lambda : [phase1_end(), phase2()])
message1 = Label( tk, text="Bienvenue au jeu du Pendu!", font='Times 50 bold', bg='deep sky blue', fg='black')
message2 = Label( tk, text="Pour commencer appuyez sur JOUER", font='Times 20 bold', bg='deep sky blue', fg='black')
message3 = Label( tk, text="Votre but est de trouver le mot mystere avant que le dessin du pendu soit finit.", font='Times 30 bold', bg='deep sky blue', fg='black')
message4 = Label( tk, text="Vous pouvez appuyez sur les lettres ainsi que les touches sur votre clavier pour jouer. Bonne chance!", font='Times 20 bold', bg='deep sky blue', fg='black')
#button3= Button(tk, text="Retour", font='Times 10 bold', bg='white', fg='black', height=1, width=1, command = lambda : [phase2_end(), phase1()] )
#button3= Button(tk, text="Play", font='Times 10 bold', bg='white', fg='black', height=1, width=1, command = phase3)
