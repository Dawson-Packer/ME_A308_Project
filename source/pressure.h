#ifndef PRESSURE_H
#define PRESSURE_H
#include <Arduino.h>
#include "pinout.h"

#define ADC_RESOLUTION 1024
#define V_REF 5 /* Reference voltage is 5V */

/// @brief Initializes the pressure sensor by selecting the reference voltage. By default, this is
///        set to AVCC (power supply, 5V in our case). It can be set to INTERNAL for 1.1V or
///        EXTERNAL for another reference (this means we can substantially increase our resolution
///        by using smaller voltages, see `voltageOutPressureSensor`).
void initializePressureSensor();

/// @brief Returns the voltage value received from the pressure sensor via an Analog-Digital
///        converter pin. The formula is dependent on the reference voltage,
///        where `V_out = (V_ref / 1024) * ADC_value`
///        For a 5V reference (ours), the resolution is 0.00488 V.
/// @return The voltage out in Volts.
double voltageOutPressureSensor();

#endif