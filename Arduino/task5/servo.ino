#include<Servo.h>
Servo myservo;
void setup() {
  myservo.attach(9);

}

void loop() {

  for(int pos=30; pos <=90;pos+=1)
  {
    myservo.write(pos);
    delay(15);
  }
 
  for (int pos=90; pos>=30; pos-=1)
  {
    myservo.write(pos);
    delay(15);
  }
}
