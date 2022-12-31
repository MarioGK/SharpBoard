import json
import board

config_content = open("config.json", "r").read()
config_object = json.loads(config_content)

pins = []

for pin_number in config_object["pins"]:
    pin = getattr(board, "IO" + str(pin_number))
    pins.append(pin)

layers = config_object["layers"]

# print(config_object)
