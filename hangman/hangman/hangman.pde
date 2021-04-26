//TODO
//IMPORT WORDS AND SEE IF OPTIMIZED ENOUGH


ArrayList<String> alphabet = new ArrayList<String>();
ArrayList<String> letters = new ArrayList<String>();
ArrayList<String> usedLettersGood = new ArrayList<String>();
ArrayList<String> usedLettersBad = new ArrayList<String>();
ArrayList<String> usedLetters = new ArrayList<String>();


String[] wordList = { "word", "ludo", "anime", "violin", "gene", "hill", "give", "goes", "gold", "gift"};

String toGuess;

String[] word;


int lives = 6;

void setup() {
  size(800, 800); 
  
  wordList = loadWords();

  for (int i = 0; i < 26; i++) {
    letters.add(str(char(97+i)));
    alphabet.add(str(char(97+i)));
  }
  println(letters);

  toGuess = wordList[int(random(wordList.length))];
  println(toGuess, toGuess.length());

  word = new String[toGuess.length()];

  for (int i = 0; i < toGuess.length(); i++) {
    word[i] = "";
  }
}


void draw() {
  background(50);

  textSize(100);
  stroke(255);
  for (int i = 0; i < toGuess.length(); i++) {
    //text(toGuess.charAt(i), 100 + i*100, height-110);  
    text(word[i], 100 + i*100, height-110);  
    line(110 + i*100, height - 100, 190 + i*100, height - 100);
  }


  checkWin();


  text(lives, 0, 100);
  //getUsed();
}

void mousePressed() {
  println("word ", word[0], "|", word[1], "|", word[2], "|", word[3]);
  float[] probs = getProbs(word);  
  float elt = max(probs);
  int idx = 0;
  for (int i = 0; i < probs.length; i++) {
    if (elt == probs[i]) {
      idx = i;
    }
  }
  char c = char(97+idx);
  println("guess ", c);

  addLetter(str(c));

  println();
}

void keyPressed() {
  String guess = str(key);

  addLetter(guess);
}

void addLetter(String guess) {
  for (int i = 0; i < letters.size(); i++) {
    if (letters.get(i).equals(guess)) {

      int placed = 0;
      for (int j = 0; j < toGuess.length(); j++) {
        if (guess.equals(str(toGuess.charAt(j)))) {
          word[j] = guess;
          placed ++;
        }
      }
      letters.remove(i);

      if (placed != 0) {
        usedLettersGood.add(guess);

        break;
      } else {
        usedLettersBad.add(guess);
        lives--;
      }
    }
    usedLetters.add(guess);
  }
}

void checkWin() {
  boolean b = true;
  for (int i = 0; i < toGuess.length(); i++) {
    if (!word[i].equals(str(toGuess.charAt(i)))) {
      b = false;
    }
  }

  if (b) {
    text("win!", width/2, height/2);
  }

  if (lives <= 0) {
    text("lose!", width/2, height/2);
  }
}

//void getUsed() {
//  usedLetters.clear();

//  for (int i = 0; i < alphabet.size(); i++) {
//    boolean isUsed = false;

//    for (int j = 0; j < letters.size(); j++) {
//      //println("debug 121 ", alphabet.get(i), letters.get(j));
//      if (letters.get(j).equals(alphabet.get(i))) { //bc every letter is in alpha
//        isUsed = true;
//      }
//    } 
//    if (!isUsed) {
//      usedLetters.add(alphabet.get(i));
//    }
//  }
//}
