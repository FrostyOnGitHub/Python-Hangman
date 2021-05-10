from tkinter import *
import random as r
import tkinter.messagebox
from functools import partial

tk=Tk()
tk.geometry('1794x700')
tk.configure(bg="deep sky blue")
tk.title("Jeu du Pendu")
Canvas=Canvas(tk, bg="deep sky blue", width=1794, height=700)
tk.resizable(False, False)

#---------------Définition des variables---------------
game_phase=[0]
radius = 30
count=0
buttons=[]
word=[ ]
letters=[ ]
Ai_status=False
alreadytried=[ ]
buttonx=[0.050,0.150,0.247,0.345,0.443,0.540,0.638,0.736,0.833,0.930,0.050,0.150,0.247,0.345,0.443,0.540,0.638,0.736,0.833,0.930,0.247,0.345,0.443,0.540,0.638,0.736]
buttony=[0.68,0.68,0.68,0.68,0.68,0.68,0.68,0.68,0.68,0.68,0.78,0.78,0.78,0.78,0.78,0.78,0.78,0.78,0.78,0.78,0.88,0.88,0.88,0.88,0.88,0.88]
tk.title("Jeu de Pendu")
toguess=""
keyword_array=[]
score='0'

alreadytriedBad = []

germial = open("germinal.txt",'r')
word_AI = open("word_AI.txt", 'r')
prev_scores = open("scores.txt", 'r')
hs = 0
AI_W_DB = []


print()
prev_scores = open("scores.txt", 'r')
hs = prev_scores.readline()
prev_scores.close()

prev_scores = open("scores.txt", 'w')
prev_scores.write(hs)

prev_scores.close()

#---------------Création d'une liste basée sur un livre---------------
def process_data(isAI):
    fiveLetterWords= []
    if not isAI :
        f = open("germinal.txt",'r')
    else :
        f = open("word_AI.txt", 'r') 
    
    ligne = f.readline()
    
    while ligne!='':
        ligne = ligne.replace(',','')
        ligne = ligne.replace('.','')
        ligne = ligne.replace(';','')
        ligne = ligne.replace(':','')
        ligne = ligne.replace("'",' ') 
        ligne = ligne.replace('  ',' ')
        ligne = ligne.replace('\n','')
        if (not isAI) :
            t=ligne.split(' ')
        else :
            t=[ligne]
        ligne = f.readline()
        
        for word in t:
            if len(word) > 4:
                    isgood= True
                    for s in word:
                        if not (97<= ord(s) and ord(s)<= 97+26):
                            isgood= False
                    if isgood:
                        fiveLetterWords.append(word)
    return fiveLetterWords
    

        
#---------------Remplir une liste avec toutes les lettres de l'alphabet et une autre liste avec tous les mots et choisir l'un de ces mots---------------
def setup():
    global wordlist, letters, toguess, word, AI_W_DB, hs
    for i in range(26):
        letters.append(chr(97+i))
    wordlist=process_data(False)
    print("lengermial", len(wordlist))
    AI_W_DB = process_data(True)
    print("lenAI", len(AI_W_DB))
    
    toguess=wordlist[r.randint(0,len(wordlist)-1)]
    for i in range(len(toguess)):
        word.append("")
        print(toguess[i], end="")
        

        
        



