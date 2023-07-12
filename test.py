from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
import sys
import time

logging.basicConfig(
    filename=os.getcwd() + '/error.log', level=logging.ERROR)

try:
    # Setting up driver
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    # Fetching the web page
    driver.get("https://9ijakids.gamequiz.live/")
    driver.maximize_window()

    # Click on the login link
    links = driver.find_elements(By.XPATH, "//a[contains(@class, 'navMenus')]")
    for link in links:
        if "Login" in link.get_attribute("innerHTML"):
            link.click()
            break

    # Click on the child button
    buttonLinks = driver.find_element(
        By.XPATH, "//div[contains(@class, 'Login_switchButtonWrap__WCJs3')][.//button[text()[contains(., 'Child')]]]")
    buttonLinks.click()

    input_fields = driver.find_elements(
        By.XPATH, "//input[contains(@class, 'Login_childOTP__L-Idf')]")

    # send code 995007
    input_fields[0].send_keys("9")
    input_fields[1].send_keys("9")
    input_fields[2].send_keys("5")
    input_fields[3].send_keys("0")
    input_fields[4].send_keys("0")
    input_fields[5].send_keys("7")

    # Click on the submit button
    buttonLinks = driver.find_element(
        By.XPATH, "//div[contains(@class, 'Login_button__BgVdC')]")
    buttonLinks.click()
    # Wait for section cards to appear
    wait = WebDriverWait(driver, 10)
    sectionCards = wait.until(EC.visibility_of_all_elements_located(
        (By.XPATH, "//section[contains(@class, 'CDD-featureCard')]")))

    # Tags for each element
    div_tags = sectionCards[0].find_elements(
        By.XPATH, ".//div[contains(@class, 'featureCard_featureTitle__gOjhJ')]")

    # select all event card
    div_tags[0].click()
    time.sleep(5)
    div_tags[1].click()
    time.sleep(5)
    div_tags[2].click()
    time.sleep(5)
    div_tags[0].click()

    # Tags for each quest on the current events
    # card_tags = driver.find_elements(
    #     By.XPATH, ".//div[contains(@class, 'featureCard_active__Bf8Ii')]")

    # print(card_tags[0].get_attribute("innerHTML"))
    # Find all quest tags
    quest_tags = driver.find_elements(
        By.XPATH, "//div[contains(@class, 'quests-container')]"
    )
    for tag in quest_tags:
        play_buttons = tag.find_elements(
            By.XPATH, ".//div[contains(@class, 'quests-buttonWrap')][.//button[text()[contains(., 'Play')]]]"
        )
        for play_button in play_buttons:
            if play_button.is_enabled():
                play_button.click()
                # Wait 30 seconds before closing
                time.sleep(30)
                close_button = wait.until(EC.visibility_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'gameTopBar_container__Ol3mh')][.//button[text()[contains(., 'Close')]]]")))
                close_button.click()
            else:
                print("Quest disabled")

    print("Automation Done")

except Exception as e:
    logging.error(e)
    sys.exit(1)
