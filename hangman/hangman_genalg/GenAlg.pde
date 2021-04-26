void nextGeneration() {
  caclulateFitness();
  for (int i = 0; i < pop; i++) {
    gallows.add(pickOne());
  }
  savedGallows.clear();
}

Gallow pickOne() {
  int index = 0;
  float r = random(1);
  
  while (r > 0) {
    r -= savedGallows.get(index).fitness;
    index++;
  }
  index--;

  Gallow hanged = savedGallows.get(index);  //savedBirds.get(int(random(savedBirds.size())));
  Gallow child = new Gallow(hanged.murderer);
  child.murderer.Mutate(0.08);
  return child;
}

void caclulateFitness() {
  int totScore = 0;
  for (Gallow g_ : savedGallows) {
   g_.score = pow(g_.score,2);
  }
  for (Gallow g_ : savedGallows) {
    totScore += g_.score;
  }
  for (int i = 0; i < savedGallows.size(); i++) {//Gallow g_ : savedGallows) {
    Gallow g_ = savedGallows.get(i);
    g_.fitness = g_.score/totScore;
    println("fitness of ", i, ":", g_.fitness);
  }
}
