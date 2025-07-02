"""
Author: Gemma McLean
Date: May 2025
Script to showcase basic functionality of a single connected DIGIT sensor.
Based on https://github.com/facebookresearch/digit-interface
"""

# Imports
from digit_interface.digit import Digit
from digit_interface.digit_handler import DigitHandler


# Pause the program and wait for a key press
def pause():
    print("--------")
    input("Press a key to continue...")
    print("--------")


# Get a list of connected DIGIT sensors
digits = DigitHandler.list_digits()

# Print name and serial numbers
for digit in digits:
    print(f"DIGIT detected at {digit["dev_name"]} with serial number {digit["serial"]}.")

pause()

# If a DIGIT is connected
if len(digits) > 0:
    # Get the serial number for the DIGIT device
    serial = digits[0]["serial"]

    # Connect to DIGIT
    digit = Digit(serial, "Single_Digit")
    digit.connect()

    # Print basic info
    print("Digit info:")
    print(digit.info())
    pause()

    # Print possible streams
    print("Possible streams:")
    print(Digit.STREAMS)
    pause()

    # Set stream resolution and fps
    digit.set_resolution({"resolution": {"width": 320, "height": 240}})  # QVGA resolution
    digit.set_fps(Digit.STREAMS["QVGA"]["fps"]["30fps"])  # 30 fps
    print("Set stream to QVGA 30fps.")
    pause()

    # Print basic info again
    print("Digit info:")
    print(digit.info())
    pause()

    # Print min and max intensity
    print(f"Min intensity: {Digit.LIGHTING_MIN}")
    print(f"Max intensity: {Digit.LIGHTING_MAX}")
    pause()

    # Set lighting intensity
    digit.set_intensity(0)
    print("Set lighting intensity to 0.")
    pause()
    digit.set_intensity(15)
    print("Set lighting intensity to 15.")
    pause()

    # Show Open CV live view
    print("Showing live view. Hit ESC to close window.")
    digit.show_view()

    num_frames = 10
    # Save frames to disk
    print(f"Saving {num_frames} frames to disk.")
    for i in range(num_frames):
        # Save single frame from DIGIT
        frame = digit.get_frame()
        digit.save_frame(f"frame_{i}.jpg")
    print("Done!")

    # Disconnect DIGIT
    digit.disconnect()

else:
    print("No DIGITS found.")
