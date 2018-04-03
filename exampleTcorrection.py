"""Example usage basic driver CCS811.py"""

from machine import Pin, I2C
import time
import CCS811, BME280
import ssd1306


def main():
    # i2c bus with scl = D1 (GPIO5) and sda= D2 (GPIO4)
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    # CCS811 sensor s
    s = CCS811.CCS811(i2c)
    # Bosch sensor b: BME280 humidity pressure temperature
    b = BME280.BME280(i2c=i2c)
    #Display d: Wemos Oled shield at 0x3c on i2c bus
    d = ssd1306.SSD1306_I2C(128,64,i2c,0x3c)
    time.sleep(1)
    while True:
        if s.data_ready():
            print('eCO2: %d ppm, TVOC: %d ppb' % (s.eCO2, s.tVOC), b.values)
            d.fill(0)
            d.text('eCO2',0,0)
            d.text(str(s.eCO2),40,0)
            d.text('ppm',100,0)
            d.text('TVOC',0,16)
            d.text(str(s.tVOC),40,16)
            d.text('ppb',100,16)
            r = b.read_compensated_data()
            t = r[0]/100
            p = r[1]/25600
            h = r[2]/1024
            d.text('T',0,26)
            d.text(str(t),40,26)
            d.text('*C',100,26)
            d.text('RH',0,36)
            d.text(str(h),40,36)
            d.text('%',100,36)
            d.text('P',0,46)
            d.text(str(p),40,46)
            d.text('hPa',100,46)
            #d.text(str(s.get_baseline()),0,46)
            x,y = s.get_baseline()
            d.text(str(x),0,56)
            d.text(str(y),32,56)
            d.show()
            s.put_envdata(humidity=h,temp=t)
            time.sleep(1)

main()
