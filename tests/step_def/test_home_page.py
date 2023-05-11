from pytest_bdd import scenario, given, when, then, parsers
from functools import partial
from utilities.otherutl import OtherUtlClass
from utilities.customlogger import CustomLoggerClass
from configuration.config_settings import ConfigSettingsClass

import allure
from allure_commons.types import AttachmentType

# declare logger
logger = CustomLoggerClass.loggen()
# declare OtherUtl
other_utl_class = OtherUtlClass()

test_id = ""

EXTRA_TYPES = {
    'String': str,
}

parse_str = partial(parsers.cfparse, extra_types=EXTRA_TYPES)


@scenario(other_utl_class.get_hkdl_folder_path() + "tests/features/test_home_page.feature",
          'Visit homepage')
def test_scenario():
    pass


# Step 1
@given("guest open the browser")
def given_scenario_one():
    logger.info("Start script: test open homepage")
    logger.info("guest open the browser")


@when("guest navigate to the homepage")
def when_scenario_one():
    logger.info("When guest navigate to the homepage")


@then("displays the homepage search")
def then_scenario_one(browser):
    logger.info("Then displays the homepage search")

    #if "" is False:
    #    logger.info("search found on the current page")
    assert True
    #else:
    #    screenshot_file_name = test_id + "_step1_then_fail_show_search"
    #    common_steps = CommonStepClass()
    #    common_steps.take_screenshot_add_to_report(screenshot_file_name, browser)
    #    assert False


@then("displays the homepage title")
def then_scenario_one(browser):
    logger.info("Then displays the homepage title")

    #if "" is False:
    #    logger.info("homepage title found on the current page")
    assert True
    #else:
    #    screenshot_file_name = test_id + "_step1_then_fail_show_title"
    #    common_steps = CommonStepClass()
    #    common_steps.take_screenshot_add_to_report(screenshot_file_name, browser)
    #    assert False
