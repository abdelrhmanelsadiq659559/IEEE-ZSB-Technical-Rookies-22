// motor a
int enba=9;
int inp1=7;
int inp2=6;
// motor b 
int enbb=11;
int inp3=5;
int inp4=4;


void setup() 
{
 pinMode(enba,OUTPUT);
 pinMode(inp1,OUTPUT);
 pinMode(inp2,OUTPUT);
 pinMode(enbb,OUTPUT);
 pinMode(inp3,OUTPUT);
 pinMode(inp4,OUTPUT);
}
void work ()
{
  ///motor a in clock 
  digitalWrite(inp1,HIGH);
  digitalWrite(inp2,LOW);
  analogWrite(enba,255);
  //motor b in clock
  digitalWrite(inp3,LOW);
  digitalWrite(inp4,HIGH);
  analogWrite(enbb,255);
  delay(2000);

  ///change the directions
  digitalWrite(inp1,LOW);
  digitalWrite(inp2,HIGH);
  digitalWrite(inp3,HIGH);
  digitalWrite(inp4,LOW);
  delay(2000);
  // off the motors 
  
  digitalWrite(inp1,LOW);
  digitalWrite(inp2,LOW);
  digitalWrite(inp3,LOW);
  digitalWrite(inp4,LOW);
  
}

void loop() {
  work();
}
