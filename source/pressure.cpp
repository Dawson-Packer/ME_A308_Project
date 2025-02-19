#include "pressure.h"
#include <avr/interrupt.h>

void initializePressureSensor() {

    /* Sets V_ref to AVCC (5V for us) TODO: Look into using internal/external for better resolution */
    analogReference(DEFAULT);
}

float voltageOutPressureSensor() {

    int voltage_reading = analogRead(ADC_PIN);
    
    return ((float)V_REF / 1024.0) * (float)voltage_reading;
}