import json
import pytest
from configuration.config_settings import ConfigSettingsClass
from configuration.driver import DriverClass
from appium import webdriver as appiumdriver
from utilities.customlogger import CustomLoggerClass
from utilities.otherutl import OtherUtlClass

# declare logger
logger = CustomLoggerClass.loggen()
check_log_folder = CustomLoggerClass.check_log_file_folder_exist
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from appium import webdriver
# Define the global variables
CONFIG_PATH = ConfigSettingsClass.config_path
DEFAULT_WAIT_TIME = 30
# supported browsers variable defines the browsers names that are supported with the script
SUPPORTED_BROWSERS = ConfigSettingsClass.supported_browsers


@pytest.fixture
def start_log_title():
    logger.info("---------- START OF e-Commerce STORE AUTOMATION SCRIPT ----------")
    logger.info(" SETUP CONFIGURATION OF RESOURCES & SETTINGS BEFORE EXECUTION OF SCRIPT")


@pytest.fixture
def config():
    # logger.info("Update Allure reporting folder directory structure")
    otherutl_class = OtherUtlClass()
    # current_time_string = otherutl_class.get_current_time()
    # new_report_path = otherutl_class.create_new_report_folder(Content.report_path, current_time_string)
    # otherutl_class.update_bat_file_alluredir_option(new_report_path)

    """ Read the JSON config file and returns it as a parse dict """
    # Read the JSON config file and returns it as a parse dict
    logger.info("Read the JSON config file and returns it as a parse dict")
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


# update the bat file allure report folder
# @pytest.fixture
# def update_alluredir_folder():
# logger.info("Update Allure reporting folder directory structure")
# otherutl_class = OtherUtl()
# current_time_string = otherutl_class.get_current_time()
# new_report_path = otherutl_class.create_new_report_folder(Content.report_path, current_time_string)
# otherutl_class.update_bat_file_alluredir_option(new_report_path)

@pytest.fixture
def test_data_content(config):
    """ return the test data content file path """
    return config['test_data_content']


@pytest.fixture
def config_url_run(config):
    logger.info("start Validating url and return url choice if it exist in config_file.json")
    # Validate url and return url choice
    if 'url_select' not in config:
        logger.info(f"url_select not in config_file.json")
        # exception is raised if config file doesn't contain url path
        raise Exception('The config file does not contain "url"')
    return config['url_select']


@pytest.fixture
def check_config_run_prod(config_url_run):
    """
    Checks if the configuration url is set to production or staging
    """
    if config_url_run == 'prod':
        return True
    elif config_url_run == 'stage' or config_url_run == 'latest':
        return False


@pytest.fixture
def get_selected_environment(config):
    """Retrieve the selected environment specified by user to be executed in script"""
    # Validate url and return url choice
    if 'url_select' not in config:
        # exception is raised if config file doesn't contain url path
        raise Exception('The config file does not contain "url"')
    config_selection = config['url_select']
    print("get_selected_environment function - configuration selection option: " + config_selection)
    return config_selection


@pytest.fixture
def get_url_select(config):
    """
    Retrieve the url value based on whether the url select option is prod or stage
    """
    # Validate url and return url choice
    if 'url_select' not in config:
        # exception is raised if config file doesn't contain url path
        raise Exception('The config file does not contain "url"')
    config_selection = config['url_select']
    print("configuration selection option: " + config_selection)
    if config_selection == 'prod':
        return config['prod_url']
    elif config_selection == 'stage':
        print("stage_url: " + config['stage_url'])
        logger.info("select the 'url_select' value from config_file.json, stage_url: " + config['stage_url'])
        return config['stage_url']
    elif config_selection == 'latest':
        print("latest_url: " + config['latest_url'])
        logger.info("latest_url: " + config['latest_url'])
        return config['latest']


@pytest.fixture
def config_url(config):
    """ Validate url and return url choice """
    # Validate url and return url choice
    if 'prod_url' not in config:
        # exception is raised if config file doesn't contain url path
        raise Exception('The config file does not contain "url"')
    return config['prod_url']


@pytest.fixture
def config_browser(config):
    """ Validate browser exist and return browser choice """
    # Validate browser exist and return browser choice
    if 'browser' not in config:
        # exception is raised if config file doesn't contain browser name
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture
def config_wait_time(config):
    """ Validate and return the wait time from the config data """
    logger.info("Setup wait time value")
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME

