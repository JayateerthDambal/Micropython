from machine import Pin, I2C
import ssd1306
from time import sleep


i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64

display = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

display.text("Hello ", 10, 20, 1)
display.show()
