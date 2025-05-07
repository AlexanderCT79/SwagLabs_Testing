import pytest
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Utils.webdriver import WebDriver
from Utils.logger import Logger


VALID_USERNAMES = ["standard_user",
                   "locked_out_user",
                   "problem_user",
                   "performance_glitch_user",
                   "error_user",
                   "visual_user"]

VALID_PASSWORD = "secret_sauce"

WARNING_MESSAGES = ["Epic sadface: Username and password do not match any user in this service",
                    "Epic sadface: Username is required",
                    "Epic sadface: Password is required"]


ENTERED_USERNAME = "standard_user_invalid"
ENTERED_PASSWORD = "secret_sauce_invalid"


def test_login_failed():

    logger = Logger().get_logger()

    # Step 1: Open Web page in Edge Application
    logger.info("Step 1:")
    driver = WebDriver()
    driver.go_to("https://www.saucedemo.com/")
    logger.info("Web page opened")

    # Step 2: Enter values in Username and Password fields
    logger.info("Step 2:")
    username_input = driver.find(By.ID, value="user-name")
    password_input = driver.find(By.ID, value="password")
    username_input.send_keys(ENTERED_USERNAME)
    logger.info("Username entered")
    password_input.send_keys(ENTERED_PASSWORD)
    logger.info("Password entered")

    time.sleep(3)

    # Step 3: Press Login button
    logger.info("Step 3:")
    login_button = driver.find(By.ID, value="login-button")
    login_button.click()
    logger.info("Login button pressed")

    # Step 4: Check Warning
    logger.info("Step 4:")
    # Check Login failure warning is present
    try:
        warning_element = driver.find(By.CLASS_NAME, value="error-message-container")
        logger.info("Warning is present. Login failed")

    except NoSuchElementException:
        logger.error("Warning is absent")
        pytest.fail()

    # Check warning text
    try:
        warning_text = driver.find(By.CSS_SELECTOR, value='h3[data-test="error"]')
        logger.info("Text is present")

        # Verify warning text is valid
        if warning_text.text in WARNING_MESSAGES:
            logger.info("Valid Warning Message")
        else:
            logger.error("Invalid Warning Message")
            pytest.fail()

    except NoSuchElementException:
        logger.error("Text is absent")
        pytest.fail()

    time.sleep(3)
