# Libraries
import RPi.GPIO as GPIO
import time


try:
    # GPIO Mode
    GPIO.setmode(GPIO.BOARD)

    # set GPIO Pins
    PIN_TRIGGER = 5
    PIN_ECHO = 3

    # set GPIO direction (IN / OUT)
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    print("Waiting for sensor to settle")

    time.sleep(2)

    print("Calculating distance")

    GPIO.output(PIN_TRIGGER, True)

    time.sleep(0.00001)

    GPIO.output(PIN_TRIGGER, False)

    while True:
        pulse_start_time = time.time()
        pulse_end_time = time.time()

        while GPIO.input(PIN_ECHO) == 0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time

        distance = pulse_duration * 34300 / 2

        if distance <= 50:
            print("BEEP BEEP BEEP")
        elif distance <= 100:
            print("BEEP BEEP")
        elif distance <= 200:
            print("BEEP")

        time.sleep(0.1)

finally:
    GPIO.cleanup()
