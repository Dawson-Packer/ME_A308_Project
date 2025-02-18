#include <arduino.h>
#include <HardwareSerial.h>
#include "ultrasonic.h"

void setup() {

    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, 1);
    Serial.begin(9600);

    initializeUltrasonic();
    
}

void loop() {

    

    long distance = getUltrasonicOutput();
    Serial.println(distance);

}