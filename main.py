from machine import PWM
from machine import Pin
import time

led = Pin(25, Pin.OUT)

#motor controller standby port
standby_engine = Pin(12, Pin.OUT)

#motor_a ports
ina1 = Pin(13, Pin.OUT)
ina2 = Pin(14, Pin.OUT)
pwm_a = PWM(Pin(15))

#motor_b ports
inb1 = Pin(18, Pin.OUT)
inb2 = Pin(17, Pin.OUT)
pwm_b = PWM(Pin(16))

#sensor ports
sensor_1 = 19
sensor_2 = 20
sensor_3 = 21

led(1)
standby_engine(1)

pwm_a.freq(10000)
pwm_b.freq(10000)

#in



def left_motor_forward(duty):
	inb1.value(0)
	inb2.value(1)
	duty_16 = int((duty * 65536) / 100)
	pwm_b.duty_u16(duty_16)
	

def left_motor_backward(duty):
	inb1.value(1)
	inb2.value(0)
	duty_16 = int((duty * 65536) / 100)
	pwm_b.duty_u16(duty_16)

def stop_left_motor():
	ina1.value(0)
	ina2.value(0)
	pwm_a.duty_u16(0)
	

def right_motor_forward(duty):
	ina1.value(0)
	ina2.value(1)
	duty_16 = int((duty * 65536) / 100)
	pwm_a.duty_u16(duty_16)
	
def right_motor_backward(duty):
	ina1.value(1)
	ina2.value(0)
	duty_16 = int((duty * 65536) / 100)
	pwm_a.duty_u16(duty_16)

def stop_right_motor():
	inb1.value(0)
	inb2.value(0)
	pwm_b.duty_u16(0)


def sensor_test_with_counter(port):
	counter = 0
	input_sensor = Pin(port, Pin.OUT)
	input_sensor(1)
	time.sleep(0.01)
	input_sensor.init(Pin.IN, Pin.PULL_DOWN)
	while input_sensor.value() == 1:
		counter = counter+1
	print(port, counter)
	return counter


#def sensor_test_with_time(port):
#	input_sensor = Pin(port, Pin.OUT)
#	input_sensor(1)
#	pulse_start = time.time_ns()
#	input_sensor.init(Pin.IN, Pin.PULL_DOWN)
#	while input_sensor.value() > 0:
#		time.sleep(0.00001)
#	if input_sensor.value() == 0:
#		pulse_end = time.time_ns()
#	pulse_duration = pulse_end - pulse_start
#	return pulse_duration
	

while True:
	if sensor_test_with_counter(20) > 4:
	#	print("middle")
		left_motor_forward(25)
		right_motor_forward(25)
		continue
	if sensor_test_with_counter(19) > 4:
	#	print("right")
		right_motor_backward(25)
		left_motor_forward(50)
		continue
	if sensor_test_with_counter(21) > 4:
	#	print("left")
		left_motor_backward(25)
		right_motor_forward(50)
		continue
	#else:
	#	stop_left_motor()
	#	stop_right_motor()
	