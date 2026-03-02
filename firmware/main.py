import board
from kb import MacroPad

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.modules.macros import Macros, Press, Release, Tap, Delay

from kmk.extensions.rgb import RGB

# ─── Keyboard Instance ────────────────────────────────────────────────
keyboard = MacroPad()

# ─── Modules ──────────────────────────────────────────────────────────
layers = Layers()
holdtap = HoldTap()
macros = Macros()

keyboard.modules.append(layers)
keyboard.modules.append(holdtap)
keyboard.modules.append(macros)

# ─── RGB Extension (2x SK6812MINI-E daisy-chained on D9) ─────────────
rgb = RGB(
    pixel_pin=keyboard.rgb_pixel_pin,
    num_pixels=keyboard.rgb_num_pixels,
    val_limit=100,           # Max brightness (0-255) — keep low for USB power
    hue_default=0,           # Red hue as default (0-255)
    sat_default=255,         # Full saturation
    val_default=80,          # Default brightness
    animation_mode='static', # Static color, no animation
)
keyboard.extensions.append(rgb)

# ─── Macro Definitions ───────────────────────────────────────────────
# All macros follow the pattern:
#   Cmd+Space (open Spotlight) → delay → type app name → Enter

# Layer 0, K3: Open Photo Booth
MACRO_PHOTO_BOOTH = KC.MACRO(
    Press(KC.LGUI),
    Tap(KC.SPACE),
    Release(KC.LGUI),
    Delay(200),   # Wait for Spotlight to appear
    'Photo Booth',
    Delay(150),
    Tap(KC.ENTER),
)

# Layer 1, K1: Open Spotify
MACRO_SPOTIFY = KC.MACRO(
    Press(KC.LGUI),
    Tap(KC.SPACE),
    Release(KC.LGUI),
    Delay(200),
    'Spotify',
    Delay(150),
    Tap(KC.ENTER),
)

# Layer 1, K2: Open Visual Studio Code
MACRO_VSCODE = KC.MACRO(
    Press(KC.LGUI),
    Tap(KC.SPACE),
    Release(KC.LGUI),
    Delay(200),
    'Visual Studio Code',
    Delay(150),
    Tap(KC.ENTER),
)

# Layer 1, K3: Open Brave Browser
MACRO_BRAVE = KC.MACRO(
    Press(KC.LGUI),
    Tap(KC.SPACE),
    Release(KC.LGUI),
    Delay(200),
    'Brave',
    Delay(150),
    Tap(KC.ENTER),
)

# ─── Hold-Tap Key ────────────────────────────────────────────────────
# K4: Tap = Cmd+S (Save), Hold = MO(1) (momentary layer 1)
K4_HOLDTAP = KC.HT(
    KC.LGUI(KC.S),   # Tap action: Cmd+S
    KC.MO(1),        # Hold action: Momentary Layer 1
    prefer_hold=True,
    tap_time=200,
)

# ─── Keymap ───────────────────────────────────────────────────────────
#
#  Physical layout:
#   ┌──────┬──────┬──────┬──────┐
#   │  K1  │  K2  │  K3  │  K4  │
#   │ SW1  │ SW2  │ SW3  │ SW4  │
#   │  D0  │  D1  │  D2  │  D4  │
#   └──────┴──────┴──────┴──────┘
#
#  Layer 0 (Default):
#   K1 = Ctrl + `
#   K2 = F5
#   K3 = Macro: Photo Booth
#   K4 = Tap: Cmd+S / Hold: MO(1)
#
#  Layer 1 (Momentary):
#   K1 = Macro: Spotify
#   K2 = Macro: VS Code
#   K3 = Macro: Brave
#   K4 = Transparent (passes through to hold behavior)

keyboard.keymap = [
    # ── Layer 0 ───────────────────────────────────────────────────────
    [
        KC.LCTL(KC.GRAVE),     # K1: Ctrl + `
        KC.F5,                 # K2: F5
        MACRO_PHOTO_BOOTH,     # K3: Open Photo Booth via Spotlight
        K4_HOLDTAP,            # K4: Tap=Cmd+S, Hold=MO(1)
    ],

    # ── Layer 1 ───────────────────────────────────────────────────────
    [
        MACRO_SPOTIFY,         # K1: Open Spotify via Spotlight
        MACRO_VSCODE,          # K2: Open VS Code via Spotlight
        MACRO_BRAVE,           # K3: Open Brave via Spotlight
        KC.TRNS,               # K4: Transparent (MO(1) still active)
    ],
]

# ─── Start ────────────────────────────────────────────────────────────
if __name__ == '__main__':
    keyboard.go()