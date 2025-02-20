#include "ultrasonic.h"

void initializeUltrasonic() {

    pinMode(TRIGGER_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);

}

long getUltrasonicOutput() {

    long duration;

    digitalWrite(TRIGGER_PIN, 0);
    delayMicroseconds(2);
    digitalWrite(TRIGGER_PIN, 1);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_PIN, 0);

    duration = pulseIn(ECHO_PIN, 1);
    
    return duration;

}