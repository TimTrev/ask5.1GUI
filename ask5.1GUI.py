# Importing necessary libraries for GPIO pins and GUI interfaces
import RPi.GPIO as GPIO
import tkinter as tk

# GPIO Setup
GPIO.setmode(GPIO.BCM)
LED_PINS = {"Red": 17, "Green": 27, "Blue": 22}
GPIO.setup(list(LED_PINS.values()), GPIO.OUT, initial=GPIO.LOW) # Initially turns them off

# Function to turn on the selected LED
def turn_on_led():
    selected_colour = led_var.get() #
    for colour, pin in LED_PINS.items(): # Turns on LED if it matches the selected colour
        GPIO.output(pin, GPIO.HIGH if colour == selected_colour else GPIO.LOW)

# Function to exit the GUI and cleanup GPIO
def exit_gui():
    GPIO.cleanup()
    root.destroy()

# Create GUI with window title and window size
root = tk.Tk()
root.title("LED Controller")
root.geometry("300x100")

led_var = tk.StringVar(value="Red") # Variable to store the LED colour - default red

# Create radio buttons for LEDs in a single row
frame = tk.Frame(root)  # Create a frame/container to hold the buttons
frame.pack(pady=10)  # Add some space above and below the buttons

col = 0  # Column index for grid layout
for colour in LED_PINS: # Creates a 'radio button' for each LED
    # Places buttons in a row, adjust spacing horizontally
    tk.Radiobutton(frame, text=colour, variable=led_var, value=colour, command=turn_on_led).grid(row=0, column=col, padx=10)
    col += 1  # Move to the next column

# Creates an exit button to clean up GPIO and close the window
tk.Button(root, text="Exit", command=exit_gui).pack(pady=10)

# Run GUI and the Tkinter event loop
root.mainloop()
