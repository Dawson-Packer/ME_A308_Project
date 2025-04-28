#include <arduino.h>
#include <HardwareSerial.h>
#include "ultrasonic.h"
#include "pressure.h"
#include "float.h"
#include "valve.h"

static bool is_filling = false;

void setup() {

    /* Initializes the Serial connection */
    Serial.begin(9600);

    /* Initialize sensors */
    initializeUltrasonic();

    /* Initialize valve motor */
    initializeValveMotor();

}


void loop() {

    delay(100); // originally 100

    // long ultrasonic_microseconds = microsecondsUltrasonic();
    double pressure_voltage = voltageOutPressureSensor();
    float float_voltage = voltageOutFloatSensor();
    long current_time = millis();
    
    Serial.print("T: ");
    Serial.print(current_time);

    // Serial.print(" US: ");
    // Serial.print(ultrasonic_microseconds);

    Serial.print(" P: ");
    Serial.print(pressure_voltage, 5);
    // Serial.print(" P: ");
    // Serial.print(0.0, 5);

    Serial.print(" F: ");
    Serial.print(float_voltage, 5);

    Serial.print('\n');
}