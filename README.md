# CCS811
Basic MicroPython driver for CCS811 connected over I2C.

Based on datasheet.
Tested with Adafruit CCS811 Air Quality Sensor Breakout. Remember to connect WAKE pin to ground.
Tested with NodeMCU and Wemos D1 mini with MicroPython v1.9.3-8-g63826ac5c ESP8266

The driver starts the sensor in operation mode 1: constant power mode, new measurement every second.
Call data_ready() to get new measurements.
See examples for usage.

Mode 0,2,3,4 are not yet implemented.
Temperature and humidity correction are also not yet implemented.
