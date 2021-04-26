float[] getProbs(String[] c_) {
  float[] probs = new float[26];

  //-------------generate sublist-----------
  ArrayList<String> subList = new ArrayList<String>();
  for (String s : wordList) {
    if (s.length() == c_.length) { 
      boolean areIn = true;

      //for (int j = 0; j < c_.length; j++) {
      //  if (c_[j].length() > 0) {
      //    boolean isIn = false;
      //    for (int i = 0; i < s.length(); i++) {
      //      if (c_[j].charAt(0) == s.charAt(i)) {
      //        isIn = true;
      //        break;
      //      }
      //    }
      //    if (!isIn) {
      //      areIn = false;
      //      break;
      //    }
      //  }
      //}

      for (int i = 0; i < c_.length; i++) {
        if (!c_[i].equals("")) {
          if (!c_[i].equals(str(s.charAt(i)))) {
            areIn = false;
            break;
          }
        }
        for (int j = 0; j < usedLettersBad.size(); j++) { 
          if (usedLettersBad.get(j).equals(str(s.charAt(i)))){
            areIn = false;
            break;
          }
        }
        if (!areIn) {
          break;
        }
      }


      if (areIn) {
        subList.add(s);
      }
    }
  }
  println("sList ", subList);


  //------------Find prob---------------
  for (int l = 0; l < 26; l++) {
    char c = char(97+l);
    boolean inUsed = false;
    for (int i = 0; i < usedLetters.size(); i++) {
      if (str(c).equals(usedLetters.get(i))) {
        inUsed = true;
      }
    }
    if (!inUsed) {

      int nbWord = 0;
      for (String s : subList) {
        for (int i = 0; i < s.length(); i++) {
          if (c == s.charAt(i)) {
            nbWord++;
          }
        }
      }

      probs[l] = nbWord*1.0 / subList.size();
    }
  }

  for (int p = 0; p < 26; p++) {
    print(char(97+p), probs[p], " ");
  }
  println();


  return probs;
}
