# net_radio_pi
This is a project for Digital Radio enthusiasts. We utilize Raspberry pi MCU with 1*2 LCD for this project. 

Main Steps involved :
1. Setup Raspberry pi
2. Ensure you have python3 and pip3
3. sudo apt-get update
4. pip install rpi-lcd
5. sudo apt-get install rpi.gpio
6. Copy the net_radio_pi.py file to your RPI 
7. Go to folder using cd command
8. Run net_radio_pi.py as :
9. python3 radio.py

Your Radio is ready.
A simple click switch is connected between :
The RPI's GPIO Ground and GPIO 7 for channel selection. 

1. You can spice up with an LCD Display to show channel details.
2. Please replace your channel weblinks in the code. 
3. For any channel selection, the radio will play BBC only as it is.
