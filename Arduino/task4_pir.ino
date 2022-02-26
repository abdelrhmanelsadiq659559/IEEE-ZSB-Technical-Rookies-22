
int pir =5;
int reading;
void setup() {
 pinMode(pir,INPUT);
 Serial.begin(9600);

}

void loop() {
  
reading=digitalRead(pir);
if (reading==1)
{
  Serial.println("human are detected  ");
}


}
