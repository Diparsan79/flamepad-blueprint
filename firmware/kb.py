import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner

class MacroPad(KMKKeyboard):
    def __init__(self):
        super().__init__()

        # Direct-wire key scanner (active low, pull-up enabled)
        # SW1 = D0, SW2 = D1, SW3 = D2, SW4 = D4
        self.matrix = KeysScanner(
            pins=[board.D0, board.D1, board.D2, board.D4],
            value_when_pressed=False,  # Active low (switch connects pin to GND)
            pull=True,                 # Enable internal pull-up resistors
        )

        # Single-row, 4-column coord mapping
        self.coord_mapping = [0, 1, 2, 3]

        # NeoPixel / SK6812 data pin
        self.rgb_pixel_pin = board.D9
        self.rgb_num_pixels = 2