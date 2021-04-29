#Bonjour Monsieur,
#Petite préface pour vous prévenir et m'excuser sur le fait que mon IA n'est pas très performante...
#Pas de problème au niveau du code, mais je n'ai pas eu le temps de l'optimiser
#pour qu'il prenne un temps raisonnable pour une profondeur de 5, où on peut la considérer "parfaite".
#Elle fonctionne correctement, mais en trop de temps.
#Bref, ce n'est pas ma meilleur IA, donc je m'excuse pour la petite déception de ce coté





#------------------------Création de la page et initialisation------------------------

from tkinter import *

fen=Tk()

def creer_la_page(couleur,fe):
    fe.title('machine de base')
    fe.configure(bg=couleur)
    fe.geometry('1200x700+600+50')
#     for i in range(nblignes):
#         for j in range(nbcolonnes):
#             vide=Label(fen,text='kk ',bg="white",fg=couleur, font=("Arial bold",10))
#             vide.grid(row =i, column =j)
                        
creer_la_page('blue', fen)


width = 1000
height = 600



game_phase = [0]

rows, cols = 6, 7

canvas = Canvas(fen, bg="white", width=width, height=height)

winner_message = {"message" : ("Les Bleus sont Vainqueur!", "Les Rouges sont Vainqueur!", "Pas de Vainqueur : Égalité!"), "color": ("blue", "red", "violet")}

players = {"human" : -1, "ai": 1}
depth_max = [3]

board = []

length_to_win = 4#min(min(rows,cols), 4)

isIA = [False]

dx, dy = width/cols, height/rows
diameter = min(dx, dy)


#------------------------Fonctions d'affichage------------------------

def draw_grid(rows_, cols_) :
    for i in range(cols_):
        for j in range(rows_):
            line = canvas.create_line(dx*i, j*dy, dx*i+width, j*dy       )
            line = canvas.create_line(dx*i, j*dy, dx*i      , j*dy+height)
    canvas.update()



draw_grid(rows,cols)

def circle(x, y, player) :
    if player == 1 :
        color = "red"
    elif player == -1:
        color = "blue"
    else :
        color = "black"
    oval = canvas.create_oval((y+1)*dx - diameter, (x+1)*dy - diameter, (y+1)*dx, (x+1)*dy, fill=color) #
    
# circle(1,4, 1)
# circle(3,7, 1)

                
def show_pieces() :
    for i in range(rows) :
        for j in range(cols) :
            if (board[i][j] != 0) :
                circle(i, j, board[i][j])



#------------------------Fonctions de logique------------------------

def createBoard() :
    for i in range(rows):
        board.append([])
        for j in range(cols):
            board[i].append(0)
    #turn = 0
createBoard()    
    

            
def removePiece(col_) :
    for i in range(len(board)):
        if board[i][col_] != 0:
            board[i][col_] = 0
            break
    
def pieces_on_board() :
    nb = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] != 0):
                nb+=1
    return nb

def check_win() :
    winner = 0
    
    full = True
    for i in range(cols) :
        if (board[0][i] == 0) :
            full = False
            break
    if full :
        return -2
    
    for i in range(cols): #colonnes
        for j in range(rows-length_to_win+1):
            s = 0
            for k in range(length_to_win):
                s+= board[j+k][i]
            if s == length_to_win:
                winner = 1
            elif s == -length_to_win:
                winner = -1
            
    for i in range(rows): #lignes
        for j in range(cols-length_to_win+1) :
            s = 0
            for k in range(length_to_win):
                s += board[i][j+k]
            if s == length_to_win:
                winner = 1
            elif s == -length_to_win:
                winner = -1
    
    #----diag--------
    #West-South
    for i in range(rows-1, 0, -1):
        diago = []
        for j in range(0, cols):
            if (j+i < rows) :
                diago.append(board[i+j][j])
        for n in range(0, len(diago)-length_to_win+1):
            s = 0
            for m in range(length_to_win):
                s+= diago[n+m]
                #fen.bind("<Button 1>",player_add)
            if s == length_to_win:
                winner = 1
            elif s == -length_to_win:
                winner = -1
    
    #North-East
    for i in range(cols+rows):
        diago = []
        for j in range(rows):
            if (j+i < cols) :
                diago.append(board[j][i+j])
        for n in range(0, len(diago)-length_to_win+1):
            s = 0
            for m in range(length_to_win):
                s+= diago[n+m]
            if s == length_to_win:
                winner = 1
            elif s == -length_to_win:
                winner = -1
              
   #South-East   
    for i in range(cols):
        diago = []
        for j in range(rows-1, -1, -1):
            if (i+(rows-j) < cols) :
                diago.append(board[j][i+(rows-j)])
        for n in range(0, len(diago)-length_to_win+1):
            s = 0
            for m in range(length_to_win):
                s+= diago[n+m]
            if s == length_to_win:
                winner = 1
            elif s == -length_to_win:
                winner = -1
    
    #West-North
    for i in range(rows-1, -1, -1):
        diago = []
        for j in range(cols):
            if (0 <= i-j and i-j <= rows-1) :
                diago.append(board[i-j][j])
        for n in range(0, len(diago)-length_to_win+1):
            s = 0
            for m in range(length_to_win):
                s+= diago[n+m]
            if s == length_to_win:
                winner = 1
            elif s == -length_to_win:
                winner = -1                
    
    return winner

