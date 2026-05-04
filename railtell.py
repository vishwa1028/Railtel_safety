from gpiozero import DistanceSensor, Motor, Servo
from time import sleep

# Set up ultrasonic sensor
sensor = DistanceSensor(echo=18, trigger=23)

# Set up servo motor
servo = Servo(17)

# Set up DC motors
motor_left = Motor(forward=4, backward=14)
motor_right = Motor(forward=17, backward=18)

def measure_distance():
    # Return distance in centimeters
    return sensor.distance * 100

def turn_servo(angle):
    servo.value = angle
    sleep(1)

def left_distance():
    turn_servo(-0.5)
    sleep(1)
    return measure_distance()

def right_distance():
    turn_servo(0.5)
    sleep(1)
    return measure_distance()

def forward():
    motor_left.forward()
    motor_right.forward()

def turn_left():
    motor_left.backward()
    motor_right.forward()

def turn_right():
    motor_left.forward()
    motor_right.backward()

def stop():
    motor_left.stop()
    motor_right.stop()

try:
    while True:
        distance = measure_distance()
        print("Distance: {:.2f} cm".format(distance))

        if distance <= 20:
            stop()
            sleep(0.2)
            left_dist = left_distance()
            right_dist = right_distance()

            if left_dist >= right_dist:
                turn_left()
                sleep(0.2)
                stop()
            else:
                turn_right()
                sleep(0.2)
                stop()
        else:
            forward()
            print("Forward")
except KeyboardInterrupt:
    stop()
    servo.detach()
