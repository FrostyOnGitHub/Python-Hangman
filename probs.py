wordList = ["word", "letter", "tonny", "sebastien", "souveraine", "etienne", "beaulieu"]
usedLetters = ["a", "w", b", r"]
usedLettersBad = ["a", "b"]


def get_probs(c_):
    probs = []
    
    
    #Generate Sublist
    subList = []
    
    for s in (wordList) :
        if (len(s) == len(c_)) :
            areIn = True
            
            for i in range(len(c_)) :
                if (c_[i] != "") :
                    if (c_[i] != s[i]) :
                        areIn = False
                        break
                for j in range(len(usedLettersBad)) :
                    if (usedLettersBad[j] == s[i] ) :
                        areIn = False
                        break
                if (not areIn) :
                    break
                
                
            if (areIn) :
                subList.append(s)
                
    print("subList : ", subList)
    
    #Find Probs                
    for l in range(26) :
        c = chr(97+l)
        inUsed = False
        
        for i in range(len(usedLetters)):
            if (c == usedLetters[i]) :
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
            
    
            
    return probs

get_probs(["w", "", "r", ""])

