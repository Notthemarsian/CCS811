"""Example usage basic driver CCS811.py"""

from machine import Pin, I2C
import time
import CCS811
import ssd1306


def main():
    # i2c bus with scl = D1 (GPIO5) and sda= D2 (GPIO4)
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    # CCS811 sensor s
    s = CCS811.CCS811(i2c)
    #Display d: Wemos Oled shield at 0x3c on i2c bus
    d = ssd1306.SSD1306_I2C(64,48,i2c,0x3c)
    time.sleep(1)
    while True:
        if s.data_ready():
            print('eCO2: %d ppm, TVOC: %d ppb' % (s.eCO2, s.tVOC))
            d.fill(0)
            d.text('eCO2 ppm',0,0)
            d.text(str(s.eCO2),0,10)
            d.text('TVOC ppb',0,20)
            d.text(str(s.tVOC),0,30)
            d.show()
            time.sleep(1)

main()
