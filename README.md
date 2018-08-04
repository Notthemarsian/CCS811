# CCS811
Basic MicroPython driver for ams CCS811 sensor connected over I2C.

The ams CCS811 is a digital metal oxide gas sensor which detects a wide range of volatile organic compounds.
The sensor outputs a Total VOC value in ppb and an equivalent CO2 level in ppm.

Driver based on datasheet.
Tested with Adafruit CCS811 Air Quality Sensor Breakout (i2c addr = 90 / 0x5A; alternative addr = 91 / 0x5B). Remember to connect WAKE pin to ground.
Tested with both NodeMCU and Wemos D1 mini with MicroPython version v1.9.3-8-g63826ac5c ESP8266.
(Sparkfun CCS811 Air Quality Breakout has default address 91 (0x5B)).

Define sensor c:   c = CCS811.CCS811(i2c=i2c,addr=90)

The driver starts the sensor in operation mode 1: constant power mode, new measurement every second.
Mode 0,2,3,4 are not implemented.
The sensor has to run for 20 minutes before accurate readings are generated (the resistance has to stabilise). ams advises to run the sensor for 48 hours when new (see burn-in period in datasheet).

Call c.data_ready() to get new measurements.
See example.py for usage.

The sensor readings seem to drift a lot with temperature and humidity changes. Compensation data can be written to the sensor with the function c.put_envdata(humidity=h,temp=t) and this improves stability. 
See exampleTcorrection.py for usage. The example uses a Bosch BME280 sensor to measure temperature and humidity (BME280 driver from catdog2) and writes this data to the ENV_DATA register.

Manual Baseline Correction:
The resistance varies from sensor to sensor and over time. A baseline is maintained by the software (internal Automatic Baseline Correction). It is possible to retrieve and later restore this baseline (e.g. save a baseline when operating in clean air).
The baseline can be retrieved from the BASELINE register. It is a two-byte read/write register which contains an encoded version of the current baseline used in Algorithm Calculations. These two bytes can be read with x,y = c.get_baseline(). This baseline can be saved and written back to the register with c.put_baseline(HB=x,LB=y). The Algorithms will use the new value in its calculations (until it adjusts it as part of its internal Automatic Baseline Correction). The baseline should only be retrieved or restored when the resistance is stable (typically earliest after 20-30 minutes operation - see datasheet).
