from tkinter import *
import random as r
import tkinter.messagebox
tk=Tk()
tk.geometry('1794x700')
tk.configure(bg="deep sky blue")
tk.title("Jeu du Pendu")
Canvas=Canvas(tk, bg="deep sky blue", width=1794, height=700)
tk.resizable(False, False)

#---------------Variable Defining---------------
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
    
alreadytriedBad = []

germial = open("germinal.txt",'r')
word_AI = open("word_AI.txt", 'r')
AI_W_DB = []
#---------------Creating a List based on a book---------------
def process_data(isAI):
    fiveLetterWords= []
    if not isAI :
        f = open("germinal.txt",'r')
    else :
        f = open("word_AI.txt", 'r') 
    #germial = open("germinal.txt",'r')
    #word_AI = open("word_AI.txt", 'r')
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
                #if word not in fiveLetterWords :
                    isgood= True
                    for s in word:
                        if not (97<= ord(s) and ord(s)<= 97+26):
                            isgood= False
                    if isgood:
                        fiveLetterWords.append(word)
    return fiveLetterWords
    

        
#---------------Filling a list with all the letters of the alphabet and one with all the words and picking one of those words---------------
def setup():
    global wordlist, letters, toguess, word, AI_W_DB
    for i in range(26):
        letters.append(chr(97+i))
    wordlist=process_data(germial)
    print("len", len(wordlist))
    AI_W_DB = process_data(word_AI) 
    
    print("len(w)", len(wordlist))
    toguess=wordlist[r.randint(0,len(wordlist)-1)]
    for i in range(len(toguess)):
        word.append("")
        print(toguess[i], end="")
        
        



#---------------Main logic function that accounts for used letters/bad letters/guessed letters---------------
def addLetter(guess) :
    global letters , alreadytried, buttons
    print("len", len(letters))
    for i in range(len(letters)) :
        placed = 0
        if letters[i] == guess :
            letters.remove(guess)
            for j in range(len(toguess)):
                if guess == toguess[j] :
                    print(guess)
                    word[j] = guess
                    placed += 1
            
            if placed != 0 :
                
                buttons[ord(guess)-97].config(bg="green")

                break
            else :
                alreadytriedBad.append(guess)
                boom()
                buttons[ord(guess)-97].config(bg="red")
                print("placed", placed)
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
    check_win()
    check_loss()
    
    print("var", word, toguess)

    
    
#---------------Function to draw the Hangman---------------    
def boom():
    global count
    count+=1
    
    if count >= 1: #Draw hook
        Canvas.create_line(200,50,200,70,tags="hang")
    if count >= 2: #Draw face
        Canvas.create_oval(200-radius, 100-radius, 200+radius, 100+radius, tags="hang")
    if count >= 3: #Draw first arm
        Canvas.create_line(200,150,100,100,tags="hang")
    if count >= 4: #Draw second arm
        Canvas.create_line(200,150,300,100,tags="hang")
    if count >= 5: #Draw body length
        Canvas.create_line(200,130,200,250,tags="hang")
    if count >= 6: #Draw one leg
        Canvas.create_line(200,250,100,300,tags="hang")
    if count >= 7: #Draw second leg
        Canvas.create_line(200,250,300,300,tags="hang")

#---------------First page setup---------------
def phase1():
    game_phase[0]=0
    Canvas.place(x=0,y=0)
    
    message1.place(anchor='n', relx=0.5, rely=0.09, relwidth=0.8, relheight=0.180)

    
    message2.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.8, relheight=0.180)
    
     
    button1.place(anchor='n', relx=0.3, rely=0.55, relwidth=0.4, relheight=0.2)
    
    buttonAI.place(anchor='n', relx=0.5, rely=0.75, relwidth=0.4, relheight=0.2)
   
    button2.place(anchor='n', relx=0.7, rely=0.55, relwidth=0.4, relheight=0.2)
   
