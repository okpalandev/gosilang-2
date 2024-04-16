from setuptools import setup, find_packages

setup(
    name='gstunit',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gstunit = gstunit.__main__:main',
        ],
    },
)
