from tkinter import *
import random as r
import tkinter.messagebox

tk=Tk()
tk.geometry('1794x700')
tk.configure(bg="deep sky blue")

tk.title("Jeu de Pendu")
wordlist=["sebastien","memoire","secondes"]
toguess=""

#buttonx=[0.050,0.150,0.247,0.345,0.443,0.540,0.638,0.736,0.833,0.930,0.050,0.150,0.247,0.345,0.443,0.540,0.638,0.736,0.833,0.930,0.247,0.345,0.443,0.540,0.638,0.736]
#buttony=[0.68,0.68,0.68,0.68,0.68,0.68,0.68,0.68,0.68,0.68,0.78,0.78,0.78,0.78,0.78,0.78,0.78,0.78,0.78,0.78,0.88,0.88,0.88,0.88,0.88,0.88]
buttons=[]
word=[ ]
letters=[ ]
alreadytried=[ ]


Canvas=Canvas(tk, bg="deep sky blue", width=1794, height=470)
radius = 30
count=0
def create():
    global toguess, word
    Canvas.place(x=0,y=0)

    Canvas.create_line(10,470-10,50,470-10)
    Canvas.create_line(30,470-10,30,50)
    Canvas.create_line(30,50,200,50)

    print("t", toguess)
    for i in range(len(toguess)):
        Canvas.create_line(650+60*i,341,650+60*(i+1)-10,341)
        

        

def setup():
    global wordlist, letters, toguess, word
    for i in range(26):
        letters.append(chr(97+i))
    toguess=wordlist[r.randint(0,len(wordlist)-1)]
    for i in range(len(toguess)):
        word.append("")
        print(toguess[i])
        



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
                boom()
                buttons[ord(guess)-97].config(bg="red")
                print(placed)
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
        Canvas.create_text(680+60*i,330,fill="darkblue",font="Times 20 bold",text=word[i] )
    alreadytried.append(guess)
   


     
    
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
 

button1 = Button(tk, text="A", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("a"))
button1.place(anchor='n', relx=0.050, rely=0.68, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="B", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("b"))
button1.place(anchor='n', relx=0.150, rely=0.68, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="C", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("c"))
button1.place(anchor='n', relx=0.247, rely=0.68, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="D", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("d"))
button1.place(anchor='n', relx=0.345, rely=0.68, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="E", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("e"))
button1.place(anchor='n', relx=0.443, rely=0.68, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="F", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("f"))
button1.place(anchor='n', relx=0.540, rely=0.68, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="G", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("g"))
button1.place(anchor='n', relx=0.638, rely=0.68, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="H", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("h"))
button1.place(anchor='n', relx=0.736, rely=0.68, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="I", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("i"))
button1.place(anchor='n', relx=0.833, rely=0.68, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="J", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("j"))
button1.place(anchor='n', relx=0.930, rely=0.68, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="K", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("k"))
button1.place(anchor='n', relx=0.050, rely=0.78, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="L", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("l"))
button1.place(anchor='n', relx=0.150, rely=0.78, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="M", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("m"))
button1.place(anchor='n', relx=0.247, rely=0.78, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="N", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("n"))
button1.place(anchor='n', relx=0.345, rely=0.78, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="O", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("o"))
button1.place(anchor='n', relx=0.443, rely=0.78, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="P", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("p"))
button1.place(anchor='n', relx=0.540, rely=0.78, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="Q", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("q"))
button1.place(anchor='n', relx=0.638, rely=0.78, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="R", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("r"))
button1.place(anchor='n', relx=0.736, rely=0.78, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="S", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("s"))
button1.place(anchor='n', relx=0.833, rely=0.78, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="T", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("t"))
button1.place(anchor='n', relx=0.930, rely=0.78, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="U", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("u"))
button1.place(anchor='n', relx=0.247, rely=0.88, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="V", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("v"))
button1.place(anchor='n', relx=0.345, rely=0.88, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="W", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("w"))
button1.place(anchor='n', relx=0.443, rely=0.88, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="X", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("x"))
button1.place(anchor='n', relx=0.540, rely=0.88, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="Y", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("y"))
button1.place(anchor='n', relx=0.638, rely=0.88, relwidth=0.1, relheight=0.1)
buttons.append(button1)

button1 = Button(tk, text="Z", font='Times 20 bold', bg='black', fg='white', height=1, width=1,command=lambda: addLetter("z"))
button1.place(anchor='n', relx=0.736, rely=0.88, relwidth=0.1, relheight=0.1)
buttons.append(button1)




setup()
create() 
print(letters)

Canvas.update()

tk.mainloop()