def addPiece(col_, player) :
    #if (0 <= col_ and col_ < len(board[0])):
        if (board[0][col_] == 0) :
            for i in range(rows-1, -1, -1):
                if (board[i][col_] == 0) :
                    board[i][col_] = player
                    #print("piece added", pieces_on_board() %2)
                    break
    #else :
        #print("wrung 77")
                
    #removePiece(col_)

def player_add(eventorigin) :
    if (game_phase[0] == 1):
        mousex = eventorigin.x
        for i in range(cols) :
            if (i*dx < mousex and mousex < (i+1)*dx) :
                addPiece(i,2*(pieces_on_board()%2)-1)


canvas.bind("<Button 1>",player_add)






def Message_Winner(winner) :
    if winner == -2 :
        winner_index = 2
    if winner == -1 :
        winner_index = 0
    if winner == 0 :
        winner_index = 2
    if winner == 1 :
        winner_index = 1
    text = Label(fen, text=winner_message["message"][winner_index], bg="white", width="40", height="2", fg=winner_message["color"][winner_index], font=("Courier", 20))
    text.place(x=100, y= 10)




#--------------------IA--------------------

def find_Moves() :
    moves = []
    for i in range(cols):
        if board[0][i] == 0:
            moves.append(i)
    return moves
nb_eval = [0]

def best_move() :
    pieces_init = pieces_on_board() %2
    
    allMoves = find_Moves()
    bestScore = -100000
    bestMove = 0
    for i in range(cols) :
        if (board[0][i] != 0) :
            bestMove = i
            break
    
    for i in allMoves:
        #print("loop nb ", i)
        addPiece(i, players["ai"])
        score = minimax(0, -1000000, 100000, False)##Evaluate(-1)#
        removePiece(i)
        if (score > bestScore) : 
            bestScore = score
            bestMove = i
            #print("new best ", i, bestScore)
    print("depth ",depth_max[0])
    print("bestscore ", bestScore,  "bestMove ", bestMove)
    addPiece(bestMove, players["ai"])
    #print(pieces_on_board() %2 == pieces_init)
    #print("")
    print("nb eval ", nb_eval[0])
    
def minimax(depth, alpha, beta, isMaximizing) :
    result = check_win()
    if (result != 0) :
        return result*100000 - 20*depth
    
    if (result == -2) :
        return 0
        
    if (depth >= depth_max[0]):#depth_max[0]) :#check_win() != 0):# # and
        nb_eval[0] += 1
        #print("evaluate : ", Evaluate(-1 if depth%2 == 0 else 1))
        return -Evaluate(-1 if depth%2 == 0 else 1)
    
    
    if (isMaximizing) :
        allMoves = find_Moves()
        bestScore = -1000000000#float("-inf")
        for i in range(len(allMoves)):
            move = allMoves[i]
            addPiece(move, players["ai"])
            #print("ai pieces after add ", pieces_on_board() %2, i)
            score = minimax(depth+1, alpha, beta, False)
            removePiece(move)
            #print("ai pieces after remove ", pieces_on_board() %2)
            if (score > bestScore) :
                bestScore = score
            alpha = max(alpha, score)
            if (beta <= alpha) :
                break
        return bestScore
    else :
        allMoves = find_Moves()
        bestScore = 1000000000#float("inf")
        for i in range(len(allMoves)):
            move = allMoves[i]
            addPiece(move, players["human"])
            #print("pieces after add ", pieces_on_board() %2)
            score = minimax(depth+1, alpha, beta, True)
            removePiece(move)
            #print("pieces after remove ", pieces_on_board() %2)
            if (score < bestScore) :
                bestScore = score
            beta = max(beta, score)
            if (beta <= alpha) :
                break
        return bestScore        


def lengthLine(begin_i, begin_j, end_i, end_j, type_) :
    nb = 0
    if (begin_i == end_i) :
        for j in range(begin_j, end_j):
            if (j < rows) :
                if (board[begin_i][j] == type_):
                    nb += 1

    if (begin_j == end_j) :
        for i in range(begin_i, end_i):
            if (i < rows) :
                if (board[i][begin_j] == type_):
                    nb += 1

