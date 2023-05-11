from pages.basepage import BasePage


class Homepage(BasePage):
    # -------------------------- Define Element Locator Identifier to be use ------------------------------

    # --------------------------------------- Defined Actions for HKDL Home Page----------------------------

    def __init__(self, driver):
        super().__init__(driver)

    # FIND FUNCTIONS
    def wait_for_homepage_entire_pg_xpath_element(self):
        return BasePage.wait_for_element_xpath(self, self._homepage_entire_pg_xpath)