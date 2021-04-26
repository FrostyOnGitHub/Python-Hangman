//Link genAlg to program
//make evolution



int pop = 10;
String[] list = { "word", "ludo", "char", "math", "food", "fogg"};



ArrayList<Gallow> gallows = new ArrayList<Gallow>();
ArrayList<Gallow> savedGallows = new ArrayList<Gallow>();

Gallow g;



void setup() {
  println("start");

  for (int i = 0; i < 32; i++) {
    print(97 + i, char(97+i), " ");
  }
  println();


  size(800, 800); 

  //g = new Gallow(null);


  for (int i = 0; i < pop; i++) {
    gallows.add(new Gallow(null));
  }

  //println(g.toGuess);


  g = new Gallow(null);

  //brain = new NeuralNetwork(32, 10, 5);
}


void draw() {
  background(50);

  g.show();

  g.checkWin();


  if (g.hanged()) {
    g.Setup();
  } else if (g.isWin()) {
    g.Setup();
    delay(1000);
  }

  for (int i = 0; i < gallows.size(); i++) { //Gallow g_ : gallows) {
    Gallow g_ = gallows.get(i);
    g_.think();
    //println("guess ", g_.makeGuess(), "lives ", g_.lives, "toGuess ", g_.toGuess, "score ", g_.score, "letters ", g_.letters);
    if (i == gallows.size()-1) {
      //println();  
    }
  }
  //println();

  for (int j = gallows.size()-1; j >= 0; j--) {
    if (gallows.get(j).hanged() || gallows.get(j).isWin()) {
      savedGallows.add(gallows.get(j));
      gallows.remove(j);
    }
  }
  
 if (gallows.size() == 0) {
    //println();
    //println();

    nextGeneration();
    println("next gen");
  }

  //println(gallows.size());
}



//---------------------------------------------------------//
//actions
void mousePressed() {

  //g.murderer = gallows.get(0).murderer;
  char ai = gallows.get(0).makeGuess();
  g.addLetter(str(ai));
  text(ai, width/2, height/2);
  //println(ai);
  //g.think();
  //println(gé


  if (mouseButton == RIGHT) {
    noLoop();
  } else {
    loop();
  }

 
}

void keyPressed() {
  String guess = str(key);

  g.addLetter(guess);

  println(g.letters);
  //makeGuess();
}






float letterToNeuron(char s) {
  float ascii = getAscii(s);
  float code = map(ascii, 97, 97+26, 0, 1);
  return code;
}

char NeuronToLetter(float[] f) {
  int s = 0;

  for (int i = 0; i < f.length; i++) {
    f[i] = 0.5 * (abs(f[i]-0.5)/(f[i]-0.5) + 1); 
    s += pow(2, i)*f[i];
  }
  //println(f);
  char answer = char(97+s);

  return answer;
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
