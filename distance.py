import RPi.GPIO as GPIO
import time


class DistanceSensor:
    def __init__(self):
        # GPIO Mode
        GPIO.setmode(GPIO.BOARD)

        # Set GPIO Pins
        self.PIN_TRIGGER = 5
        self.PIN_ECHO = 3

        # Set GPIO direction (IN / OUT)
        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(self.PIN_ECHO, GPIO.IN)

        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

        time.sleep(2)

        GPIO.output(self.PIN_TRIGGER, True)

        time.sleep(0.00001)

        GPIO.output(self.PIN_TRIGGER, False)

    def run(self):
        while True:
            pulse_start_time = time.time()
            pulse_end_time = time.time()

            while GPIO.input(self.PIN_ECHO) == 0:
                pulse_start_time = time.time()
            while GPIO.input(self.PIN_ECHO) == 1:
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

    def cleanup(self):
        GPIO.cleanup()


def main():
    distance_sensor = DistanceSensor()

    try:
        distance_sensor.run()
    finally:
        distance_sensor.cleanup()


if __name__ == '__main__':
    main()
