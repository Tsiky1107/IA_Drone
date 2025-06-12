#include <Arduino.h>


void setup() {
  // put your setup code here, to run once:
  pinMode(7, OUTPUT);
  Serial.begin(9600);
  digitalWrite(7, HIGH);
}


int calculVitesseMoyenne(){
  // Fonction qui donne la vitesse des moteurs
  int v1 = 1;//Vitesse du moteur 1
  int v2 = 1;
  int v3 = 1;
  int v4 = 1;

  int v_moyenne = (v1 + v2 + v3 + v4) / 4;
  return v_moyenne;
}

void loop() {

  //Detection marquage
  if(Serial.available() > 0){
    String data = Serial.readStringUntil("\n");
    // Serial.println(data);

    if(data){
      digitalWrite(7, LOW); //Pompe a eau en marche.0à)0"
      delay(500);
    }
    else{
      digitalWrite(7, HIGH);
      delay(500);
    }
  } else{
      digitalWrite(7, HIGH);
      delay(500);
    }

  //Affichage vitesse
  Serial.print(calculVitesseMoyenne());
  Serial.print(" ");
  // delay(500);
  Serial.println(74);
  delay(500);
}