@pytest.fixture
def get_lang_url(set_lang, get_selected_environment):
    """ Configure the language setting on browser based on command line user input """
    sel_lang_url = ""
    print(f'in the get_lang function {set_lang}, enviornment is: {get_selected_environment}')
    logger.info(f'Setup Language selection option based on user selection --lang or default setting')
    logger.info(f'--lang selected: {set_lang}')

    match get_selected_environment:
        # check the selected environment specifed by user is PRDOUCTION
        case "prod":
            print(f"prod,  and the set_browser: {set_lang}")
            # check if ENGLISH language has been specified by the user
            if set_lang == "eng":
                print("navigate to english site")
                sel_lang_url = "https://www.google.com.hk"

            # check if Traditonal Chinese language has been specified by the user
            elif set_lang == "tc":
                print("navigate to traditional chinese site")
                sel_lang_url = "https://www.google.com.hk"

            # check if Simplified Chinese language has been specified by the user
            elif set_lang == "sc":
                print("navigate to simplified chinese site")
                sel_lang_url = "https://www.google.com.hk"

        # check the selected environment specified by user is STAGING
        case "stage":
            print(f"selected stage case in get_lang function and the set_browser: {set_lang}")
            # check if ENGLISH language has been specified by the user
            if set_lang == "eng":
                print("navigate to english site")
                sel_lang_url = "https://stage.www.google.com"
                logger.info(f"navigate to english site: {sel_lang_url}")

            # check if Traditonal Chinese language has been specified by the user
            elif set_lang == "tc":
                print("navigate to traditional chinese site")
                sel_lang_url = "https://stage.google.com.hk/th"

            # check if Simplified Chinese language has been specified by the user
            elif set_lang == "sc":
                print("navigate to simplified chinese site")
                sel_lang_url = "https://stage.www.google.com/zh-cn"

        # check the selected environment specified by user is LATEST
        case "latest":
            print(f"latest and the set_browser: {set_lang}")
            # check if ENGLISH language has been specified by the user
            if set_lang == "eng":
                print("navigate to english site")
                sel_lang_url = "https://latest.www.google.com"

            # check if Traditonal Chinese language has been specified by the user
            elif set_lang == "tc":
                print("navigate to traditional chinese site")
                # sel_lang_url = "https://latest.www.example.com/zh-hk/"
                sel_lang_url = "https://www.google.com.hk"

            # check if Simplified Chinese language has been specified by the user
            elif set_lang == "sc":
                print("navigate to simplified chinese site")
                # sel_lang_url = "https://latest.www.example.com/zh-cn/"
                sel_lang_url = "https://www.google.com.hk"

    return sel_lang_url


@pytest.fixture
def check_platform(set_browser):
    """
    check which platform have been specified by user input if it exist
    :parameter - set_browser
    """
    logger.info("---------- START OF e-Commerce STORE AUTOMATION SCRIPT ----------")
    logger.info(" SETUP CONFIGURATION OF RESOURCES & SETTINGS BEFORE EXECUTION OF SCRIPT")

    logger.info("Check if --browser has been specified or not and return platform type")
    platform_val = ""
    print(f'set browser ={set_browser}')
    if set_browser is not None:
        print(f'set browser contains _')
        usr_input_platform_val = set_browser.split("_")[0]
        print(f'usr_input_platform_val: {usr_input_platform_val}')

    if set_browser is None:
        return " "
    elif "_" in set_browser:
        usr_input_platform_val = set_browser.split("_")[0]
        if usr_input_platform_val == "android":
            platform_val = "mobile"
            return platform_val
        elif usr_input_platform_val == "ios":
            platform_val = "mobile"
            return platform_val
    else:
        print("platform val will be desktop")
        platform_val = "desktop"
        return platform_val


