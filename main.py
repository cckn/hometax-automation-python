from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC

import pyautogui as pag
import keyboard

import time
import threading

# This example requires Selenium WebDriver 3.13 or newer

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 980

driver = webdriver.Chrome()
driver.set_window_position(1920 / 2 - 170, 0)
driver.set_window_size(1920 / 2 + 170, 1080)
# with as driver:
# wait = WebDriverWait(driver, 600)
driver.get("https://www.hometax.go.kr/")


# first_result = wait.until(presence_of_element_located(By.CSS_SELECTOR, "h3>div"))
# print(first_result.get_attribute("textContent"))

def is_alert_present():
    try:
        alert = driver.switch_to.alert
        return True
    except Exception:
        return False


def alert_close():
    alert = driver.switch_to.alert
    text = alert.text

    print("alert : " + text)
    alert.accept()


def has_hometax_login():
    try:
        driver.find_element(By.LINK_TEXT, "로그아웃")
        return True
    except:
        return False


def hometax_logout():
    try:
        driver.find_element(By.LINK_TEXT, "로그아웃").click()
    except Exception as e:
        print(e)


def hometax_login():
    try:
        driver.find_element(By.LINK_TEXT, "로그인").click()
    except Exception as e:
        print(e)


def button_click(element):
    driver.execute_script("arguments[0].click();", element)


def logout_and_login():
    if has_hometax_login():
        # logout button click
        hometax_logout()
        # confirm alert close
        alert_close()
        # wait
        wait = WebDriverWait(driver, 1000)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "로그인")))

    hometax_login()



def action_go_total_page():
    try:
        button_click(driver.find_element(By.ID, "menuAtag_0104030200"))
    except:
        print("F10 Except")


# alertKillerT = threading.Thread(target=is_alert_present)
# alertKillerT.start()
while True:
    if is_alert_present():
        alert_close()

    if keyboard.is_pressed("F4"):
        action_go_total_page()

    if keyboard.is_pressed("F7"):
        logout_and_login()

    if keyboard.is_pressed("F8"):
        print("F8")

    if keyboard.is_pressed("F9"):
        print("F9")

    if keyboard.is_pressed("F10"):
        print("F10")

    time.sleep(0.01)