#---------------Fonction logique principale qui tient compte des lettres utilisées / mauvaises lettres / lettres devinées---------------
def addLetter(guess, isAI) :
    global letters , alreadytried, buttons, score, hs, prev_score
   
    for i in range(len(letters)) :
        placed = 0
        if letters[i] == guess :
            letters.remove(guess)
            for j in range(len(toguess)):
                if guess == toguess[j] :
                    word[j] = guess
                    placed += 1
            
            if placed != 0 :
                buttons[ord(guess)-97].config(bg="green")

                

                break
            else :
                alreadytriedBad.append(guess)
                boom()
                buttons[ord(guess)-97].config(bg="red")
                break
        else :
            isin = False
            for x in range(len(alreadytried)):
                
                if alreadytried[x] == guess:
                    isin=True
                    tkinter.messagebox.showinfo("Hangman", "Lettre déja utilisée!")
                    break
            if isin:
                break
            
    middle = 850
    for i in range(len(word)) :
        Canvas.create_text(middle - 60*len(toguess)//2 + 60*i + 20, 315,fill="darkblue",font="Times 30 bold",text=word[i],tag="text" )

    alreadytried.append(guess)
    if not isAI :
        check_win()
        check_loss()
    
    
        
        
    
    prev_scores = open("scores.txt", 'r')

    
    hs = prev_scores.readline()

    prev_scores.close()
    prev_scores = open("scores.txt", 'w')
    if (int(score) > int(hs)) :
        prev_scores.write(score)
        labelHS.config(text = "Record : "+ score)
        labelHS.place(anchor='n', relx=0.890, rely=0.15, relwidth=0.1, relheight=0.1)

    else :
        prev_scores.write(hs)
    prev_scores.close()
        
    


    
    
#---------------Fonction pour dessiner le pendu---------------    
def boom():
    global count
    count+=1
    
    if count >= 1:
        Canvas.create_line(200,50,200,70,tags="hang")
    if count >= 2:
        Canvas.create_oval(200-radius, 100-radius, 200+radius, 100+radius, tags="hang")
    if count >= 3:
        Canvas.create_line(200,150,100,100,tags="hang")
    if count >= 4:
        Canvas.create_line(200,150,300,100,tags="hang")
    if count >= 5:
        Canvas.create_line(200,130,200,250,tags="hang")
    if count >= 6:
        Canvas.create_line(200,250,100,300,tags="hang")
    if count >= 7:
        Canvas.create_line(200,250,300,300,tags="hang")

#---------------Configuration de la première page---------------
def phase1():
    game_phase[0]=0
    Canvas.place(x=0,y=0)
    
    message1.place(anchor='n', relx=0.5, rely=0.09, relwidth=0.8, relheight=0.180)

    
    message2.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.8, relheight=0.180)
    
     
    button1.place(anchor='n', relx=0.3, rely=0.55, relwidth=0.4, relheight=0.2)
    
    buttonAI.place(anchor='n', relx=0.5, rely=0.75, relwidth=0.4, relheight=0.2)
   
    button2.place(anchor='n', relx=0.7, rely=0.55, relwidth=0.4, relheight=0.2)
   
#---------------Supprimer des widgets de la première page---------------
def phase1_end() :
    message1.destroy()
    message2.destroy()
    button2.destroy()


#---------------Configuration de la deuxième page---------------
def phase2():

    game_phase[0]=1
   
    message3.place(anchor='n', relx=0.5, rely=0.07, relwidth=0.8, relheight=0.180)
   
    message4.place(anchor='n', relx=0.5, rely=0.30, relwidth=0.8, relheight=0.180)
    
    button1.place(anchor='n', relx=0.5, rely=0.55, relwidth=0.8, relheight=0.2)
    
    buttonAI.place(anchor='n', relx=0.5, rely=0.75, relwidth=0.8, relheight=0.2)
    


#---------------Suppression des éléments de la deuxième page---------------
def phase2_end() :
    message3.destroy()
    message4.destroy()
    button1.destroy()
    buttonAI.destroy()
 
#---------------Fonction pour lier(bind) les touches du clavier aux boutons de lettres---------------
def key_pressed(event) :
    if not Ai_status:
        key = event.char
        addLetter(key, False)
    





# ---------------Création des boutons pour chaque lettre---------------

for i in range(26) :
   v_ = chr(97+i)
   buttons.append(Button(tk, text=chr(65+i), font='Times 20 bold', bg='slate gray', fg='white',
                         height=1, width=1,command= partial(addLetter, guess = chr(97+i), isAI=False  ))) 


#---------------Vérifier si on a gagné---------------
def check_win():
    global word, togues, count, alreadytried, buttons, score
    isWin = True
    
    for i in range(len(toguess)) :
        if word[i] != toguess[i] :
            isWin = False
    if isWin == True:
          score = int(score)
          score+=1
          score = str(score)
          scorelabel.config(text="Score : " + score)  
        
          tkinter.messagebox.showinfo("Hangman", "Vous avez gagné! Cela vous à pris :" + str(len(alreadytriedBad)) + " coups !" )
          for i in range(len(buttons)):
             buttons[i]["state"]= DISABLED
 
 

        
             
             
             
             
             
             
#---------------Vérifier si on a perdu---------------            
def check_loss() :
    global count, scoring_possible, score
    if count >= 7 :
        score = 0
        text="Score : " + str(score)
        scorelabel.config(text=text)  

        tkinter.messagebox.showinfo("Hangman", "Vous avez perdu!" )
        for i in range(len(buttons)):
            buttons[i]["state"]= DISABLED
        
    

        
#---------------Fonction pour le bouton pour recommencer une partie---------------
def restart_game():
    global button3, count, buttons, word, letters, toguess, alreadytried,alreadytriedBad,keyword_array,score
    Canvas.delete("hang")
    Canvas.delete("text")
    Canvas.delete("oldline")
    for i in range(len(buttons)):
        buttons[i]["state"]= NORMAL
        
    count=0
    alreadytried=[]
    word = []
    for i in range(len(toguess)) :
        word.append("")

    letters=[ ]
    for i in range(26):
        letters.append(chr(97+i))
    alreadytriedBad=[]
    keyword_array=[]


