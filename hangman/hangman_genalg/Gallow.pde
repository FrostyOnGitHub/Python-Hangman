class Gallow {
  int lives = 6;


  float score;
  float fitness;

  ArrayList<String> letters = new ArrayList<String>();
  String toGuess;
  String[] word;

  NeuralNetwork murderer;

  Gallow(NeuralNetwork brein) {

    for (int i = 0; i < 26; i++) {
      letters.add(str(char(97+i)));
    }

    toGuess = list[int(random(list.length))];

    word = new String[toGuess.length()];
    for (int i = 0; i < toGuess.length(); i++) {
      word[i] = " ";
    }



    if (brein != null) {
      this.murderer = brein.Copy();
    } else {
      this.murderer = new NeuralNetwork(32, 10, 5);
    } 
    this.score = 0;
    this.fitness = 0;
  }

  void show() {
    textSize(100);
    stroke(255);
    for (int i = 0; i < toGuess.length(); i++) {
      //text(toGuess.charAt(i), 100 + i*100, height-110);  
      text(word[i], 100 + i*100, height-110);  
      line(110 + i*100, height - 100, 190 + i*100, height - 100);
    }

    text(lives, 0, 100);
  }

  //---------------------------------------------------------//
  //game logic
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

        if (placed != 0) {
          score ++;
          letters.remove(i);
          return;
        } else {
          lives--;
          letters.remove(i);
          return;
        }
      }
    }
    lives--;
  }

  boolean isWin() {
    for (int i = 0; i < toGuess.length(); i++) {
      if (!word[i].equals(str(toGuess.charAt(i)))) {
        return false;
      }
    }
    return true;
  }

  void checkWin() {
    boolean b = isWin();

    if (b) {
      text("win!", width/2, height/2);
    }

    if (lives <= 0) {
      text("lose!", width/2, height/2);
    }
  }


  boolean hanged() {
    if (lives == 0) {
      return true;
    } else {
      return false;
    }
  }

  void Setup() {
    lives = 6;
    letters.clear();
    for (int i = 0; i < 26; i++) {
      letters.add(str(char(97+i)));
    }

    toGuess = list[int(random(list.length))];

    word = new String[toGuess.length()];
    for (int i = 0; i < toGuess.length(); i++) {
      word[i] = " ";
    }
    println("setup");
  }


  //---------------------------------------------------------//
  //  NN functions

  void mutate() { 
    murderer.Mutate(0.1);
  }



  void think() {//String[] word_, String[] letters_) {
    //float[] data = new float[32];
    //for (int i = 0; i < 26; i++) {
    //  if (eltInList(str(char(97+i)), letters)) {
    //    data[i] = 0.5;
    //  } else if (eltInArr(str(char(97+i)), word)) {
    //    data[i] = 1;
    //  } else {
    //    data[i] = 0;
    //  }
    //}
    String q = str(makeGuess());
    addLetter(q);
    //println(q);
  }


  float[] getInputs() {
    float[] data = new float[32];
    for (int i = 0; i < 26; i++) {
      if (eltInList(str(char(97+i)), letters)) {
        data[i] = 0.5;
      } else if (eltInArr(str(char(97+i)), word)) {
        data[i] = 1;
      } else {
        data[i] = 0;
      }
    }


    for (int i = 0; i < 5; i++) {
      if (i < word.length) {
        if (word[i].equals("")) {
          data[26+i] = 1;
        } else {
          data[26+i] = letterToNeuron(word[i].charAt(0));
        }
      } else {
        data[26+i] = -1;
      }
    }
    return data;
  }


  char makeGuess() {
    float[] inputs = getInputs();

    //println(inputs);

    float[] guess = murderer.feedforward(inputs);

    //println();
    //println(guess);
    char c = NeuronToLetter(guess);
    //printArray(guess);
    //println( " ", c);
    //println(" ", toGuess);
    return c;
  }
}
