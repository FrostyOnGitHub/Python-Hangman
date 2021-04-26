ArrayList<String> letters = new ArrayList<String>();
String[] list = { "word", "ludo", "char", "math"};
String toGuess;
String[] word;

float[][][] training_data;

NeuralNetwork brain;

int lives = 6;

void setup() {
  size(800, 800); 
  
  //training_data = prepareData();

  for (int i = 0; i < 26; i++) {
    letters.add(str(char(97+i)));
  }
  toGuess = list[int(random(list.length))];
  println(toGuess, toGuess.length());
  word = new String[toGuess.length()];
  for (int i = 0; i < toGuess.length(); i++) {
    word[i] = "";
  }


  brain = new NeuralNetwork(32, 10, 1);

  prepareData();
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



//---------------------------------------------------------//
//  NN functions
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

  println(inputs);

  float[] guess = brain.feedforward(inputs);

  println();
  println(guess);

  println(NeuronToLetter(guess[0]));
  return NeuronToLetter(guess[0]);
}

float letterToNeuron(char s) {
  float ascii = getAscii(s);
  float code = map(ascii, 97, 97+26, 0, 1);
  return code;
}

char NeuronToLetter(float n) {//float[] f) {
  //int s = 0;

  //for (int i = 0; i < f.length; i++) {
  //  f[i] = 0.5 * (abs(f[i]-0.5)/(f[i]-0.5) + 1); 
  //  s += pow(2, i)*f[i];
  //}
  ////println(f);
  //char answer = char(97+s);
  
  float a = map(n, 0,1, 97,127);
  char answer = char(int(a));

  return answer;
}

void prepareData() { //float[][][]
  String[] inputs = new String[list.length * 4];
  char[] target = new char[list.length * 4];
  for (int i = 0; i < list.length; i++) {
    for (int j = 0; j < list[i].length(); j++) {
      inputs[i*list[i].length()+j] = list[i].replace(list[i].charAt(j), char(32)); 
      target[i*list[i].length()+j] = list[i].charAt(j);
    }
  }
  for (int i = 0; i < inputs.length; i++) {
    println(inputs[i], " -> ", target[i]);
  }
  

  //return 1;
}



//void trainEpoch() {

//  for (int i = 0; i < training.length; i++) {

//      brain.train(
//  }
//}





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
      letters.remove(i);

      if (placed != 0) {

        break;
      } else {
        //lives--;
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


//---------------------------------------------------------//
//actions
void mousePressed() {
  char ai = makeGuess();
  addLetter(str(ai));
  println(ai);
}

void keyPressed() {
  String guess = str(key);

  addLetter(guess);

  println(letters);
  makeGuess();
}




//---------------------------------------------------------//
// conversion and other
int getAscii(char c) {
  for (int i = 97; i < 97+26; i++) {
    if (char(i) == c) {
      return i;
    }
  } 
  return 0;
}

boolean charInStr(String s, char c) {
  for (int i = 0; i < s.length(); i++) {
    if (s.charAt(i) == c) {
      return true;
    }
  }
  return false;
}

boolean eltInList(String s, ArrayList<String> l) {
  for (int i = 0; i < l.size(); i++) {
    if (l.get(i).equals(s)) {
      return true;
    }
  }
  return false;
}

boolean eltInArr(String s, String[] l) {
  for (int i = 0; i < l.length; i++) {
    if (l[i].equals(s)) {
      return true;
    }
  }
  return false;
}
