#ifndef VALVE_H
#define VALVE_H
#include <Stepper.h>
#include "pinout.h"

#define STEPS_PER_REV 1024
#define STEPPER_SPEED 30
#define STEPS_TO_CLOSED STEPS_PER_REV * 15

extern float valveOpenPercentage;

extern Stepper valveMotor;

void initializeValveMotor();

int valveSetOpenPercentage(float percentage);

#endif