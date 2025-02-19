#include <arduino.h>
#include <HardwareSerial.h>
#include "ultrasonic.h"

void setup() {

    /* Enables the led pin as an output and turns it on */
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, 1);

    /* Initializes the Serial connection */
    Serial.begin(9600);

    /* Initialize sensors */
    initializeUltrasonic();
    
}

void loop() {

    long us_distance = getUltrasonicOutput();
    
    Serial.print("US: ");
    Serial.print(us_distance);

    Serial.print("P: ");
    // TODO: get pressure reading

    Serial.print("F: ");
    // TODO: get float reading

    Serial.print('\n');

}