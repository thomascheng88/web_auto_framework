from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoSuchFrameException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from utilities.customlogger import CustomLoggerClass
import time


class BasePage:
    # logger = CustomLoggerClass.loggen()
    count = 0
    current_element = False
    MAXIMUM_WAIT_TIME = 1

    def __init__(self, driver):
        self.driver = driver

    def click_element_xpath(self, element):
        """
        This function is used to perform the click action by using the element's xpath locator value,
        returns False if it cannot be found
        """
        try:
            click_element = self.wait_for_element_clickable_xpath(element)
            # self.logger.info(f"click_element: {click_element}")
            click_element.click()
            return True
        except(NoSuchFrameException, NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return False

    def click_element_id(self, element):
        """
        This function is used to perform the click action by using the element's id locator value,
        returns False if it cannot be found
        """
        try:
            click_element = self.find_element_id(element)
            click_element.click()
            return True
        except(NoSuchFrameException, NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return False

    def click_element_by_css_selector(self, element):
        """
        This function is used to perform the click action by using the element's css selector locator value,
        returns False if it cannot be found
        """
        try:
            click_element = self.find_element_css_selector(element)
            click_element.click()
            return True
        except(NoSuchFrameException, NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return False

    def click_element_name(self, element):
        """
        This function is used to perform the click action by using the element's name locator value,
        returns False if it cannot be found
        """
        try:
            click_element = self.find_element_name(element)
            click_element.click()
            return True
        except(NoSuchFrameException, NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return False

    def click_element_class_name(self, element):
        """
        This function is used to perform the click action by using the element's class name locator value,
        returns False if it cannot be found
        """
        try:
            click_element = self.find_element_class_name(element)
            click_element.click()
            return True
        except(NoSuchFrameException, NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return False

    def find_element_xpath(self, element):
        """
        This function is used to find the element taking in xpath locator value, returns False if it cannot be found
        """
        try:
            find_by_element = self.driver.find_element(By.XPATH, element)
            return find_by_element
        except(NoSuchFrameException, NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return False

    def find_element_css_selector(self, element):
        """
        This function is used to find the element taking in css selector locator value, returns False if it cannot be found
        """
        try:
            find_by_element = self.driver.find_element(By.CSS_SELECTOR, element)
            return find_by_element
        except(NoSuchFrameException, NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return False

    def find_element_id(self, element):
        """
        This function is used to find the element taking in id locator value, returns False if it cannot be found
        """
        try:
            find_by_element = self.driver.find_element(By.ID, element)
            return find_by_element
        except(NoSuchFrameException, NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return False

    def find_element_name(self, element):
        """
        This function is used to find the element taking in name locator value, returns False if it cannot be found
        """
        try:
            find_by_element = self.driver.find_element(By.NAME, element)
            return find_by_element
        except(NoSuchFrameException, NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return False

    def find_element_class_name(self, element):
        """
        This function is used to find the element taking in class name locator value, returns False if it cannot be found
        """
        try:
            find_by_element = self.driver.find_element(By.CLASS_NAME, element)
            return find_by_element
        except(NoSuchFrameException, NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return False

    def find_element_tag_name(self, element):
        """
        This function is used to find the element taking in tag ame locator value, returns False if it cannot be found
        """
        try:
            find_by_element = self.driver.find_element(By.TAG_NAME, element)
            return find_by_element
        except(NoSuchFrameException, NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return False

    def get_element_href_attribute_xpath(self, element):
        """
        This function is used to get the href attribute value by using the element's xpath locator value
        """

        try:
            href_attribute_element = self.find_element_xpath(element)
            href_attribute_text = href_attribute_element.get_attribute("href")
            return href_attribute_text
        except(NoSuchFrameException, NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return ''

    def get_element_value_attribute_xpath(self, element):
        """
        This function is used to get the value attribute value by using the element's xpath locator value
        """

        try:
            value_attribute_element = self.find_element_xpath(element)
            value_attribute_text = value_attribute_element.get_attribute("value")
            return value_attribute_text
        except(NoSuchFrameException, NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return ''

    def get_element_attribute_val_id(self, element):
        try:
            # self.logger.info(f"inside get_element_attribute_val_id the element value = {element}")
            get_element = self.find_element_id(element)
            # self.logger.info(f"inside get_element_attribute_val_id the element exist?? : {get_element} ")
            get_element_val_attribute = get_element.get_attribute("value")
            # self.logger.info(f"inside get_element_attribute_val_id, {get_element_val_attribute}")
            return get_element_val_attribute
        except(NoSuchElementException, TimeoutException, AttributeError, RuntimeError, TypeError, NameError):
            return 'cannot find the element attribute value in the element'

    def get_element_text_val_xpath(self, element):
        """
        This function is used to the element text value by using the element's xpath locator value,
        return '' if no text value is found
        """
        try:
            get_element = self.find_element_xpath(element)
            get_element_txt_value = get_element.text
            return get_element_txt_value
        except(NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return ''

    def get_element_text_val_by_css_selector(self, element):
        """
        This function is used to the element text value by using the element's css selector locator value,
        return '' if no text value is found
        """
        try:
            element = self.find_element_css_selector(element)
            element_value = element.text
            return element_value
        except(NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return ''

    def get_element_text_val_id(self, element):
        """
        This function is used to the element text value by using the element's id locator value,
        return '' if no text value is found
        """
        try:
            element = self.find_element_id(element)
            element_value = element.text
            return element_value
        except(NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return ''

    def get_element_text_val_class_name(self, element):
        """
        This function is used to the element text value by using the element's class name locator value,
        return '' if no text value is found
        """
        try:
            get_element = self.find_element_class_name(element)
            get_element_txt_value = get_element.text
            return get_element_txt_value
        except(NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return ''

    def get_element_text_val_name(self, element):
        """
        This function is used to the element text value by using the element's name locator value,
        return '' if no text value is found
        """
        try:
            get_element = self.find_element_name(element)
            get_element_txt_value = get_element.text
            return get_element_txt_value
        except(NoSuchElementException, AttributeError, RuntimeError, TypeError, NameError):
            return ''

    # def wait_for_element_xpath(self, element):
    #     while self.count < 2:
    #         try:
    #             if self.browser.find_element_by_xpath(element).is_displayed():
    #                 self.current_element = self.browser.find_element_by_xpath(element)
    #                 self.logger.info(f'found element, {self.current_element}')
    #                 return self.current_element
    #             self.count = self.count + 1
    #         except(NoSuchElementException, TypeError, TimeoutError):
    #             self.logger.info('failed element - exception found')
    #             self.count = self.count + 1
    #         self.logger.info(f'count: {self.count}')
    #         time.sleep(4)
    #     self.logger.info("end of loop wait element function result: " + str(self.current_element))
    #     return self.current_element

    def get_element_attribute_ariaselected_id(self, element):
        try:
            # self.logger.info(f"inside get_element_attribute_ariaselected_id the element value = {element}")
            get_element = self.find_element_id(element)
            # self.logger.info(f"inside get_element_attribute_ariaselected_id the element exist?? : {get_element} ")
            get_element_ariaselected_attribute = get_element.get_attribute("aria-selected")
            # self.logger.info(f"inside get_element_attribute_ariaselected_id, {get_element_ariaselected_attribute}")
            return get_element_ariaselected_attribute
        except(NoSuchElementException, TimeoutException, AttributeError, RuntimeError, TypeError, NameError):
            return 'cannot find the element attribute value in the element'

    def wait_for_clickable_xpath(self, xpath):

        try:
            element = WebDriverWait(self.driver, self.MAXIMUM_WAIT_TIME, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )

            return element

        except(NoSuchFrameException, NoSuchElementException, TypeError, TimeoutError, TimeoutException):
            return False

    def wait_for_element_xpath(self, xpath):
        """
            The function will wait for a maximum of [MAXIMUM_WAIT] seconds for an element to be found.
            If no element is found, a (boolean) False is returned. The function will return the element
            in case of success.
        """
        try:
            element = WebDriverWait(self.driver, self.MAXIMUM_WAIT_TIME, poll_frequency=2).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )

            return element

        except(NoSuchFrameException, NoSuchElementException, TypeError, TimeoutError, TimeoutException):
            return False

    def wait_for_element_id(self, id_var):

        try:
            element = WebDriverWait(self.driver, self.MAXIMUM_WAIT_TIME, poll_frequency=2).until(
                EC.visibility_of_element_located((By.ID, id_var))
            )

            return element

        except(NoSuchFrameException, NoSuchElementException, TypeError, TimeoutError, TimeoutException):
            return False

    def wait_for_visibility_of_element_located_id(self, id_var):
        try:
            element = WebDriverWait(self.driver, self.MAXIMUM_WAIT_TIME, poll_frequency=2).until(
                EC.visibility_of_element_located((By.ID, id_var)))

            return element
        except(NoSuchFrameException, NoSuchElementException, TypeError, TimeoutError, TimeoutException):
            return False

    def wait_for_invisiblity_of_element_id(self, id_var):
        try:

            element = WebDriverWait(self.driver, self.MAXIMUM_WAIT_TIME, poll_frequency=2).until(
                EC.invisibility_of_element_located((By.ID, id_var))
            )

            return element
        except(NoSuchFrameException, NoSuchElementException, TypeError, TimeoutError, TimeoutException):
            return False

    def wait_for_invisiblity_of_element_xpath(self, xpath_var):
        try:

            element = WebDriverWait(self.driver, self.MAXIMUM_WAIT_TIME, poll_frequency=2).until(
                EC.invisibility_of_element_located((By.XPATH, xpath_var))
            )

            return element
        except(NoSuchFrameException, NoSuchElementException, TypeError, TimeoutError, TimeoutException):
            return False

    def wait_for_element_clickable_xpath(self, xpath_var):
        try:
            element = WebDriverWait(self.driver, self.MAXIMUM_WAIT_TIME, poll_frequency=2).until(
                EC.element_to_be_clickable((By.XPATH, xpath_var))
            )

            return element
        except(NoSuchFrameException, NoSuchElementException, TypeError, TimeoutError, TimeoutException):
            return False

    def wait_for_element_presence_xpath(self, xpath_var):
        try:
            element = WebDriverWait(self.driver, self.MAXIMUM_WAIT_TIME, poll_frequency=2).until(
                EC.presence_of_element_located((By.XPATH, xpath_var))
            )

            return element
        except(NoSuchFrameException, NoSuchElementException, TypeError, TimeoutError, TimeoutException):
            return False

    def wait_for_element_presence_id(self, id_var):
        try:
            element = WebDriverWait(self.driver, self.MAXIMUM_WAIT_TIME, poll_frequency=2).until(
                EC.presence_of_element_located((By.ID, id_var))
            )

            return element
        except(NoSuchFrameException, NoSuchElementException, TypeError, TimeoutError, TimeoutException):
            return False

    def wait_for_element_presence_css_selector(self, css_sel_var):
        try:
            element = WebDriverWait(self.driver, self.MAXIMUM_WAIT_TIME, poll_frequency=2).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, css_sel_var))
            )

            return element
        except(NoSuchFrameException, NoSuchElementException, TypeError, TimeoutError, TimeoutException):
            return False

    def wait_for_element_class_name(self, class_name):
        """
            The function will wait for a maximum of [MAXIMUM_WAIT] seconds for an element to be found.
            If no element is found, a (boolean) False is returned. The function will return the element
            in case of success.
            check every 500 milliseconds
        """
        try:
            element = WebDriverWait(self.driver, self.MAXIMUM_WAIT_TIME, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CLASS_NAME, class_name))
            )

            return element

        except(NoSuchFrameException, NoSuchElementException, TypeError, TimeoutError, TimeoutException):
            return False

    # def wait_for_element_class_name(self, element):
    #     while self.count < 2:
    #         try:
    #             if self.browser.find_element_by_xpath(element).is_displayed():
    #                 self.current_element = self.browser.find_element_by_xpath(element)
    #                 self.logger.info(f'found element, {self.current_element}')
    #                 return self.current_element
    #             self.count = self.count + 1
    #         except(NoSuchElementException, TypeError, TimeoutError):
    #             self.logger.info('failed element - exception found')
    #             self.count = self.count + 1
    #         self.logger.info(f'count: {self.count}')
    #         time.sleep(5)
    #     self.logger.info("end of loop wait element function result: " + str(self.current_element))
    #     return self.current_element
    def hover_over_element_id(self, element):
        """
        This function is used to hover over the element by using the element's xpath locator value
        """
        element_hover_over = self.find_element_id(element)
        action = ActionChains(self)
        action.move_to_element(element_hover_over)
        action.perform()

    def hover_over_element_xpath(self, element):
        """
        This function is used to hover over the element by using the element's xpath locator value
        """
        element_hover_over = self.find_element_xpath(element)
        action = ActionChains(self)
        action.move_to_element(element_hover_over)
        action.click(element_hover_over)
        action.perform()

    def hover_over_element_class_name(self, element):
        """
        This function is used to hover over the element by using the element's class name locator value
        """
        element_hover_over = self.find_element_class_name(element)
        action = ActionChains(self)
        action.move_to_element(element_hover_over)
        action.perform()

    def hover_over_element_name(self, element):
        """
        This function is used to hover over the element by using the element's name locator value
        """
        element_hover_over = self.find_element_name(element)
        action = ActionChains(self)
        action.move_to_element(element_hover_over)
        action.perform()

    def hover_over_element_css_selector(self, element):
        """
        This function is used to hover over the element by using the element's css selector locator value
        """
        element_hover_over = self.find_element_css_selector(element)
        action = ActionChains(self)
        action.move_to_element(element_hover_over)
        action.perform()

    def is_element_enabled_id(self, element_id):
        """
        This function is used to check element is enabled by using the element's xpath locator value
        """
        action_element = self.find_element_id(element_id)
        is_enabled = action_element.is_enabled()
        return is_enabled

    def is_element_enabled_xpath(self, element_xpath):
        """
        This function is used to check element is enabled by using the element's xpath locator value
        """
        action_element = self.find_element_xpath(element_xpath)
        is_enabled = action_element.is_enabled()
        return is_enabled

    def slow_type_into_textbox_xpath(self, element, text_input):

        try:
            # self.logger.info(f"pass in the element: {element}")
            txtbox_element = self.wait_for_element_xpath(element)
            # self.logger.info(f"inside type into textbox xpath: {txtbox_element}")
            # self.logger.info(f"text_input to type in the textbox: {text_input}")
            for character in text_input:
                txtbox_element.send_keys(character)
                time.sleep(0.3)  # pause for 0.3 seconds

            return True
        except(NoSuchElementException, TypeError, TimeoutError, TimeoutException):
            return False

    def type_into_textbox_xpath(self, element, text_input):
        """
        This function is used to perform the type into action by using the element's xpath locator value
        """
        try:
            # self.logger.info(f"pass in the element: {element}")
            txtbox_element = self.wait_for_element_xpath(element)
            # self.logger.info(f"inside type into textbox xpath: {txtbox_element}")
            # self.logger.info(f"text_input to type in the textbox: {text_input}")
            txtbox_element.send_keys(text_input)
            return True
        except(NoSuchElementException, TypeError, TimeoutError, TimeoutException):
            return False

    def type_into_textbox_name(self, element, text_input):
        """
        This function is used to perform the type into action by using the element's name locator value
        """
        txtbox_element = self.find_element_name(element)
        txtbox_element.send_keys(text_input)

    def type_into_textbox_id(self, element, text_input):
        """
        This function is used to perform the type into action by using the element's id locator value
        """
        txtbox_element = self.find_element_id(element)
        txtbox_element.send_keys(text_input)

    def select_drpdwn_lst_value_xpath(self, element, select_value_text):
        """
        This function is used to click on the dropdown list option by taking in dropdown option xpath locator value
        and the selected value text
        """
        select_value_drpdwn_lst = Select(self.find_element_xpath(element))
        try:
            select_value_drpdwn_lst.select_by_value(select_value_text)
        except(NoSuchElementException, TypeError, TimeoutError):
            return False

    def get_total_options_from_lst_xpath_tag_name(self, element, tag_name):
        """
        this will return the total no. of options in the list
        element - should be the outer div or ul
        tag name - the name of tag inside the div or li
        """
        total_options_from_lst_element = self.find_element_xpath(element)
        items = total_options_from_lst_element.find_elements_by_tag_name(tag_name)
        items_length = len(items)
        return items_length

    def get_total_options_from_lst_xpath_class_name(self, element, class_name):
        """
        this will return the total no. of options in the list
        element - should be the outer div or ul
        class name - div or li class name
        """
        total_options_from_lst_element = self.find_element_xpath(element)
        items = total_options_from_lst_element.find_element(By.CLASS_NAME, class_name)
        items_length = len(items)
        return items_length

    def check_scroll_dropdown_lst(self, user_dropdown_select_no, element):
        # self.logger.info("user_dropdown_select_no: " + str(user_dropdown_select_no))
        user_select = user_dropdown_select_no + 1
        # self.logger.info("user_select: " + str(user_select))
        if user_select > 7:
            pass
            # self.logger.info("perform dropdown list scroll down action")
            # self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_on_drpdwn_lst_option(self, element):
        """
        This function is used to click on the dropdown list option
        """

        click_on_list = element.find_element(By.TAG_NAME, 'div')
        # self.logger.info(str(click_on_list))
        actions = ActionChains(self.driver)
        actions.click(click_on_list).perform()

    def radio_btn_is_selected(self, element):
        """
        This function is used to radio btn from a list of radio btn options
        """
        find_by_element = self.find_element_xpath(element).is_selected()
        return find_by_element

    def scroll_element_into_view_xpath(self, xpath):
        """
        This function is used to scroll to the element by using the element's xpath locator value
        """
        element = self.find_element_xpath(xpath)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_element_into_view_id(self, id_element):
        """
        This function is used to scroll to the element by using the element's id locator value
        """
        element = self.find_element_id(id_element)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_elements_xpath(self, xpath):
        """
        This function is used to find the elements by using the element's xpath locator value,
        returns False if it cannot be found
        """

        return self.driver.find_elements(By.XPATH, xpath)

    def find_elements_class_name(self, class_name):
        """
        This function is used to find the elements by using the element's class name locator value,
        returns False if it cannot be found
        """

        return self.driver.find_elements(By.CLASS_NAME, class_name)

    def get_current_url(self):
        return self.driver.current_url

    def navigate_to_url(self, str_url):
        self.driver.get(str_url)

    def key_page_down(self, driver):
        action = ActionChains(driver)
        action.key_down(Keys.PAGE_DOWN)
        action.perform()

    def key_page_up(self, driver):
        action = ActionChains(driver)
        action.key_down(Keys.PAGE_UP)
        action.perform()

    def get_all_cookies(self):
        return self.driver.get_cookies()

    def get_speific_cookie(self, cookie_name):
        return self.driver.get_cookie(cookie_name)

    def delete_all_cookies(self):
        return self.driver.delete_cookies()
