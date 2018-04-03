# CCS811
Basic MicroPython driver for CCS811 connected over I2C.

Based on datasheet.
Tested with Adafruit CCS811 Air Quality Sensor Breakout. Remember to connect WAKE pin to ground.
Tested with NodeMCU and Wemos D1 mini with MicroPython v1.9.3-8-g63826ac5c ESP8266

The driver starts the sensor in operation mode 1: constant power mode, new measurement every second.
Mode 0,2,3,4 are not yet implemented.

Call data_ready() to get new measurements.
See examples for usage.

The sensor readings seem to drift a lot with temperature and humidity changes. Compensation data can be written to the sensor and this improves stability. 
See exampleTcorrection for usage. The example uses a Bosch BME280 sensor to measure temperature and humidity (BME280 driver from catdog2) and writes this data to the ENV_DATA register.
