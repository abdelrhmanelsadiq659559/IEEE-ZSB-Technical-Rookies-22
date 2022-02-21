//senors
int rightIR=12;
int leftIR=13;
// motor a 
int ena =9;
int inp1=11;
int inp2=10;
// motor b 
int enb =6;
int inp3=4;
int inp4=3;


void setup() {
  //senor
  pinMode(rightIR,INPUT);
  pinMode(leftIR,INPUT);
  pinMode(ena,OUTPUT);
  pinMode(inp1,OUTPUT);
  pinMode(inp2,OUTPUT);
  pinMode(inp3,OUTPUT);
  pinMode(enb,OUTPUT);
  pinMode(inp4,OUTPUT);
}

void loop() {
  int readright=digitalRead(rightIR);
  int readleft=digitalRead(leftIR);
  
  if (readright==LOW&&readleft==LOW)//on white in clock 
  {
    analogWrite(ena,255);
    analogWrite(enb,255);
    digitalWrite(inp1,HIGH); 
    digitalWrite(inp2,LOW);

    digitalWrite(inp3,LOW);
    digitalWrite(inp4,HIGH);
    
  }
  
  
   else if (readright==HIGH&&readleft==LOW)
   {

     analogWrite(ena,255);
    analogWrite(enb,255);
    digitalWrite(inp1,LOW); 
    digitalWrite(inp2,HIGH);

    digitalWrite(inp3,LOW);
    digitalWrite(inp4,HIGH);
  }
  else if (readright==LOW&&readleft==HIGH)//right on white 
  {
    digitalWrite(inp1,HIGH); 
    digitalWrite(inp2,LOW);

    digitalWrite(inp3,HIGH);
    digitalWrite(inp4,LOW);
   
  }
  else if (readright==HIGH&&readleft==HIGH)
   {
   analogWrite(ena,255);
    analogWrite(enb,255);
    digitalWrite(inp1,LOW); 
    digitalWrite(inp2,LOW);
    digitalWrite(inp3,LOW);
    digitalWrite(inp4,LOW);

  }




  delay(250);
  
  
}
