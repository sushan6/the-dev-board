from machine import Pin
import time

# Initialize onboard LED (adjust pin number based on your schematic, e.g., pin 25 for Raspberry Pi Pico)
led = Pin(25, Pin.OUT)

# Initialize user tactile switch / button if connected to a specific GPIO (e.g., Pin 9)
# Adjust the pin number to match your actual schematic design
button = Pin(9, Pin.IN, Pin.PULL_UP)

print("RP2040 Custom Board Firmware Initialized Successfully!")

while True:
    # Check if the tactile switch is pressed (Active Low with pull-up)
    if button.value() == 0:
        print("Button pressed! Fast blinking...")
        for _ in range(5):
            led.toggle()
            time.sleep(0.1)
    else:
        # Standard heartbeat blink
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)