#     for i in range(begin_i, end_i):
#         for j in range(begin_j, end_j):
#             if (board[i][j] == type_):
#                 nb += 1
    #print(nb)
    return nb


def lengthDiago(init_i, init_j, direction, type_) :
    length = 0
    if (direction == 1) :
        for n in range(0, 4) :

            if (init_i + n < rows and init_j + n < cols) :
                if (board[init_i+n][init_j+n] == type_) :
                    length += 1
    else :
        for n in range(0, 4) :

            if (init_i + n < rows and init_j - n < cols and init_j - n >= 0) :
                if (board[init_i+n][init_j-n] == type_) :
                    length += 1
    return length
    

#canvas.bind("<Button 1>", lengthLine(0,0,3,3,0) )

def Evaluate(perspective):
    Eval = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if ( (lengthLine(i, j, i+4, j, players["ai"]) == 3 and lengthLine(i, j, i+4, j, 0) == 1)
                 or (lengthLine(i, j, i, j+4, players["ai"]) == 3 and lengthLine(i, j, i, j+4, 0) == 1)
                 or (lengthDiago(i, j, 0, players["ai"]) == 3 and lengthDiago(i, j, 1, 0) == 1)) :
                Eval -= 1000
                
            if ( (lengthLine(i, j, i+4, j, players["ai"]) == 2 and lengthLine(i, j, i+4, j, 0) == 2) or  (lengthLine(i, j, i, j+4, players["ai"]) == 2 and lengthLine(i, j, i, j+4, 0) == 2)
                 or (lengthDiago(i, j, 0, players["ai"]) == 2 and lengthDiago(i, j, 1, 0) == 2)) :
                Eval -= 100
                 
            if ( (lengthLine(i, j, i+4, j, players["ai"]) == 1 and lengthLine(i, j, i+4, j, 0) == 3) or  (lengthLine(i, j, i, j+4, players["ai"]) == 1 and lengthLine(i, j, i, j+4, 0) == 3)
                 or (lengthDiago(i, j, 0, players["ai"]) == 3 and lengthDiago(i, j, 1, 0) == 1)) :
                Eval -= 1
     
            if ( (lengthLine(i, j, i+4, j, players["human"]) == 3 and lengthLine(i, j, i+4, j, 0) == 1) or  (lengthLine(i, j, i, j+4, players["human"]) == 3 and lengthLine(i, j, i, j+4, 0) == 1)
                 or (lengthDiago(i, j, 0, players["human"]) == 3 and lengthDiago(i, j, 1, 0) == 1)) :
                Eval += 1000
                
            if ( (lengthLine(i, j, i+4, j, players["human"]) == 2 and lengthLine(i, j, i+4, j, 0) == 2) or  (lengthLine(i, j, i, j+4, players["human"]) == 2 and lengthLine(i, j, i, j+4, 0) == 2)
                 or (lengthDiago(i, j, 0, players["human"]) == 2 and lengthDiago(i, j, 1, 0) == 2)) :
                Eval += 100
               
            if ( (lengthLine(i, j, i+4, j, players["human"]) == 1 and lengthLine(i, j, i+4, j, 0) == 3) or  (lengthLine(i, j, i, j+4, players["human"]) == 1 and lengthLine(i, j, i, j+4, 0) == 3)
                 or (lengthDiago(i, j, 0, players["human"]) == 3 and lengthDiago(i, j, 1, 0) == 1)) :
                Eval += 1
    return Eval*perspective



def game_phase_up() :
    game_phase[0] = 1

def finish_game() :
    game_phase[0] = 2







#------------------------Mise en page et temps de jeux------------------------



textHead = Label(fen, text="Connect 4", bg="blue", width="20", height="2", fg="black", font=("Courier", 40))
text0 = Label(fen, text="Comment jouer ?", bg="blue", width="30", height="2", fg="black", font=("Courier", 25))
text = Label(fen, text="Cliquez sur une colonne pour y déposer une pièce", bg="blue", width="50", height="2", fg="white", font=("Courier", 20))
text2 = Label(fen, text="Alignez quatre pièces de votre couleur pour gagner!", bg="blue", width="52", height="2", fg="white", font=("Courier", 20))
text3 = Label(fen, text="Soyez stratégique afin de bloquer l'ennemi ", bg="blue", width="50", height="2", fg="white", font=("Courier", 20))


