#include "pressure.h"

void initializePressureSensor() {

    /* Sets V_ref to AVCC (5V for us) TODO: Look into using internal/external for better resolution */
    analogReference(DEFAULT);
}

float voltageOutPressureSensor() {

    int adc_output = analogRead(P_ADC_PIN);

    return ((float)V_REF / ADC_RESOLUTION) * (float)adc_output;
}