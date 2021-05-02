from tkinter import *
import random as r
import tkinter.messagebox
tk=Tk()
tk.geometry('1794x700')
tk.configure(bg="deep sky blue")
tk.title("Jeu du Pendu")
Canvas=Canvas(tk, bg="deep sky blue", width=1794, height=700)
tk.resizable(False, False)

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
#wordlist=["sebastien","memoire","secondes"]
toguess=""
keyword_array=[]
    
alreadytriedBad = []


def process_data():
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
                #if word not in fiveLetterWords :
                    isgood= True
                    for s in word:
                        if not (97<= ord(s) and ord(s)<= 97+26):
                            isgood= False
                    if isgood:
                        fiveLetterWords.append(word)
    return fiveLetterWords
    

        

def setup():
    global wordlist, letters, toguess, word 
    for i in range(26):
        letters.append(chr(97+i))
    wordlist=process_data()
    
    print("len(w)", len(wordlist))
    toguess=wordlist[r.randint(0,len(wordlist)-1)]
    for i in range(len(toguess)):
        word.append("")
        print(toguess[i], end="")
        
        



def addLetter(guess) :
    global letters , alreadytried, buttons
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
    for i in range(len(word)):
        Canvas.create_text(680+60*i,325,fill="darkblue",font="Times 30 bold",text=word[i],tag="text" )
    alreadytried.append(guess)
    check_win() 

    
    
    
def boom():
    global count
    count+=1
    
    if count >= 1: #Draw hook
        Canvas.create_line(200,50,200,70,tags="hang")
    if count >= 2: #Draw face
        Canvas.create_oval(200-radius, 100-radius,
                           200+radius, 100+radius, tags="hang")
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

def phase1():
    game_phase[0]=0
    Canvas.place(x=0,y=0)
    
    message1.place(anchor='n', relx=0.5, rely=0.1, relwidth=0.8, relheight=0.180)

    
    message2.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.8, relheight=0.180)
    
     
    button1.place(anchor='n', relx=0.3, rely=0.55, relwidth=0.4, relheight=0.2)
    
    buttonAI.place(anchor='n', relx=0.5, rely=0.75, relwidth=0.4, relheight=0.2)
   
    button2.place(anchor='n', relx=0.7, rely=0.55, relwidth=0.4, relheight=0.2)
   

def phase1_end() :
    message1.destroy()
    message2.destroy()
    #button1.destroy()
    button2.destroy()

    
def phase2():

    game_phase[0]=1
   
    message3.place(anchor='n', relx=0.5, rely=0.1, relwidth=0.8, relheight=0.180)
   
    message4.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.8, relheight=0.180)
    
    button1.place(anchor='n', relx=0.5, rely=0.55, relwidth=0.8, relheight=0.2)
    
    buttonAI.place(anchor='n', relx=0.5, rely=0.75, relwidth=0.8, relheight=0.2)
    
    #phase2_effacer()
    
def phase2_end() :
    message3.destroy()
    message4.destroy()
    button1.destroy()
    buttonAI.destroy()
    
def key_pressed(event) :
    if not Ai_status:
        key = event.char
        addLetter(key)
    

   
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

def check_win():
    global word, togues, count, alreadytried, buttons
    isWin = True
    for i in range(len(word)) :
        if word[i] != toguess[i] :
            isWin = False
    if isWin == True:
          tkinter.messagebox.showinfo("Hangman", "Vous avez gagné! Cela vous à pris :" + str(len(alreadytried)) + "coups !" )
          for i in range(len(buttons)):
             buttons[i]["state"]= DISABLED
            


def restart_game():
    global button3, count, buttons, word, letters, toguess, alreadytried,alreadytriedBad,keyword_array
    Canvas.delete("hang")
    Canvas.delete("text")
    Canvas.delete("oldline")
    for i in range(len(buttons)):
             buttons[i]["state"]= NORMAL
    count=0
    alreadytried=[]
    word=[ ]
    letters=[ ]
    alreadytriedBad=[]
    keyword_array=[]
    print(alreadytried, "alreadytried")
    print(letters,"letters")
    print(toguess,"toguess")




def phase3_setup() :
    global buttons, buttonx, buttony
    print("t", toguess)
    for i in range(len(toguess)):
        Canvas.create_line(650+60*i,341,650+60*(i+1)-10,341, tag="oldline")
    
    for i in range(len(buttons)):
        buttons[i].config(bg="slate gray")
        buttons[i].place(anchor='n', relx=buttonx[i], rely=buttony[i], relwidth=0.1, relheight=0.1)
    tk.bind('<Key>', key_pressed)    

        
    
    button5 = Button(tk,text="Recommencer", font = "Times 15 bold", bg="SlateBlue2", fg="white", height=1, width=1, command= lambda :[restart_game(), setup(), phase3_setup()])
    button5.place(anchor='n', relx=0.890, rely=0.30, relwidth=0.1,relheight=0.1)
    
