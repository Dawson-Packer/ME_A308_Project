#include "pressure.h"

void initializePressureSensor() {

    /* Sets V_ref to AVCC (5V for us) TODO: Look into using internal/external for better resolution */
    analogReference(DEFAULT);
}

double voltageOutPressureSensor() {

    int adc_output = analogRead(P_ADC_PIN);

    return ((double)V_REF / (double)ADC_RESOLUTION) * (double)adc_output;
}