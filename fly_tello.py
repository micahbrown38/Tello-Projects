from djitellopy import Tello
import time

# Connect to the Tello drone
tello = Tello()
tello.connect()

# Display battery level
battery_level = tello.get_battery()
print(f"Battery level: {battery_level}%")

# Take off
tello.takeoff()

# Hover for 5 seconds
time.sleep(5)

# Land
tello.land()

# Disconnect
tello.end()

