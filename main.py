from PyQt5.QtCore import QThread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from PyQt5.QtWidgets import QApplication, QLabel

import keyboard

import time

import web_config
import gui

driver = webdriver.Chrome()


class Worker(QThread):
    def run(self):
        init()
        main()


def init():
    init_qt()
    gui.init()
    init_chrome()


def init_chrome():
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 980

    driver.set_window_position(SCREEN_WIDTH / 2 - 170, 0)
    driver.set_window_size(SCREEN_WIDTH / 2 + 170, SCREEN_HEIGHT)
    driver.get("https://www.hometax.go.kr/")


def init_qt():
    app = QApplication([])
    label = QLabel('Hello World!')
    label.show()


def main():
    while True:
        if is_alert_present():
            alert_handler()

        if keyboard.is_pressed("F4"):
            action_goto_new()
            print("F7")

        if keyboard.is_pressed("F7"):
            action_goto_list()
            print("F7")

        if keyboard.is_pressed("F8"):
            print("F8")

        if keyboard.is_pressed("F9"):
            print("F9")

        if keyboard.is_pressed("F10"):
            print("F10")
            logout_and_login()

        time.sleep(0.01)
        # print(web_config.config.wanna_alert_kill)


def is_alert_present():
    try:
        check_alert = driver.switch_to.alert  # check Alert
        return True
    except Exception:
        return False


def alert_handler():
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
        alert_handler()
        # wait
        wait = WebDriverWait(driver, 1000)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "로그인")))

    hometax_login()


def action_goto_new():
    try:
        button_click(driver.find_element(By.ID, "menuAtag_0104010100"))
    except:
        print("F10 Except")


def action_goto_total_page():
    try:
        button_click(driver.find_element(By.ID, "menuAtag_0104030200"))
    except:
        print("F10 Except")


def action_goto_list():
    try:
        button_click(driver.find_element(By.ID, "menuAtag_0104020100"))
    except:
        print("F10 Except")


if __name__ == "__main__":
    # execute only if run as a script
    init()
    main()
