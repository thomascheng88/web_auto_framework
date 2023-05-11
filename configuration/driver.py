from selenium.webdriver import Chrome, Firefox, Edge, Safari
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from configuration.config_settings import ConfigSettingsClass
from appium import webdriver as appiumdriver
import os


class DriverClass:

    def get_chrome_browser(self, browser_name, private_mode, headless):
        """
        This function aims to define the Chrome Web Browser setting to be used for automation
        :no parameters
        :return: webdriver
        """
        brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

        # s = Service(executable_path=f'/Users/thcheng/Documents/99.0.4844.51/chromedriver')
        s = Service(executable_path=f'{ConfigSettingsClass.driver_path}chromedriver_win32_111.0.5563.64/chromedriver')
        opt = webdriver.ChromeOptions()

        if browser_name == 'brave':
            opt.binary_location = brave_path

        if private_mode == "True":
            opt.add_argument("--incognito")  # OPTIONAL

        if headless == "True":
            opt.add_argument("--headless")  # OPTIONAL

        # opt.add_argument("--lang={}".format('en'))
        opt.add_experimental_option('prefs', {
            'geolocation': True
        })

        # opt.set_capability('chromedriverExecutable', '/usr/local/chromedriver/99.0.4844.51/chromedriver')
        driver = Chrome(service=s, options=opt)
        return driver

    def get_firefox_browser(self):
        """
        This function aims to define the Firefox Web Browser setting to be used for automation
        :no parameters
        :return:
        """
        s = Service(executable_path=f"{ConfigSettingsClass.driver_path}geckodriver")
        opt = webdriver.FirefoxOptions()
        driver = Firefox(service=s, options=opt)
        # driver = Firefox()
        return driver

    def get_edge_browser(self):
        """
        This function aims to define the Edge Web Browser setting to be used for automation
        no parameters
        :return:
        """
        path = os.path.join(ConfigSettingsClass.driver_path, "edgedriver/msedgedriver")
        print(path)
        s = Service(executable_path=f"{path}")
        opt = webdriver.EdgeOptions()
        driver = Edge(service=s, options=opt)
        # driver = Edge()
        return driver

    def get_safari_browser(self):
        """
        This function aims to define the Safari Web Browser setting to be used for automation
        no parameters
        :return:
        """
        s = Service(executable_path=f"{ConfigSettingsClass.safari_path}safaridriver")
        driver = Safari(service=s)
        # driver = Safari()
        return driver

    def get_android_simulator_chrome_browser(self):
        """
        This function aims to define the Android Simulator Chrome Web Browser setting to be used for automation
        no parameters
        :return:
        """
        options = webdriver.ChromeOptions()
        options.set_capability('platformName', 'Android')
        options.set_capability('chromedriverExecutable',
                               f'{ConfigSettingsClass.driver_path}chromedriver_win32_103.0.5060.134/chromedriver')
       # options.set_capability('deviceName', '26288d01bc1c7ece')
        options.set_capability('deviceName', 'emulator-5554')
        # capabilities = {
        #    'platformName': 'Android',
        #    'browserName': 'Chrome',
        #    'deviceName': '26288d01bc1c7ece',  # for real device
        #    # 'deviceName': 'emulator-5554',
        #    'chromeOptions': {
        #        'androidPackage': 'com.android.chrome',
        #    }
        # }

        # driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        driver = appiumdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=options.to_capabilities())
        return driver

    def get_android_real_device_chrome_browser(self):
        """
        This function aims to define the Android Real Device Chrome Web Browser setting to be used for automation
        no parameters
        :return:
        """
        options = webdriver.ChromeOptions()
        options.set_capability('platformName', 'Android')
        options.set_capability('chromedriverExecutable',
                               f'{ConfigSettingsClass.driver_path}chrome_91.0.4472.101/chromedriver')
        driver = appiumdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=options.to_capabilities())
        return driver

    def get_ios_simulator_safari_browser(self):
        """
        This function aims to define the iOS Simulator Safari Web Browser setting to be used for automation
        no parameters
        :return:
        """
        # Set up the web driver and launch the webview app. DesiredCapabilities
        capabilities = {
            'platformName': 'iOS',
            'platformVersion': '15.4',
            'automationName': 'XCUITest',
            'browserName': 'Safari',
            'deviceName': 'iPhone 13'
        }

        # driver = driver.Remote('http://localhost:4723/wd/hub', capabilities)
        driver = appiumdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        return driver

    def get_ios_real_device_safari_browser(self):
        """
        This function aims to define the iOS Real Device Safari Web Browser setting to be used for automation
        no parameters
        :return:
        """
        # Set up the web driver and launch the webview app. DesiredCapabilities
        capabilities = {
            'platformName': 'iOS',
            'platformVersion': '15.4',
            'automationName': 'XCUITest',
            'browserName': 'Safari',
            'deviceName': 'iPhone 13'
        }

        # driver = driver.Remote('http://localhost:4723/wd/hub', capabilities)
        driver = appiumdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        return driver

    def get_ios_real_device_chrome_browser(self):
        """
        This function aims to define the iOS Real Device Chrome Web Browser setting to be used for automation
        no parameters
        :return:
        """
        # Set up the web driver and launch the webview app. DesiredCapabilities
        capabilities = {
            'platformName': 'iOS',
            'platformVersion': '15.4',
            'automationName': 'XCUITest',
            'browserName': 'Chrome',
            'deviceName': 'iPhone 13'
        }

        # driver = driver.Remote('http://localhost:4723/wd/hub', capabilities)
        driver = appiumdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        return driver

    def get_ios_simulator_chrome_browser(self):
        """
        This function aims to define the iOS Real Device Safari Web Browser setting to be used for automation
        no parameters
        :return:
        """
        # Set up the web driver and launch the webview app. DesiredCapabilities
        capabilities = {
            'platformName': 'iOS',
            'platformVersion': '15.4',
            'automationName': 'XCUITest',
            'browserName': 'Chrome',
            'deviceName': 'iPhone 13'
        }

        # driver = driver.Remote('http://localhost:4723/wd/hub', capabilities)
        driver = appiumdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        return driver
