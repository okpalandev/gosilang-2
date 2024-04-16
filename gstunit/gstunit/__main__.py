
from .keyboard import *
import pickle

def igbo_to_ndebe(gosi_code):

    # Create an instance of the NdebeKeyboardMapping class
    keyboard_mapping = NdebeStandardLayoutMapping()

    # Translate each character in the Gosi code using the keyboard mapping
    translated_code = ""
    for char in gosi_code:
        translated_char = keyboard_mapping.get_translation(char)
        translated_code += translated_char

    return translated_code


def ndebe_to_igbo(ndebe_code):
    # Create an instance of the NdebeKeyboardMapping class
    keyboard_mapping = NdebeKeyboardMapping()

    # Translate each character in the Ndebe code back to Igbo characters
    translated_code = ""
    for char in ndebe_code:
        translated_char = keyboard_mapping.get_translation(char)
        translated_code += translated_char

    return translated_code
