#include <arduino.h>
#include <HardwareSerial.h>
#include "ultrasonic.h"

void setup() {

    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600);

    initializeUltrasonic();
    
}

void loop() {

    float distance = getUltrasonicOutput();
    Serial.println(distance);

}