@pytest.fixture
# configure the web driver based on the specified browser name from the command line (input by user)
def get_browser(check_platform, config_browser, set_browser, set_browser_name, set_private_mode, set_headless):
    # Initialize WebDriver
    global driver
    # print(f'{check_platform}:check_platform')
    # print(f'{set_browser}: set_browser')
    logger.info("Get browser settings based on config_file.json or user specified selection (--browser) ")

    if check_platform == "desktop":
        if set_browser == 'chrome':
            driver = DriverClass()
            driver = driver.get_chrome_browser(set_browser_name, set_private_mode, set_headless)

            # s = Service(executable_path=f'/Users/thcheng/Documents/99.0.4844.51/chromedriver')
            # opt = webdriver.ChromeOptions()
            # opt.set_capability('chromedriverExecutable', '/usr/local/chromedriver/99.0.4844.51/chromedriver')
            # driver = Chrome(service=s, options=opt)
            # driver = Chrome()

        elif set_browser == 'firefox':
            driver = DriverClass()
            driver = driver.get_firefox_browser()

            # s = Service(executable_path=f"{Content.driver_path}geckodriver")
            # opt = webdriver.FirefoxOptions()
            # driver = Firefox(service=s, options=opt)
            # driver = Firefox()

        elif set_browser == 'safari':
            driver = DriverClass()
            driver = driver.get_safari_browser()

            # s = Service(executable_path=f"{Content.safari_path}safaridriver")
            # driver = Safari(service=s)
            # driver = Safari()

        elif set_browser == 'edge':
            driver = DriverClass()

            driver = driver.get_edge_browser()

            # s = Service(executable_path=f"{path}")
            # opt = webdriver.EdgeOptions()
            # driver = Edge(service=s, options=opt)
            # driver = Edge()

    elif check_platform == "mobile":
        if set_browser == 'android_chrome':
            driver = DriverClass()
            # driver = driver.get_android_real_device_chrome_browser()
            driver = driver.get_android_simulator_chrome_browser()

        elif set_browser == 'ios_safari':
            driver = DriverClass()
            # driver = driver.get_ios_real_device_safari_browser()
            driver = driver.get_ios_simulator_safari_browser()

            # Set up the web driver and launch the webview app. DesiredCapabilities
            # capabilities = {
            #    'platformName': 'iOS',
            #    'platformVersion': '15.4',
            #    'automationName': 'XCUITest',
            #    'browserName': 'Safari',
            #    'deviceName': 'iPhone 13'
            # }

            # driver = driver.Remote('http://localhost:4723/wd/hub', capabilities)
            # driver = appiumdriver.Remote('http://localhost:4723/wd/hub', capabilities)

        elif set_browser == 'ios_chrome':
            driver = DriverClass()
            # driver = driver.get_ios_real_device_chrome_browser()  # if we are using real device to test please call this function
            driver = driver.get_ios_simulator_chrome_browser()  # if we are using emulator to test please call this function

            # Set up the web driver and launch the webview app. DesiredCapabilities
            # options = webdriver.ChromeOptions()
            # options.set_capability('platformName', 'iOS')
            # capabilities = {
            #    'platformName': 'iOS',
            #    'platformVersion': '15.4',
            #    'automationName': 'XCUITest',
            #    'browserName': 'Chrome',
            #    'deviceName': 'iPhone 13'
            # }

            # driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
            # driver = appiumdriver.Remote('http://localhost:4723/wd/hub', capabilities)
            # driver = appiumdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=options.to_capabilities())
            # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=options.to_capabilities())

    # if no browser has been defined by user then look for default browser
    # get the default browser from the config_file.json
    else:
        if config_browser == 'chrome':
            driver = DriverClass()
            driver = driver.get_chrome_browser()
            print("config_browser = chrome")
            logger.info("chrome browser has been selected")
            # s = Service(executable_path='/Users/thcheng/Documents/99.0.4844.51/chromedriver')
            # opt = webdriver.ChromeOptions()
            # opt.set_capability('chromedriverExecutable', '/usr/local/bin/chrome_driver/99.0.4844.51/chromedriver')
            # driver = Chrome(options=opt)
            # driver = Chrome(service=s, options=opt)
            # driver = Chrome()

        elif config_browser == 'firefox':
            driver = DriverClass()
            driver = driver.get_firefox_browser()

            # driver = Firefox()

        elif config_browser == 'safari':
            driver = DriverClass()
            driver = driver.get_safari_browser()

            # driver = Safari()

        elif config_browser == 'edge':
            driver = DriverClass()
            driver = driver.get_edge_browser()

            # driver = Edge()

        else:
            print("no config_browser value found - go to default")
            driver = DriverClass()
            driver = driver.get_chrome_browser()
            # driver = Chrome()

    return driver


