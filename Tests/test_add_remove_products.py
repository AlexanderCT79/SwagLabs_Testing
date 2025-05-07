import pytest
import time
import random
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


def test_add_remove_products():

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

    # Step 4: Add Products
    logger.info("Step 4:")

    # Get items from inventory
    inventory_items = driver.find_various(By.CLASS_NAME, value="inventory_item")
    logger.info("Items in Inventory:")
    inventory_titles = []
    for item in inventory_items:
        title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        inventory_titles.append(item.find_element(By.CLASS_NAME, "inventory_item_name").text)
        logger.info(title)

    # Grab random items from inventory and add to cart
    selected_titles = []
    selected_items = random.sample(inventory_items, k=2)
    for item in selected_items:
        selected_titles.append(item.find_element(By.CLASS_NAME, "inventory_item_name").text)

    time.sleep(3)

    for item in selected_items:
        item_button = item.find_element(By.TAG_NAME, "button")
        item_button.click()
        logger.info(f'Article added to the cart: '
                    f'{item.find_element(By.CLASS_NAME, "inventory_item_name").text}')
        time.sleep(3)

    # Step 5: Go to Cart
    logger.info("Step 4:")
    shopping_cart_button = driver.find(By.CLASS_NAME, value="shopping_cart_container")
    shopping_cart_button.click()
    logger.info("Shopping Cart button pressed")
    time.sleep(3)

    # Step 6: Check products are added to cart
    logger.info("Step 6:")

    # Get items from shopping cart
    cart_items = driver.find_various(By.CLASS_NAME, value="cart_item")
    logger.info("Items in Cart:")
    cart_titles = []
    for item in cart_items:
        title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        cart_titles.append(item.find_element(By.CLASS_NAME, "inventory_item_name").text)
        logger.info(title)

    for item in selected_titles:
        if item in cart_titles:
            logger.info(f'Item added correctly: {item}')
        else:
            logger.error("Item was not added")
            pytest.fail()

    # Step 7: Remove item from cart
    logger.info("Step 7:")
    item_to_remove = random.sample(cart_items, k=1)[0]
    remove_button = item_to_remove.find_element(By.TAG_NAME, "button")
    remove_button.click()
    time.sleep(3)

    # Step 8: Check item is removed
    logger.info("Step 8:")
    cart_items = driver.find_various(By.CLASS_NAME, value="cart_item")
    logger.info(item_to_remove)
    logger.info(cart_items)

    if item_to_remove in cart_items:
        logger.info("Item was not removed")
        pytest.fail()
    else:
        logger.error("Item was removed successful")
