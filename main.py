basic.clear_screen()

def on_forever():
    basic.show_number(pins.analog_read_pin(AnalogPin.P0))
    basic.pause(100)
    serial.write_value("value", pins.analog_read_pin(AnalogPin.P0))
basic.forever(on_forever)