@pytest.fixture
def browser(get_browser, check_platform, config_wait_time, get_url_select, get_lang_url, set_lang):
    """ Initialize Startup
    This function defines the setting configuration for browser before execution of test cases
    Every test script with function must specfic the paramter "browser" to initialize and open browser
    ( browser name and language can be set in command line)
    :parameter get_browser = defined which browser name to execute in from the command line
    :parameter config_wait_time = defined the wait time before starting the test case execution from config_file.json
    :parameter get_url_select = defined the starting url path from the config_file.json
    :parameter set_lang = define the language to be used for test execution
    :parameter check_platform = define the platform that will be used for execution
    """
    logger.info("Initialize and Open Web Browser with configured browser type and language selection")
    # Initialize WebDriver
    # if config_browser == 'chrome':
    # get_browser = Chrome()
    # elif config_browser == 'firefox':
    # get_browser = Firefox()
    # elif config_browser == 'ie':
    # get_browser = ie()
    # elif config_browser == 'Edge':
    # get_browser = Edge()
    print(f'get_lang value: {get_lang_url} and set_lang value: {set_lang}')
    logger.info(f'get_lang value: {get_lang_url} and set_lang value: {set_lang}')

    # check that user has specified the language to be used eg. --lang eng
    if set_lang == 'eng' or set_lang == 'tc' or set_lang == 'sc':
        logger.info("get_lang_url")
        get_browser.get(get_lang_url)

    else:
        # Open initial URL as set in configuration file
        logger.info(f"No language has been selected, use default, {get_url_select}")
        get_browser.get(get_url_select)
    # queue it
    # logger.info("waiting for 30 secs")
    # driver.get(config_url)
    logger.info(f"in confest.py current url: {get_browser.current_url}")
    logger.info(f"is the platform desktop or mobile? : {check_platform}")
    if check_platform == "desktop":
        # maximize window of browser
        get_browser.maximize_window()

        # driver.maximize_window()
        # Wait implicitly for elements to be ready before attempting interactions
        get_browser.implicitly_wait(config_wait_time)
        # driver.implicitly_wait(config_wait_time)
    # Return the driver object at the end of setup

    # yield get_browser
    yield driver

    # For cleanup, quit the driver
    get_browser.quit()

    # driver.quit()


def pytest_addoption(parser):
    """ Configure customised command line options that can be utilized by user """
    parser.addoption("--browser", default='chrome',
                     choices=['chrome', 'firefox', 'edge', 'safari', 'ios_chrome', 'ios_safari', 'android_chrome'],
                     help="Select chrome, firefox, edge, safari, ios chrome or ios safari for automation excution")
    parser.addoption("--lang", default='eng', choices=['eng', 'tc', 'sc'],
                     help="Select a language to run the merchstore, eng = english, tc= traditional chinese, sc= simplified chinese")
    parser.addoption("--name", default='na', choices=['na', 'chrome', 'brave', 'firefox', 'edge'],
                     help="Select a browser name")
    parser.addoption("--private_mode", default='False', choices=['True', 'False'],
                     help="Select if private mode will be executed on browser")
    parser.addoption("--headless", default='False', choices=['True', 'False'],
                     help="Select if browser execution is visual on the screen to or run in background")


# This will return the browser value to setup browser selection
@pytest.fixture
def set_browser(request):
    return request.config.getoption("--browser")


# This will return the browser name that will be opened in the browser
@pytest.fixture
def set_browser_name(request):
    return request.config.getoption("--name")


# This will return the browser mode that will be opened in the browser
@pytest.fixture
def set_private_mode(request):
    return request.config.getoption("--private_mode")


@pytest.fixture
def set_headless(request):
    return request.config.getoption("--headless")


# This return the selected lang value to set up which language to use in the execution
@pytest.fixture
def set_lang(request):
    return request.config.getoption("--lang")


# This return the selected store value to set up which store to be used for execution
# @pytest.fixture
# def set_lang(request):
#      return request.config.getoption("--store")


# Pytest-bdd Hook (reporting purpose)
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step Failed:{step} and the step function {step_func}')

# --------------------- pytest HTML Report ------------------------
# def pytest_configure(browser):
#    config.metadata['Project Name'] = ''
#   config.metadata['Module Name'] = 'Online Ticketing'
#    config.metadata['Tester'] = 'Thomas C'


# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#   metadata.pop("JAVA_HOME", None)
#    metadata.pop("Plugins", None)
