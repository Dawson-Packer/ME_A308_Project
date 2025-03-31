#include "valve.h"

float valveOpenPercentage = 0.0;

Stepper valveMotor = Stepper(STEPS_PER_REV, V_STEP_PIN1, V_STEP_PIN3, V_STEP_PIN2, V_STEP_PIN4);

void initializeValveMotor() {

    valveMotor.setSpeed(STEPPER_SPEED);
}

int valveSetOpenPercentage(float percentage) {

    int steps_to_turn = (int)(STEPS_TO_CLOSED * (percentage - valveOpenPercentage));
    valveOpenPercentage = percentage;

    valveMotor.step(steps_to_turn);
    return steps_to_turn;
}