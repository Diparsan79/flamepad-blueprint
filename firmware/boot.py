import usb_hid

# Enable all standard HID devices (keyboard + consumer control for media keys)
usb_hid.enable((usb_hid.Device.KEYBOARD, usb_hid.Device.CONSUMER_CONTROL))