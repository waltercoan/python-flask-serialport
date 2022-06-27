
const unsigned int MAXMSG = 13;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  while(Serial.available() > 0){
      static char message[MAXMSG];
      static char valtwobytes[3];
      static unsigned int message_pos=0;

      char inbyte = Serial.read();
      if (inbyte != '\n' && (message_pos < MAXMSG-1)){
        message[message_pos] = inbyte;
        message_pos++;
      }else{
        message[message_pos] = '\0';
        Serial.println(message);
        for(int i=0;i<message_pos;i++){
           valtwobytes[i % 2] = message[i];
           if(i % 2 == 1){
              valtwobytes[2] = '\0';
              int valorint = atoi(valtwobytes);
              Serial.print("valorint: ");
              Serial.println(valorint);
           }
        }
        message_pos = 0;
      }
  }

}