#---------------Configuration de la page de jeu---------------
def phase3_setup() :
    global buttons, buttonx, buttony, score
    
    middle = 850
    for i in range(len(toguess)) :
        Canvas.create_line(middle - 60*len(toguess)//2 + 60*i, 341, middle - 60*len(toguess)//2 + 60*i + 50, 341, tag="oldline")
     
    scorelabel.place(anchor='n', relx=0.890, rely=0.07, relwidth=0.1, relheight=0.1)
    for i in range(len(buttons)):
        buttons[i].config(bg="slate gray")
        buttons[i].place(anchor='n', relx=buttonx[i], rely=buttony[i], relwidth=0.1, relheight=0.1)
    tk.bind('<Key>', key_pressed)
    tk.bind('<Return>', recommencer_)    

    
    
    button5 = Button(tk,text="Recommencer", font = "Times 15 bold", bg="SlateBlue2", fg="white", height=1, width=1, command= lambda :[restart_game(), setup(), phase3_setup()])
    button5.place(anchor='n', relx=0.890, rely=0.30, relwidth=0.1,relheight=0.1)
    labelHS.place(anchor='n', relx=0.890, rely=0.15, relwidth=0.1, relheight=0.1)
    
 #---------------Widgets de la page de jeu--------------- 
def phase3():
    global toguess, word
    game_phase[0]=2
    
    Canvas.place(x=0,y=0)

    Canvas.create_line(10,470-10,50,470-10)
    Canvas.create_line(30,470-10,30,50)
    Canvas.create_line(30,50,200,50)

    
def recommencer_(event) :
    restart_game()
    setup()
    phase3_setup()
    
    
#---------------Configuration de la page IA---------------    
def phaseAI():
     Ai_status=True
     game_phase[0]=3
     Canvas.place(x=0, y=0)
     Canvas.create_line(10,470-10,50,470-10)
     Canvas.create_line(30,470-10,30,50)
     Canvas.create_line(30,50,200,50)
  
 #---------------Obtenir le mot saisi par saisie utilisateur--------------- 
def AiWordPhase(keyword_array):
    global toguess
    keyword_array.append(keyword_list.get())
    
    if len(keyword_array[0]) >= 5:
        toguess=str(keyword_array[0])
        toguess = toguess.strip()
        middle = 850
        for i in range(len(toguess)) :
            Canvas.create_line(middle - 60*len(toguess)//2 + 60*i, 341, middle - 60*len(toguess)//2 + 60*i + 50, 341, tag="oldline")
        
        print(keyword_array)
    else :
        tkinter.messagebox.showinfo("Hangman", "Mot invalide, veuillez en choisir un autre (plus de 5 lettres)" )


        
 #---------------Poursuite de la configuration de la mécanique des pages IA---------------   
def phaseAI_setup():
    middle = 850
    for i in range(len(toguess)) :
        Canvas.create_line(middle - 60*len(toguess)//2 + 60*i, 341, middle - 60*len(toguess)//2 + 60*i + 50, 341, tag="oldline")
    
    AIentry.place(anchor='n', relx=0.450, rely=0.70, relwidth=0.3,relheight=0.2)
    
    AIentry.bind('<Return>', set_toguess(AIentry.get())) 
    print(set_toguess)
    
    buttonAI.destroy()
    button1.destroy()   
    message3.destroy()
    message4.destroy()
     
     
    button6 = Button(tk,text="Recommencer", font = "Times 15 bold", bg="SlateBlue2", fg="white", height=1, width=1, command= lambda :[setup(), phaseAI_setup(), restart_game(), ])
    button6.place(anchor='n', relx=0.890, rely=0.30, relwidth=0.1,relheight=0.1)
    button7= Button(tk,text="IA devine", font="Times 15 bold", bg="SlateBlue2", fg="white", height=1, width=1, command=lambda : [AI_Make_Guess()])
    button7.place(anchor='n', relx=0.890, rely=0.20, relwidth=0.1, relheight=0.1)
    
    labelAI.place(anchor="n", relx=0.800, rely=0.55, relwidth=0.50, relheight=0.50)    
    
    button8= Button(tk,text="Chosir ce mot", font="Times 15 bold", bg="SlateBlue2", fg="white", height=1, width=1, command= lambda : [AiWordPhase(keyword_array), restart_game(), phaseAI_setup()])
    button8.place(anchor='n', relx=0.890, rely=0.40, relwidth=0.1, relheight=0.1)
    
#---------------Widgets définis à partir de fonctions pour différentes pages---------------    
keyword_list=StringVar()
txtlabelHS = "Record : " + str(hs)
print("hs429", hs)
labelHS = Label(tk, text=txtlabelHS, font = "Times 20 bold", bg="deep sky blue", height=1, width=1)
txtscore = "Score : " + str(score)
scorelabel=Label(tk,text=txtscore, font="Times 20 bold", bg="deep sky blue", height=1, width=1)

labelAI = Label(tk, text="Choisir un mot et appuyer sur \n le bouton 'choisir ce mot'", font = "Times 25 bold", bg="deep sky blue", height=1, width=1)
AIentry = Entry(tk, bg="white", bd="1", cursor="dot", font = "Times 20 bold", textvariable=keyword_list, justify='center')    
buttonAI = Button(tk, text="Jouer avec l'Ordi", font = 'Times 20 bold', bg='#32586E', fg='black', activebackground= "#32586E" ,height=1, width=1, command=lambda:[phaseAI_setup(), phaseAI(), phase1_end()])    
button1 = Button(tk, text="JOUER", font='Times 20 bold', bg='green', fg='black', activebackground= "green" ,height=1, width=1, command=lambda : [phase1_end(), phase2_end(), phase3_setup(), phase3()] )
button2 = Button(tk, text="RÈGLES DU JEU", font='Times 20 bold', bg='firebrick1', fg='black', activebackground="red", height=1, width=1, command= lambda : [phase1_end(), phase2()])
message1 = Label( tk, text="Bienvenue au jeu du Pendu!", font='Times 50 bold', bg='deep sky blue', fg='black')
message2 = Label( tk, text="Pour commencer appuyez sur JOUER", font='Times 20 bold', bg='deep sky blue', fg='black')
message3 = Label( tk, text="Votre but est de trouver le mot mystere avant \n que le dessin du pendu soit fini.", font='Times 30 bold', bg='deep sky blue', fg='black')
message4 = Label( tk, text="Vous pouvez appuyez sur les lettres ainsi que les touches sur votre clavier pour jouer. \n Bonne chance!", font='Times 20 bold', bg='deep sky blue', fg='black')


#---------------Fonctions et algorithmes logiques du IA---------------
def set_toguess(w) :
    toguess = w


def get_probs(c_):
    global AI_W_DB
    
    probs = []
    
    print("!!!!!!!!!!!!!!!!!!!!!!!")
    print()
    print()
    
    subList = []
    
    for s in (AI_W_DB) :
        if (len(s) == len(c_)) :
            areIn = True
            
            for i in range(len(c_)) :
                if (c_[i] != "") :
                    if (c_[i] != s[i]) :
                        areIn = False
                        break
                for j in range(len(alreadytriedBad)) :
                    if (alreadytriedBad[j] == s[i] ) :
                        areIn = False
                        break
                if (not areIn) :
                    break
                
                
            if (areIn) :
                subList.append(s)
                
    if len(subList) == 0:
        print("503subL 0")
        setup()
        phaseAI_setup()
        restart_game()
        tkinter.messagebox.showinfo("Hangman", "Vous avez piégé l'Ordi!")
        return None
    
    print("subList : ", subList)
                   
    for l in range(26) :
        c = chr(97+l)
        inUsed = False
        
        for i in range(len(alreadytried)):
            if (c == alreadytried[i]) :
                inUsed = True
                
        if (not inUsed) :
            
            nbWord = 0
            for s in (subList) :
                for i in range(len(s)) :
                    if (c == s[i]) :
                        nbWord+=1
            probs.append(nbWord / len(subList))
        else :
             probs.append(0)
            
        print(c, ":",  probs[l], end=" | ")

    idx = 0
    for i in range(1, len(probs)) :
        if (probs[idx] < probs[i]) :
            idx = i
        
    guess = chr(idx+97)
    print("guess :::::::::", guess)

            
    return guess


def AI_Make_Guess() :
    guess = get_probs(word)
    addLetter(guess, True)
    print("AI guessed ", guess)
    check_win_AI()
    check_loss_AI()
    
    
#---------------Vérifier si on a gagné---------------
def check_win_AI():
    global word, togues, count, alreadytried, buttons
    isWin = True
    for i in range(len(toguess)) :
        if word[i] != toguess[i] :
            isWin = False
    if isWin == True:
          tkinter.messagebox.showinfo("Hangman", "L'Ordi à gagné en : " + str(len(alreadytriedBad)) + " coups !" )
          
#---------------Vérifier si on a perdu---------------            
def check_loss_AI() :
    global count
    if count >= 7 :
        tkinter.messagebox.showinfo("Hangman", "Bien joué, vous avez piégé l'Ordi!" )
 





setup()




#---------------Page de vérification du mécanisme de boucle---------------

while True:

    tk.update_idletasks()
    tk.update()

    if (game_phase[0] == 0) :   
        phase1()

    elif (game_phase[0] == 1) :
        phase2()
        
    elif (game_phase[0] == 2) :
        phase3()
    elif(game_phase[0]== 3):
        phaseAI()
        
Canvas.update()

tk.mainloop()