textai0 = Label(fen, text="Sur l'IA :", bg="blue", width="30", height="2", fg="black", font=("Courier", 25))
textai = Label(fen, text="Plusieurs difficultés vous sont proposées", bg="blue", width="50", height="2", fg="white", font=("Courier", 20))
textai2 = Label(fen, text="Cliquez sur les boutons à gauche pour \n régler le niveau de l'IA", bg="blue", width="52", height="2", fg="white", font=("Courier", 20))
textai3 = Label(fen, text="Plus l'IA est fort, plus il met du temps à jouer ", bg="blue", width="55", height="2", fg="white", font=("Courier", 20))

def change_label() :
    buttonTalkAi.destroy()
    
    textai0.place(x=0, y= 150)
    
    textai.place(x=100, y= 250)

    textai2.place(x=100, y= 350)
    
    textai3.place(x=100, y= 450)
    

    
def set_for_AI() :
    change_label() 
    isIA[0] = True

button0 = Button(fen, text="Jouer!", command=game_phase_up, width="8", height="1", font=("Courier", 40))

buttonTalkAi = Button(fen, text="Jouer \n contre \n l'IA", command=set_for_AI, width="10", height="2", font=("Courier", 30))

def phase0_setup() :
    buttonTalkAi.place(x=700, y=525)


def phase0() :
    textHead.place(x = 200, y = 10)
    
    text0.place(x=0, y= 150)
    
    text.place(x=100, y= 250)

    text2.place(x=100, y= 350)
    
    text3.place(x=100, y= 450)
    
  
    button0.place(x=200, y=550)
    #game_phase[0] += 1

def set_depth_easy() :
    depth_max[0] = 2
def set_depth_medium() :
    depth_max[0] = 3
def set_depth_hard() :
    depth_max[0] = 4
    
button1 = Button(fen, text="Terminer", width="20", height="1", command=finish_game)
buttona = Button(fen, text="Facile", width="20", height="1", command=set_depth_easy)
buttonb = Button(fen, text="Moyen", width="20", height="1", command=set_depth_medium)
buttonc = Button(fen, text="Diffcile", width="20", height="1", command=set_depth_hard)


Labela = Label(fen, text="", width="20", height="1", bg="blue")
Labelb = Label(fen, text="", width="20", height="1")
Labelc = Label(fen, text="", width="20", height="1")

#     Labela.place(x=1020, y=300)
#     Labelb.place(x=1020, y=350)
#     Labelc.place(x=1020, y=400)

    



def phase1_setup() :
    buttonTalkAi.destroy()

    textHead.destroy()
    button0.destroy()
    text0.destroy()    
    text.destroy()
    text2.destroy()
    text3.destroy()
    
    textai0.destroy()
    textai.destroy()
    textai2.destroy()
    textai3.destroy()
        
    button1.place(x=1020, y=500)

    if (isIA[0]) :
        textIAdiff.place(x=1010, y= 230)

        buttona.place(x=1020, y=300)
        buttonb.place(x=1020, y=350)
        buttonc.place(x=1020, y=400)

    
    print("setup")
    #buttonYeaAI.place(x=1020, y= 100)


difficulties = ("Facile", "Moyen", "Difficile")

textIAdiff = Label(fen, text="Difficultés \n de l'IA \n"+str(difficulties[depth_max[0]-2]), bg="blue", width="20", height="3", fg="white", font=("Courier", 10))

def phase1() :
    textIAdiff.config(text="Difficultés \n de l'IA \n"+str(difficulties[depth_max[0]-2]))

    
    canvas.place(x=0, y=100)

    #show_pieces()    
    canvas.update()
    if (pieces_on_board() %2 == 1/2*players["ai"]+1/2 and isIA[0]) :
        print("start")
        best_move()
        print("end")
        print()
        
    if check_win() != 0:
        print(check_win())
        game_phase[0] += 1
    show_pieces()    

        
def end() :
    fen.destroy()    
    
button2 = Button(fen, text="Fermer", command=end, width="20", height="2")
def phase2_setup() :
    button1.destroy()
    buttona.destroy()
    buttonb.destroy()
    buttonc.destroy()
    
    textIAdiff.destroy()

    
    button2.place(x=1020, y=20)    

def phase2() :
    Message_Winner(check_win())

setup_done = [False, False, False]



#------------------------Mise à jour de la fenêtre------------------------
while True:
    fen.update_idletasks()
    fen.update()

    if (game_phase[0] == 0) :
        if (setup_done[0] == False) :
            phase0_setup()
            print("a")
            setup_done[0] = True
        phase0()

    elif (game_phase[0] == 1) :
        if (setup_done[1] == False) :
            phase1_setup()
            print("b")
            setup_done[1] = True
        
        phase1()
    elif (game_phase[0] == 2) :
        if (setup_done[2] == False) :
            phase2_setup()
            print("c")
            setup_done[2] = True
        
        phase2()