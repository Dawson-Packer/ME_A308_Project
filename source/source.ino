#include <arduino.h>
#include <HardwareSerial.h>
#include "ultrasonic.h"
#include "pressure.h"
#include "float.h"

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

    long ultrasonic_microseconds = getUltrasonicOutput();

    float pressure_voltage = voltageOutPressureSensor();

    float float_voltage = voltageOutFloatSensor();
    
    Serial.print("US: ");
    Serial.print(ultrasonic_microseconds);

    Serial.print(" P: ");
    Serial.print(pressure_voltage);

    Serial.print(" F: ");
    Serial.print(float_voltage);

    Serial.print('\n');

}