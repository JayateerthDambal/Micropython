from machine import PWM
led = PWM(4, freq = 1000, duty=512)   # frequency ranges upto 1Hz and Duty scycle of 512

for i in range(0,511, 5):
    led.duty(i)
    print(i)

for i in range(510,-5, -5):
    led.duty(i)
    print(i)

led.deinit()   ### Deinitialises the process

