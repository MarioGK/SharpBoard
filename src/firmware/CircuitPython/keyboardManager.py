import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
import config


def update_layer(index):
    global active_layer_index
    global active_layer
    global active_keys
    global activation_sequence

    active_layer_index = index
    active_layer = config.layers[active_layer_index]
    active_keys = active_layer["keys"]
    activation_sequence = active_layer["activation"]


def change_layer():
    for possible_layer in config.layers:
        if possible_layer["activation"] == pressed_keys:
            update_layer(possible_layer["index"])
            return True

    return False


def handle_events():
    event = keys.events.get()
    # event will be None if nothing has happened.
    if event:
        if event.pressed:
            print("Pressed:", event.key_number)
            pressed_keys.append(event.key_number)

        if event.released:
            print("Released:", event.key_number)
            pressed_keys.pop(event.key_number)
            kbd.release(active_keys[event.key_number])

    changed_layer = change_layer()

    if changed_layer:
        print("Changed layer to: " + str(active_layer_index))
        print("Activation sequence: " + str(activation_sequence))
        print("Active keys: " + str(active_keys))
        return
    else:
        for key in pressed_keys:
            kbd.press(active_keys[key])


pressed_keys = []
active_layer_index, active_layer, active_keys, activation_sequence = None, None, None, None

update_layer(0)

keys = keypad.Keys(config.pins, value_when_pressed=False, pull=True)
kbd = Keyboard(usb_hid.devices)
