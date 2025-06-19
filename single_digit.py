'''
Gemma McLean
May 2025
Script to showcase basic functionality of a single connected DIGIT sensor.
Based on https://github.com/facebookresearch/digit-interface
'''

# Imports
from digit_interface.digit import Digit
from digit_interface.digit_handler import DigitHandler


# Pause the program and wait for a key press
def pause():
    input("Press a key to continue...")


# Get a list of connected DIGIT sensors
digits = DigitHandler.list_digits()

# Print name and serial numbers
for digit in digits:
    print(f"DIGIT detected at {digit['dev_name']} with serial number {digit['serial']}.")

pause()

# If a DIGIT is connected
if len(digits) > 0:
    # Get the serial number for the DIGIT device
    serial = digits[0]['serial']

    # Connect to DIGIT
    digit = Digit(serial, "Single_Digit")
    digit.connect()

    # Print basic info
    print(digit.info())

    pause()

    # Print possible streams
    print("Possible streams:")
    print(Digit.STREAMS)

    # Print min and max intensity
    print(f"Min intensity: {Digit.LIGHTING_MIN}")
    print(f"Max intensity: {Digit.LIGHTING_MAX}")

    pause()

    # Set stream resolution and fps
    fps_30 = Digit.STREAMS['QVGA']['fps']['30fps']
    digit.set_fps(fps_30)

    # Set lighting intensity
    digit.set_intensity(12)

    print("Set stream resolution, fps and light intensity.")

    # Print basic info again
    print(digit.info())

    pause()

    # Show Open CV live view
    print("Showing live view. Hit ESC to close window.")
    digit.show_view()

    num_frames = 10
    # Save frames to disk
    print("Saving frames")
    for i in range(num_frames):
        # Save single frame from DIGIT
        frame = digit.get_frame()
        digit.save_frame(f"frame_{i}.jpg")
    print("Done!")

    # Disconnect DIGIT
    digit.disconnect()

else:
    print("No DIGITS found.")
