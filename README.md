# Web Automation Framework

This project contains the files for a simple python based bbd style test automation framework

## Introduction to the test script
There is one test script:test_home_page.py. This script's purpose is to check objective
1. Homepage is displayed

See video for an example on how to execute script: cg_demo.mp4

### Setup & Configuration Instructions Before Running the Script:

System Requirements
- Windows 10 Home or Higher / MAC OS 
- Local Disk > 100GB
- CPU that Support VT-x (hardware accelerated visualization) <- require for Android emulator

#### Step-by-Step Instructions (Windows):
1. Download Python version greater than 3.10.x from https://www.python.org/downloads/

    **RECOMMENDED**: current working version 3.10.4 https://www.python.org/downloads/release/python-3104/
    During installation add python to the Environment Variable

2. Go to Environment Variable and check user variable name "PATH" has 2 paths added to the list 
    ../Python310/Python/ & ../Python310/Python/Scripts/
3. Download Java JDK 18.0.1 or greater https://www.oracle.com/java/technologies/downloads/
4. Go to Environment Variable and under system variable create a variable name = JAVA_HOME , "directory path of java_sdk"
5. Now go to system variable name PATH, and add a new directory as follows "%JAVA_HOME%/bin"
6. Download the following browser if it is not already installed: 
   - Chrome https://www.google.com/intl/en_hk/chrome/
   - Firefox https://www.mozilla.org/en-US/firefox/new/
   - Edge https://www.microsoft.com/en-us/edge?form=MA13FJ
7. Install the Build Tools Microsoft C++ Build Tools https://visualstudio.microsoft.com/vs/older-downloads/, download the latest version, if you encounter problem later on suggest download 2017, 2019 too
reference: https://wiki.python.org/moin/WindowsCompilers#Microsoft_Visual_C.2B-.2B-_14.2_standalone:_Build_Tools_for_Visual_Studio_2019_.28x86.2C_x64.2C_ARM.2C_ARM64.29
   - Verify the Build Tools have been installed by going to control panel and look for Microsoft Visual C++ Redistributable file(s)
8. Download Web Drivers for Chrome, Firefox and Edge (Please check the version of your browser before downloading)
   - Chrome Web Driver https://chromedriver.chromium.org/downloads
   - Firefox Web Driver https://github.com/mozilla/geckodriver/releases
   - Edge Web Driver https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   If your Edge Driver version is not displayed on the given url screen, click on Full Directory button to open a list of all previous versions of the Edge web driver 
9. Place the web drivers for each browser in "C:\Windows\" eg. "C:\Windows\web_driver\chrome_v99\chromedriver.exe", "C:\Windows\web_driver\geckodriver.exe", "C:\Windows\web_driver\edge_v59\edgedriver.exe"
10. Open Command Prompt and use PIP to install the following python packages (any version higher hasn't been tested)
    - Selenium v4.4.0 https://selenium-python.readthedocs.io/installation.html
    - pytest v6.2.4 https://pypi.org/project/pytest/
    - allure-pytest-bdd
    - Appium Server Client
11. Download Pycharm CE (Community Edition) https://www.jetbrains.com/pycharm/download/
12. Open Pycharm CE 
13. Go to setting and install the following packages under python interpreter
    - Selenium
    - pytest
    - allure-pytest-bdd
    - Appium Server Client

### How to Execute Test Scripts
Type in the following command in terminal: 
pytest test_home_page.py