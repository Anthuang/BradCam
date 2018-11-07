import RPi.GPIO as GPIO
import time
import threading


class DistanceSensor:
    def __init__(self):
        self.beeping = False
        self.paused = False

        # GPIO Mode
        GPIO.setmode(GPIO.BOARD)

        # Set GPIO Pins
        self.PIN_TRIGGER = 5
        self.PIN_ECHO = 3
        self.PIN_LED = 7

        # Set GPIO direction (IN / OUT)
        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(self.PIN_ECHO, GPIO.IN)
        GPIO.setup(self.PIN_LED, GPIO.OUT)
        GPIO.output(self.PIN_LED, GPIO.LOW)
        print("Done setting up")

    def triggerSensor(self):
        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

        time.sleep(0.001)

        GPIO.output(self.PIN_TRIGGER, True)

        time.sleep(0.00001)

        GPIO.output(self.PIN_TRIGGER, False)

    def beep(self, delay):
        if not self.beeping:
            self.beeping = True
            for _ in range(3):
                GPIO.output(self.PIN_LED, GPIO.HIGH)
                time.sleep(delay)
                GPIO.output(self.PIN_LED, GPIO.LOW)
        self.beeping = False

    def start(self):
        self.paused = False

        run_thread = threading.Thread(target=self.run)
        run_thread.start()

    def run(self):
        print("Sensor running")
        while True:
            if self.paused:
                print("Sensor paused")
                return

            pulse_start_time = time.time()
            pulse_end_time = time.time()
            self.triggerSensor()
            while GPIO.input(self.PIN_ECHO) == 0:
                pulse_start_time = time.time()
            while GPIO.input(self.PIN_ECHO) == 1:
                pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time

            distance = pulse_duration * 34300 / 2

            if distance <= 50:
                self.beep(0.01)
            elif distance <= 100:
                self.beep(0.1)
            elif distance <= 200:
                self.beep(0.25)

            time.sleep(0.1)

    def pause(self):
        self.paused = True

    def stop(self):
        GPIO.cleanup()


def main():
    distance_sensor = DistanceSensor()

    try:
        distance_sensor.run()
    finally:
        distance_sensor.stop()


if __name__ == '__main__':
    main()
