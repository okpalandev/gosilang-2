from .gstunit.__main__ import *

if __name__ == "__main__":
    # Instantiate the mapping classes
    standard_layout_mapping = NdebeStandardLayoutMapping()
    mobile_layout_mapping = NdebeMobileLayoutMapping()

    # Create a dictionary to hold both instances
    mapping_dict = {
        'standard_layout_mapping': standard_layout_mapping,
        'mobile_layout_mapping': mobile_layout_mapping
    }

    # Pickle the dictionary
    with open('keyboard_mappings.pkl', 'wb') as f:
        pickle.dump(mapping_dict, f)

    
