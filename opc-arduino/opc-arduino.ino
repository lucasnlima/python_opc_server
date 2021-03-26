#include<OPC.h>

OPCSerial arduinoOPC;

int velPin = 3;
int pontH1 = 2;
int pontH2 = 7;
int potPin = 0;
int ledPin = 13;
int var = 0;

int callback1(const char *itemID, const opcOperation opcOP, const int value){
  return analogRead(potPin);
}

int callback2(const char *itemID, const opcOperation opcOP, const int value){
  if (opcOP == opc_opwrite) {
    digitalWrite(velPin, value);
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pinMode(13, OUTPUT);
  pinMode(3, OUTPUT);  
  pinMode(2, OUTPUT);  
  pinMode(7, OUTPUT);
  pinMode(A0, INPUT);  
  
  arduinoOPC.setup();
  arduinoOPC.addItem("Ze.Int1",opc_read,opc_int,callback1);
  arduinoOPC.addItem("Ve.Int2",opc_read,opc_int,callback2);
}

void loop() {
  // put your main code here, to run repeatedly:
  var = analogRead(potPin)/8;
  //Serial.print("\n\r Velocidade:");
  //Serial.print(var);
  analogWrite(velPin,var);
  digitalWrite(pontH1,LOW);
  digitalWrite(pontH2,HIGH);
  digitalWrite(ledPin, HIGH);
  arduinoOPC.processOPCCommands();

}
