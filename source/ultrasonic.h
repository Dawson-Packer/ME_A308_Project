#ifndef ULTRASONIC_H
#define ULTRASONIC_H
#include <arduino.h>
#include <HardwareSerial.h>

#define TRIGGER_PIN 7 /* Used to trigger a measurement */
#define ECHO_PIN 8 /* Output response of sensor */

/// @brief Initializes the ultrasonic sensor on pins 7 and 8
void initializeUltrasonic();

/// @brief Returns the distance seen by the ultrasonic sensor in centimeters.
/// @return The centimeters to the target.
long getUltrasonicOutput();

#endif