from setuptools import setup
#trzeba to zainstalowac pip install --editable .
#TODO: dodac kolejne pomiary do measurement_tool
#TODO: dodac wymagania do setup() wszystkie pakiey ktore sa zainstalowane.
#TODO: dodac do entry_points measurement_tool
setup(
    name="PyTestDev",
    version="2020.07.23",
    description="A Kit of different packages which can be used for Test Development Scripts.",
    author="Dawid Oberda",
    author_email="dawidoberda@gmail.com",
    py_modules=['dmm_test', 'measurement_tool'],
    entry_points={
        'console_scripts': [
            'dmm_test=dmm_test:test'
        ]
    },
)