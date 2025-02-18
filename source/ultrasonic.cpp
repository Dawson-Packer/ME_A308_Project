#include "ultrasonic.h"

void initializeUltrasonic() {

    pinMode(TRIGGER_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);

}

float getUltrasonicOutput() {

    long duration;

    digitalWrite(TRIGGER_PIN, 0);
    delayMicroseconds(2);
    digitalWrite(TRIGGER_PIN, 1);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_PIN, 0);

    duration = pulseIn(ECHO_PIN, 1);
    
    return (static_cast<float>(duration) / 0.0033) / 2; /* Convert to meters */

}