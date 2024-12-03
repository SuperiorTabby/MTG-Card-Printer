@echo off

:: Run library manager.py
echo Downloading Libraries
python library_manager.py

:: Insure that libraries properly downloaded
if %errorlevel% neq 0 (
    echo library manager.py encountered an error. Exiting...
    pause
    exit /b %errorlevel%
)


:: Run fetcher.py
echo Running fetcher.py...
python fetcher.py

:: Check if fetcher.py succeeded
if %errorlevel% neq 0 (
    echo fetcher.py encountered an error. Exiting...
    pause
    exit /b %errorlevel%
)

:: Run document.py
echo Running document.py...
python document.py

:: Check if document.py succeeded
if %errorlevel% neq 0 (
    echo document.py encountered an error. Exiting...
    pause
    exit /b %errorlevel%
)

echo All scripts completed successfully.
pause
