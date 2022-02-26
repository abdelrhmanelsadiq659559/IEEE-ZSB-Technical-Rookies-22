int trig=13;
int echo=12;
long duration;
int distance;



void setup() {
  pinMode(trig,OUTPUT);//send pusle
  pinMode(echo,INPUT);// recvive it
  Serial.begin(9600);

}

void loop() {
  digitalWrite(trig,LOW);
  delayMicroseconds(2);
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  duration=pulseIn(echo,HIGH);
  distance=duration*.034/2;
  if (distance >=10)
  {
    Serial.print("safe \n");
  }
  else 
  {
    Serial.print("too close \n");
  }


}
