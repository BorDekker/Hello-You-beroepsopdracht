from microbit import *

while True:
    if display.read_light_level() < 50:
        display.show(Image(
        "00990:"
        "09009:"
        "90090:"
        "09009:"
        "00990"))
    else:
        display.show(Image(
            "90909:"
            "09990:"
            "99999:"
            "09990:"
            "90909"))