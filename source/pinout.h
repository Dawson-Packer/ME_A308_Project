/**
 * This file names all the pins being used on the Arduino for the various peripherals.
 */

#ifndef PINOUT_H
#define PINOUT_H
#include <Arduino.h>

#define US_TRIGGER_PIN 7 /* Used to trigger a measurement */
#define US_ECHO_PIN 8 /* Output response of sensor */

/* Stepper motor control pins for valve */
#define V_STEP_PIN1 9
#define V_STEP_PIN2 10
#define V_STEP_PIN3 11
#define V_STEP_PIN4 12

/* Pressure and float sensor analog pins */
#define P_ADC_PIN A0
#define F_ADC_PIN A1

#endif