@echo off
echo Start Perparing new virtual enviroment..
call python -v -m venv venv
echo Activating new venv
call .\venv\Scripts\activate.bat
echo Activated
echo Installing required packages
call pip install -r requirements.txt
echo Packages installed
echo Install PyTestDev
call pip install --editable .
pause