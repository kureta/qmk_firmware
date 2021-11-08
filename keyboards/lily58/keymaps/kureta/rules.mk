# Build Options
#   change to "no" to disable the options, or define them in the Makefile in
#   the appropriate keymap folder that will get included automatically
#
BOOTMAGIC_ENABLE = no       # Enable Bootmagic Lite
MOUSEKEY_ENABLE = no        # Mouse keys
BACKLIGHT_ENABLE = no       # Enable keyboard backlight functionality
SLEEP_LED_ENABLE = no    # Breathing sleep LED during USB suspend
AUDIO_ENABLE = no           # Audio output
RGBLIGHT_ENABLE = no       # Enable WS2812 RGB underlight.
SWAP_HANDS_ENABLE = no      # Enable one-hand typing
UNICODE_ENABLE = no  # Unicode

OLED_ENABLE = yes     # OLED display
NKRO_ENABLE = yes            # Nkey Rollover - if this doesn't work, see here: https://github.com/tmk/tmk_keyboard/wiki/FAQ#nkro-doesnt-work
ENCODER_ENABLE = yes
EXTRAKEY_ENABLE = yes        # Audio control and System control

BOOTLOADER = atmel-dfu  # Elite-C

CONSOLE_ENABLE = no         # Console for debug
COMMAND_ENABLE = yes         # Commands for debug and configuration

EXTRAFLAGS += -flto

# If you want to change the display of OLED, you need to change here
SRC += qmk_rc.c
RAW_ENABLE = yes
