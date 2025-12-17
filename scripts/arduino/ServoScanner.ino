// Josh
// 12/12/2020
#include <Servo.h>
Servo myservo;
unsigned long previousMillis = 0;
const long interval = 30;  // interval at which to increase the variable (milliseconds)
int counter = 0;
bool backwards = false;

void setup(){
  Serial.begin(9600);  // Initialize Serial Monitor
  myservo.attach(9);
  myservo.write(90);// move servos to center position -> 90°
}
 
void loop(){ 
  myservo.write(counter);// move servos
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    if (!backwards) {
      counter++; // if backwards is fale
    } else {
      counter--;
    } 
    Serial.println(counter);  // Print the value
  }
  if (counter >= 180) {
    backwards = true;
  }
  if (counter <= 0) {
    backwards = false;
  }
}