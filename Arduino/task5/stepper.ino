#include<Stepper.h>
int steps =100;
byte in1 =10;
byte in2=11;
byte in3=12;
byte in4=13;
Stepper stepper(steps,in1,in3,in2,in4);

void setup() {
}

void loop() {
 stepper.setSpeed(5);
 stepper.step(100);
 stepper.setSpeed(10);
 stepper.step(-100);
 delay(1000);
}
