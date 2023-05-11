class ConfigSettingsClass:

    # List of Content Variables to be used in the Test Script
    # Windows:
    config_path = 'C:\\Users\\ThomasCUser\\Documents\\python_projects\\web_auto_framework\\configuration\\config_file.json'

    # specify browser driver directory path for web drivers (chrome, firefox, edge and safari - only for MAC)
    # windows:
    driver_path = "C:\\Windows\\"

    # MAC
    # driver_path = "/usr/local/bin/"
    # safari_path = "/usr/bin/"

    # Windows:
    execution_script_path = "C:\\Users\\ThomasCUser\\Documents\\python_projects\\web_auto_framework\\"

    # Windows:
    executable_file_name = "execution_script.bat"
    # MAC: executable_file_name = "execution_script.sh"

    # default storage path of where allure reports are stored
    # Windows
    report_path = "C:\\Users\\ThomasCUser\\Documents\\python_projects\\web_auto_framework\\reports"

    # directory bat file path of the generate allure report
    # Windows:
    generate_allure_report_path = "C:\\Users\\ThomasCUser\\Documents\\python_projects\\web_auto_framework\\generate_allure.bat"

    # pytest (define the path of pytest location)
    pytest_path = "pytest"

    screenshot_path = "C:\\Users\\ThomasCUser\\Documents\\python_projects\\web_auto_framework\\screenshots"
    supported_browsers = ['chrome', 'firefox', 'edge']