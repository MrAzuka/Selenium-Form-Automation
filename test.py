# Requirements: install python and use pip to install selenium
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
# Things to note
# The classes on this website are dynamically rendered,
# meaning that at the next time of running this script it is possible that they have changed
# There is need to always check before running the script,
# because every new deployment to the website changes some class names.
# Also everywhere "time.sleep()" is used is to give some seconds for the website to load

try:
    # Setting up driver
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    # Fetching the web page
    driver.get("https://9ijakids.gamequiz.live/")
    # expanding the browser
    driver.maximize_window()

    # Click on the login link
    links = driver.find_elements(By.XPATH, "//a[contains(@class, 'navMenus')]")
    for link in links:
        if "Login" in link.get_attribute("innerHTML"):
            link.click()
            break

    # Click on the child button
    buttonLinks = driver.find_element(
        By.XPATH, "//div[contains(@class, 'Login_switchButtonWrap__RwJ8I')][.//button[text()[contains(., 'Child')]]]")
    buttonLinks.click()

    # Get all the input fields
    inputField = driver.find_elements(
        By.XPATH, "//input[contains(@class, 'Login_childOTP__3rkto')]")

    # send code 995007
    inputField[0].send_keys("9")
    inputField[1].send_keys("9")
    inputField[2].send_keys("5")
    inputField[3].send_keys("0")
    inputField[4].send_keys("0")
    inputField[5].send_keys("7")

    # Click on the login button
    buttonLinks = driver.find_element(
        By.XPATH, "//div[contains(@class, 'Login_button__bskDi')]")
    buttonLinks.click()

    # Wait for section cards to appear
    wait = WebDriverWait(driver, 10)
    sectionCards = wait.until(EC.visibility_of_all_elements_located(
        (By.XPATH, "//section[contains(@class, 'CDD-featureCard')]")))

    # Get all event cards on the dashboard
    div_tags = sectionCards[0].find_elements(
        By.XPATH, ".//div[contains(@class, 'featureCard_featureTitle__oZm1v')]")

    # select all event card
    div_tags[0].click()
    time.sleep(5)
    div_tags[1].click()
    time.sleep(5)
    div_tags[2].click()
    time.sleep(5)
    div_tags[0].click()

    # Click on the leaderboard link
    time.sleep(5)
    leaderboardLink = driver.find_elements(
        By.XPATH, "//a[contains(@class, 'navMenus')]")
    for link in leaderboardLink:
        if "Leaderboard" in link.get_attribute("innerHTML"):
            link.click()
            break

    time.sleep(10)

    # Click on overall leaderboard
    overallLeaderboard = driver.find_elements(
        By.XPATH, "//div[contains(@class, 'L-toggles')][.//div[text()[contains(., 'Overall Leaderboard')]]]")
    for link in overallLeaderboard:
        link.click()
        print(link.get_attribute("innerHTML"))
        break
    time.sleep(5)

    # Click on dashboard again
    dashboardLink = driver.find_elements(
        By.XPATH, "//a[contains(@class, 'navMenus')]")
    for link in dashboardLink:
        if "Dashboard" in link.get_attribute("innerHTML"):
            link.click()
            break

    time.sleep(10)
    # Logout
    logoutLink = driver.find_elements(
        By.XPATH, "//div[text()[contains(., 'Logout')]]")
    logoutLink[0].click()

    print("Automation Done")
    time.sleep(7)
    driver.close()

except Exception as e:
    logging.error(e)
    print(f"Error message: ${e}")
    sys.exit(1)
