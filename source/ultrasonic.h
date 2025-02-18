#ifndef ULTRASONIC_H
#define ULTRASONIC_H
#include <arduino.h>
#include <HardwareSerial.h>

#define TRIGGER_PIN 7 /* Used to trigger a measurement */
#define ECHO_PIN 8 /* Output response of sensor */

void initializeUltrasonic();

float getUltrasonicOutput();

#endif