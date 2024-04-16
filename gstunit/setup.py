from setuptools import setup, find_packages
from gstunit import build_mappings

# Read the contents of README.md
with open('README.md', 'r') as f:
    long_desc = f.read()

setup(
    name='gstunit',
    version='0.1',
    packages=find_packages(),
    long_description=long_desc,
    long_description_content_type='text/markdown'
)

# Call the build_mappings function
build_mappings()
