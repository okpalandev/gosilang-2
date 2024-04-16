
from .keyboard import *
import pickle

standard_layout_mapping = NdebeStandardLayoutMapping()
mobile_layout_mapping = NdebeMobileLayoutMapping()

with open('desktop.pkl', 'wb') as f:
    pickle.dump(standard_layout_mapping, f)

with open('mobile_layout_mapping.pkl', 'wb') as f:
    pickle.dump(mobile_layout_mapping, f)
