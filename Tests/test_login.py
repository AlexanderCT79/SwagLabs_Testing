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

ENTERED_USERNAME = "standard_user"
ENTERED_PASSWORD = "secret_sauce"


def test_login():

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

    # Check Username and Password are valid
    username_value = username_input.get_attribute("value")

    password_value = password_input.get_attribute("value")

    if username_value in VALID_USERNAMES:
        logger.info("Valid Username")
    else:
        logger.error("Invalid Username")
        pytest.fail()

    if password_value == VALID_PASSWORD:
        logger.info("Valid Password")
    else:
        logger.error("Invalid Password")
        pytest.fail()

    # Step 3: Press Login button
    logger.info("Step 3:")
    login_button = driver.find(By.ID, value="login-button")
    login_button.click()
    logger.info("Login button pressed")

    # Check Login was successful
    try:
        inventory_element = driver.find(By.CLASS_NAME, value="inventory_list")
        logger.info("Login successful")

    except NoSuchElementException:
        logger.error("Login failed")
        pytest.fail()

    time.sleep(3)


