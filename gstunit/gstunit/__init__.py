import shutil
import pickle
from .keyboard import *

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


def build_mappings():
    # Instantiate the mapping classes
    standard_layout_mapping = NdebeStandardLayoutMapping()
    mobile_layout_mapping = NdebeMobileLayoutMapping()

    # Create a dictionary to hold both instances
    mapping_dict = {
        'standard': standard_layout_mapping,
        'mobile': mobile_layout_mapping
    }
    
    # Pickle the dictionary
    with open('./dist/keyboard_mapping.pkl', 'wb') as f:
        pickle.dump(mapping_dict, f)
