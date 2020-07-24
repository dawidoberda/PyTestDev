from setuptools import setup
from os import path
# trzeba to zainstalowac pip install --editable .
# TODO: dodac kolejne pomiary do measurement_tool

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="PyTestDev",
    version="2020.07.23",
    description="A Kit of different packages which can be used for Test Development Scripts.",
    author="Dawid Oberda",
    author_email="dawidoberda@gmail.com",
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['dmm_test', 'dmm_measurement_tool', 'korad_control'],
    entry_points={
        'console_scripts': [
            'dmm_test=dmm_test:test',
            'dmm_measure=dmm_measurement_tool:measure',
            'korad_set=korad_control:set',
            'korad_get=korad_control:get'
        ]
    }, install_requires=['click', 'pyvisa', 'numpy', 'pyserial', 'matplotlib']
)