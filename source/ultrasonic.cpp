#include "ultrasonic.h"

void initializeUltrasonic() {

    pinMode(US_TRIGGER_PIN, OUTPUT);
    pinMode(US_ECHO_PIN, INPUT);

}

long getUltrasonicOutput() {

    long duration;

    digitalWrite(US_TRIGGER_PIN, 0);
    delayMicroseconds(2);
    digitalWrite(US_TRIGGER_PIN, 1);
    delayMicroseconds(10);
    digitalWrite(US_TRIGGER_PIN, 0);
    
    duration = pulseIn(US_ECHO_PIN, 1);
    
    return duration;

}