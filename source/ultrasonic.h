#ifndef ULTRASONIC_H
#define ULTRASONIC_H
#include <arduino.h>
#include <HardwareSerial.h>
#include "pinout.h"

/// @brief Initializes the ultrasonic sensor on pins 7 and 8
void initializeUltrasonic();

/// @brief Returns the distance seen by the ultrasonic sensor in centimeters.
/// @return The microseconds to the target and back.
long getUltrasonicOutput();

#endif