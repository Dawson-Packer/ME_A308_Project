#include <arduino.h>
#include <HardwareSerial.h>
#include "ultrasonic.h"

static int count = 0;

void setup() {

    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600);

    initializeUltrasonic();
    
}

void loop() {

    long distance = getUltrasonicOutput();
    Serial.println(distance);

}