def phase3():
    global toguess, word
    game_phase[0]=2
    
    Canvas.place(x=0,y=0)

    Canvas.create_line(10,470-10,50,470-10)
    Canvas.create_line(30,470-10,30,50)
    Canvas.create_line(30,50,200,50)
    

    
    
def phaseAI():
     Ai_status=True
     game_phase[0]=3
     Canvas.place(x=0, y=0)
     Canvas.create_line(10,470-10,50,470-10)
     Canvas.create_line(30,470-10,30,50)
     Canvas.create_line(30,50,200,50)
     
def AiWordPhase(keyword_array):
    global toguess
    keyword_array.append(keyword_list.get())
    toguess=keyword_array[0]
    for i in range(len(toguess)):
        Canvas.create_line(650+60*i,341,650+60*(i+1)-10,341, tag="oldline")
    
    print(keyword_array)
     
def phaseAI_setup():
    for i in range(len(toguess)):
        Canvas.create_line(650+60*i,341,650+60*(i+1)-10,341, tag="oldline")
    
    AIentry.place(anchor='n', relx=0.450, rely=0.70, relwidth=0.4,relheight=0.2)
    
    AIentry.bind('<Return>', set_toguess(AIentry.get())) 
    print(set_toguess)
    
    buttonAI.destroy()
    button1.destroy()   
    message3.destroy()
    message4.destroy()
     
     
    button6 = Button(tk,text="Recommencer", font = "Times 15 bold", bg="SlateBlue2", fg="white", height=1, width=1, command= lambda :[restart_game(), setup(), phaseAI_setup()])
    button6.place(anchor='n', relx=0.890, rely=0.30, relwidth=0.1,relheight=0.1)
    button7= Button(tk,text="IA devine", font="Times 15 bold", bg="SlateBlue2", fg="white", height=1, width=1, command=lambda : [AI_Make_Guess()])
    button7.place(anchor='n', relx=0.890, rely=0.20, relwidth=0.1, relheight=0.1)
    
    
    
    button8= Button(tk,text="Chosir ce mot", font="Times 15 bold", bg="SlateBlue2", fg="white", height=1, width=1, command= lambda : [AiWordPhase(keyword_array)])
    button8.place(anchor='n', relx=0.890, rely=0.40, relwidth=0.1, relheight=0.1)
keyword_list=StringVar()    
AIentry = Entry(tk, bg="white", bd="1", cursor="dot", font = "Times 20 bold", textvariable=keyword_list)    
buttonAI = Button(tk, text="Jouer avec l'Ordi", font = 'Times 20 bold', bg='#32586E', fg='black', activebackground= "#32586E" ,height=1, width=1, command=lambda:[phaseAI_setup(), phaseAI(), phase1_end()])    
button1 = Button(tk, text="JOUER", font='Times 20 bold', bg='green', fg='black', activebackground= "green" ,height=1, width=1, command=lambda : [phase1_end(), phase2_end(), phase3_setup(), phase3()] )
button2 = Button(tk, text="RÈGLES DU JEU", font='Times 20 bold', bg='firebrick1', fg='black', activebackground="red", height=1, width=1, command= lambda : [phase1_end(), phase2()])
message1 = Label( tk, text="Bienvenue au jeu du Pendu!", font='Times 50 bold', bg='deep sky blue', fg='black')
message2 = Label( tk, text="Pour commencer appuyez sur JOUER", font='Times 20 bold', bg='deep sky blue', fg='black')
message3 = Label( tk, text="Votre but est de trouver le mot mystere avant \n que le dessin du pendu soit finit.", font='Times 30 bold', bg='deep sky blue', fg='black')
message4 = Label( tk, text="Vous pouvez appuyez sur les lettres ainsi que les touches sur votre clavier pour jouer. \n Bonne chance!", font='Times 20 bold', bg='deep sky blue', fg='black')
#button3= Button(tk, text="Retour", font='Times 10 bold', bg='white', fg='black', height=1, width=1, command = lambda : [phase2_end(), phase1()] )
#button3= Button(tk, text="Play", font='Times 10 bold', bg='white', fg='black', height=1, width=1, command = phase3)


def set_toguess(w) :
    toguess = w


def get_probs(c_):
    probs = []
    
    #Generate Sublist
    subList = []
    
    for s in (wordlist) :
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
            
    guess = chr(probs.index(max(probs))+97)

            
    return guess


def AI_Make_Guess() :
    guess = get_probs(word)
    addLetter(guess)
    print("AI guessed ", guess)
    
    
    





setup()

#print(letters)




while True:
    #print("toguess", toguess)
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



