from machine import PWM
from machine import Pin
import time

led = Pin(25, Pin.OUT)
standby_engine = Pin(12, Pin.OUT)

ina1 = Pin(13, Pin.OUT)
ina2 = Pin(14, Pin.OUT)
pwm_a = PWM(Pin(15))

inb1 = Pin(18, Pin.OUT)
inb2 = Pin(17, Pin.OUT)
pwm_b = PWM(Pin(16))

pwm_a.freq(1000)
pwm_b.freq(1000)

led(1)
standby_engine(1)


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


def sensor_test_with_counter(port):
	counter = 0
	input_sensor = Pin(port, Pin.OUT)
	input_sensor(1)
	input_sensor.init(Pin.IN, Pin.PULL_DOWN)
	while input_sensor.value() == 1:
		counter = counter+1
	return counter


def sensor_test_with_time(port):
	input_sensor = Pin(port, Pin.OUT)
	input_sensor(1)
	pulse_start = time.time()
	input_sensor.init(Pin.IN, Pin.PULL_DOWN)
	while input_sensor.value() > 0:
		pass
	if input_sensor.value() == 0:
		pulse_end = time.time()
	pulse_duration = pulse_end - pulse_start
	print(pulse_duration)
	

while True:
	if sensor_test_with_counter(20) > 2:
		stop_engine()
		left_engine_forward(40)
		right_engine_forward(40)
	if sensor_test_with_counter(19) > 2:
		stop_engine()
		left_engine_forward(40)
	if sensor_test_with_counter(21) > 2:
		stop_engine()
		right_engine_forward(40)
	