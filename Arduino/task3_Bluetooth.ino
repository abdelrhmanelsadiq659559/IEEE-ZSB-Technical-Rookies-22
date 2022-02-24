//motor a
int ena=9;
int in1=8;
int in2=7;
//motor a
int enb=3;
int in3=5;
int in4=6;
char state ='S';
void setup() {
  pinMode(ena,OUTPUT);
  pinMode(in1,OUTPUT);
  pinMode(in2,OUTPUT);
  pinMode(enb,OUTPUT);
  pinMode(in3,OUTPUT);
  pinMode(in4,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  analogWrite(enb,255);
  analogWrite(ena,255);
  if(Serial.available()>0)
  {
   state=Serial.read();
    }
  switch (state)
  {
    case 'S':  // stop
    digitalWrite(in1,LOW);
    digitalWrite(in2,LOW);
    digitalWrite(in3,LOW);
    digitalWrite(in4,LOW);
    break;
    case 'F': // move forward
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);
    break;
    case 'B': // move backward
    digitalWrite(in1,LOW);
    digitalWrite(in2,HIGH);
    digitalWrite(in3,LOW);
    digitalWrite(in4,HIGH);
    break;

    case 'R': //move right
    digitalWrite(in1,LOW);
    digitalWrite(in2,HIGH);
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);
    break;

    case 'L': // move left 
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
    digitalWrite(in3,LOW);
    digitalWrite(in4,HIGH);
    break; 
  }

}
