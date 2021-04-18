
ArrayList<String> letters = new ArrayList<String>();

String[] list = { "word", "ludo", "anime", "violin"};

String toGuess;

String[] word;


int lives = 6;

void setup() {
  size(800, 800); 

  for (int i = 0; i < 26; i++) {
    letters.add(str(char(97+i)));
  }
  println(letters);

  toGuess = list[int(random(list.length))];
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
}


void keyPressed() {
  String guess = str(key);
  
  addLetter(guess);
  
  println(letters);
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

        break;
      } else {
        lives--;
      }
    }
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
