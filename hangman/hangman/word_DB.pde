
String[] loadWords() {
  String[] Words = loadStrings("word_DB.txt");
  ArrayList<String> words = new ArrayList<String>();
  for (int i = 0; i < Words.length; i++) {
    if (Words[i].indexOf("-") == -1 && Words[i].length() > 4) {
      words.add(Words[i]);
    }
  }
  
  
  String[] word_list = new String[words.size()];
  
  for (int i = 0; i < words.size(); i++) {
    word_list[i] = words.get(i);  
  }
  
  return word_list;
}