#---------------Deleting widgets from the first page---------------
def phase1_end() :
    message1.destroy()
    message2.destroy()
    #button1.destroy()
    button2.destroy()


#---------------Second page setup---------------
def phase2():

    game_phase[0]=1
   
    message3.place(anchor='n', relx=0.5, rely=0.07, relwidth=0.8, relheight=0.180)
   
    message4.place(anchor='n', relx=0.5, rely=0.30, relwidth=0.8, relheight=0.180)
    
    button1.place(anchor='n', relx=0.5, rely=0.55, relwidth=0.8, relheight=0.2)
    
    buttonAI.place(anchor='n', relx=0.5, rely=0.75, relwidth=0.8, relheight=0.2)
    
    #phase2_effacer()


#---------------Deleting items from second page---------------
def phase2_end() :
    message3.destroy()
    message4.destroy()
    button1.destroy()
    buttonAI.destroy()
 
#---------------Function to bind keyboard keys to letter buttons---------------
def key_pressed(event) :
    if not Ai_status:
        key = event.char
        addLetter(key)
    





# ---------------Creating the buttons for each letter---------------

#for i in range(26) :
#    #button3 = Button(tk, text=chr(65+i), font='Times 20 bold', bg='slate gray', fg='white', height=1, width=1,command=lambda: addLetter(chr(97+i)))
#    v_ = chr(97+i)   
#    buttons.append(Button(tk, text=chr(65+i), font='Times 20 bold', bg='slate gray', fg='white', height=1, width=1,command=lambda a: addLetter(v_)))    
    
button3 = Button(tk, text="A", font='Times 20 bold', bg='slate gray', fg='white', height=1, width=1,command=lambda: addLetter("a"))
buttons.append(button3)

button3 = Button(tk, text="B", font='Times 20 bold', bg='light cyan', fg='white', height=1, width=1,command=lambda: addLetter("b"))
buttons.append(button3)

button3 = Button(tk, text="C", font='Times 20 bold', bg='light cyan', fg='white', height=1, width=1,command=lambda: addLetter("c"))
buttons.append(button3)

button3 = Button(tk, text="D", font='Times 20 bold', bg='light cyan', fg='white', height=1, width=1,command=lambda: addLetter("d"))
buttons.append(button3)

button3 = Button(tk, text="E", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("e"))
buttons.append(button3)

button3 = Button(tk, text="F", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("f"))
buttons.append(button3)

button3 = Button(tk, text="G", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("g"))
buttons.append(button3)

button3 = Button(tk, text="H", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("h"))
buttons.append(button3)

button3 = Button(tk, text="I", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("i"))
buttons.append(button3)

button3 = Button(tk, text="J", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("j"))
buttons.append(button3)

button3 = Button(tk, text="K", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("k"))
buttons.append(button3)

button3 = Button(tk, text="L", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("l"))
buttons.append(button3)

button3 = Button(tk, text="M", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("m"))
buttons.append(button3)

button3 = Button(tk, text="N", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("n"))
buttons.append(button3)

button3 = Button(tk, text="O", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("o"))
buttons.append(button3)

button3 = Button(tk, text="P", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("p"))
buttons.append(button3)

button3 = Button(tk, text="Q", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("q"))
buttons.append(button3)

button3 = Button(tk, text="R", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("r"))
buttons.append(button3)

button3 = Button(tk, text="S", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("s"))
buttons.append(button3)

button3 = Button(tk, text="T", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("t"))
buttons.append(button3)

button3 = Button(tk, text="U", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("u"))
buttons.append(button3)

button3 = Button(tk, text="V", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("v"))
buttons.append(button3)

button3 = Button(tk, text="W", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("w"))
buttons.append(button3)

button3 = Button(tk, text="X", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("x"))
buttons.append(button3)

button3 = Button(tk, text="Y", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("y"))
buttons.append(button3)

button3 = Button(tk, text="Z", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("z"))
buttons.append(button3)


