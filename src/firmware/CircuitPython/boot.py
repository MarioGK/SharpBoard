import usb_hid
import usb_cdc
import os

if os.getenv("debug") == "enabled":
    usb_cdc.enable(console=True, data=False)
else:
    usb_cdc.enable(console=False, data=True)

usb_hid.enable((usb_hid.Device.KEYBOARD,))
