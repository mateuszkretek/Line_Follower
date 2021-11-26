import time

from machine import PWM
from machine import Pin

led = Pin(25, Pin.OUT)
stby_engine = Pin(12, Pin.OUT)
ina1 = Pin(13, Pin.OUT)
ina2 = Pin(14, Pin.OUT)
pwm_a = PWM(Pin(15))

inb1 = Pin(18, Pin.OUT)
inb2 = Pin(17, Pin.OUT)
pwm_b = PWM(Pin(16))

pwm_a.freq(1000)

led(1)


def right_engine_forward(duty):
	ina1.value(0)
	ina2.value(1)
	duty_16 = int((duty * 65536) / 100)
	pwm_a.duty_u16(duty_16)


def left_engine_forward(duty):
	inb1.value(0)
	inb2.value(1)
	duty_16 = int((duty * 65536) / 100)
	pwm_b.duty_u16(duty_16)


def stop_engine():
	ina1.value(0)
	ina2.value(0)
	inb1.value(0)
	inb2.value(0)
	pwm_a.duty_u16(0)
	pwm_b.duty_u16(0)


def test(port):
	counter = 0
	input_sensor = Pin(port, Pin.OUT)
	input_sensor(1)
	input_sensor.init(Pin.IN, Pin.PULL_DOWN)
	while input_sensor.value() == 1:
		counter = counter+1
	return counter

while True:
	#stby_engine(1)
	#input_sensor.value(1)
	#right_engine_forward(50)
	#left_engine_forward(40)
	#time.sleep(1)
	#stop_engine()
	#time.sleep(2)
	#print("19", test(19))
	#print("20", test(20))
	#print("21", test(21))
	print(test(19))
	time.sleep(1)
	