#---------------Checking for a win---------------
def check_win():
    global word, togues, count, alreadytried, buttons
    isWin = True
    for i in range(len(toguess)) :
        if word[i] != toguess[i] :
            isWin = False
    if isWin == True:
          tkinter.messagebox.showinfo("Hangman", "Vous avez gagné! Cela vous à pris :" + str(len(alreadytriedBad)) + " coups !" )
          for i in range(len(buttons)):
             buttons[i]["state"]= DISABLED
            
#---------------Checking for a loss---------------            
def check_loss() :
    global count
    if count >= 7 :
        tkinter.messagebox.showinfo("Hangman", "Vous avez perdu!" )
        for i in range(len(buttons)):
            buttons[i]["state"]= DISABLED   
    

#---------------Function behind the restart button---------------
def restart_game():
    global button3, count, buttons, word, letters, toguess, alreadytried,alreadytriedBad,keyword_array
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
    print(alreadytried, "alreadytried")
    print(letters,"letters")
    print(toguess,"toguess")
    
    print("length", len(word), len(toguess))
    print("var", word, toguess)



#---------------Setting up the game page---------------
def phase3_setup() :
    global buttons, buttonx, buttony
    print("t", toguess)
    
    middle = 850
    for i in range(len(toguess)) :
        Canvas.create_line(middle - 60*len(toguess)//2 + 60*i, 341, middle - 60*len(toguess)//2 + 60*i + 50, 341, tag="oldline")

    
    for i in range(len(buttons)):
        buttons[i].config(bg="slate gray")
        buttons[i].place(anchor='n', relx=buttonx[i], rely=buttony[i], relwidth=0.1, relheight=0.1)
    tk.bind('<Key>', key_pressed)    

        
    
    button5 = Button(tk,text="Recommencer", font = "Times 15 bold", bg="SlateBlue2", fg="white", height=1, width=1, command= lambda :[restart_game(), setup(), phase3_setup()])
    button5.place(anchor='n', relx=0.890, rely=0.30, relwidth=0.1,relheight=0.1)
  
 #---------------Game page Widgets--------------- 
def phase3():
    global toguess, word
    game_phase[0]=2
    
    Canvas.place(x=0,y=0)

    Canvas.create_line(10,470-10,50,470-10)
    Canvas.create_line(30,470-10,30,50)
    Canvas.create_line(30,50,200,50)
    

    
#---------------AI page setup---------------    
def phaseAI():
     Ai_status=True
     game_phase[0]=3
     Canvas.place(x=0, y=0)
     Canvas.create_line(10,470-10,50,470-10)
     Canvas.create_line(30,470-10,30,50)
     Canvas.create_line(30,50,200,50)
  
 #---------------Getting the word entered by user input--------------- 
def AiWordPhase(keyword_array):
    global toguess
    keyword_array.append(keyword_list.get())
    
    if len(keyword_array[0]) >= 5:
        toguess=str(keyword_array[0])
        middle = 850
        for i in range(len(toguess)) :
            Canvas.create_line(middle - 60*len(toguess)//2 + 60*i, 341, middle - 60*len(toguess)//2 + 60*i + 50, 341, tag="oldline")
        
        print(keyword_array)
    else :
        tkinter.messagebox.showinfo("Hangman", "Mot invalide, veuillez en choisir un autre (plus de 5 lettres)" )

        
 #---------------Further setting up AI page mechanics---------------   
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
     
     
    button6 = Button(tk,text="Recommencer", font = "Times 15 bold", bg="SlateBlue2", fg="white", height=1, width=1, command= lambda :[setup(), phaseAI_setup(), restart_game()])
    button6.place(anchor='n', relx=0.890, rely=0.30, relwidth=0.1,relheight=0.1)
    button7= Button(tk,text="IA devine", font="Times 15 bold", bg="SlateBlue2", fg="white", height=1, width=1, command=lambda : [AI_Make_Guess()])
    button7.place(anchor='n', relx=0.890, rely=0.20, relwidth=0.1, relheight=0.1)
    
    labelAI = Label(tk, text="Choisir un mot et appuyer sur \n le bouton choisir ce mot", font = "Times 25 bold", bg="deep sky blue", height=1, width=1,)
    labelAI.place(anchor="n", relx=0.850, rely=0.65, relwidth=0.50, relheight=0.50)    
    
    button8= Button(tk,text="Chosir ce mot", font="Times 15 bold", bg="SlateBlue2", fg="white", height=1, width=1, command= lambda : [AiWordPhase(keyword_array), restart_game(), phaseAI_setup()])
    button8.place(anchor='n', relx=0.890, rely=0.40, relwidth=0.1, relheight=0.1)
    
#---------------Widgets defined out of functions for different pages---------------    
keyword_list=StringVar()    
AIentry = Entry(tk, bg="white", bd="1", cursor="dot", font = "Times 20 bold", textvariable=keyword_list, justify='center')    
buttonAI = Button(tk, text="Jouer avec l'Ordi", font = 'Times 20 bold', bg='#32586E', fg='black', activebackground= "#32586E" ,height=1, width=1, command=lambda:[phaseAI_setup(), phaseAI(), phase1_end()])    
button1 = Button(tk, text="JOUER", font='Times 20 bold', bg='green', fg='black', activebackground= "green" ,height=1, width=1, command=lambda : [phase1_end(), phase2_end(), phase3_setup(), phase3()] )
button2 = Button(tk, text="RÈGLES DU JEU", font='Times 20 bold', bg='firebrick1', fg='black', activebackground="red", height=1, width=1, command= lambda : [phase1_end(), phase2()])
message1 = Label( tk, text="Bienvenue au jeu du Pendu!", font='Times 50 bold', bg='deep sky blue', fg='black')
message2 = Label( tk, text="Pour commencer appuyez sur JOUER", font='Times 20 bold', bg='deep sky blue', fg='black')
message3 = Label( tk, text="Votre but est de trouver le mot mystere avant \n que le dessin du pendu soit finit.", font='Times 30 bold', bg='deep sky blue', fg='black')
message4 = Label( tk, text="Vous pouvez appuyez sur les lettres ainsi que les touches sur votre clavier pour jouer. \n Bonne chance!", font='Times 20 bold', bg='deep sky blue', fg='black')
#button3= Button(tk, text="Retour", font='Times 10 bold', bg='white', fg='black', height=1, width=1, command = lambda : [phase2_end(), phase1()] )
#button3= Button(tk, text="Play", font='Times 10 bold', bg='white', fg='black', height=1, width=1, command = phase3)

#---------------AI logic functions and algorithms---------------
def set_toguess(w) :
    toguess = w


def get_probs(c_):
    global AI_W_DB
    
    probs = []
    
    #Generate Sublist
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
        print("subL 0")
        return
    #print("subList : ", subList)
    
    #Find Probs                
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
            
        #print(c, ":",  probs[l], end=" | ")
            
    m = probs[0]
    idx = 0
    for i in range(1, len(probs)) :
        if (m < probs[i]) :
            idx = i
        
    guess = chr(idx+97)

            
    return guess


def AI_Make_Guess() :
    guess = get_probs(word)
    addLetter(guess)
    print("AI guessed ", guess)
    check_win_AI()
    check_loss_AI()
    
    
#---------------Checking for a win---------------
def check_win_AI():
    global word, togues, count, alreadytried, buttons
    isWin = True
    for i in range(len(toguess)) :
        if word[i] != toguess[i] :
            isWin = False
    if isWin == True:
          tkinter.messagebox.showinfo("Hangman", "L'Ordi à gagné en :" + str(len(alreadytriedBad)) + " coups !" )
          
#---------------Checking for a loss---------------            
def check_loss_AI() :
    global count
    if count >= 7 :
        tkinter.messagebox.showinfo("Hangman", "Bien joué, vous avez piégé l'Ordi!" )
 





setup()




#---------------Page checking mechanism loop---------------

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






