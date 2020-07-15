import time
import keyboard

import src.config as config
import src.web.hometax as ht


def handler(web):
    if keyboard.is_pressed("F4"):
        web.action_button_click(ht.ID.건별발급)

    elif keyboard.is_pressed("F7"):
        web.action_button_click(ht.ID.발급목록)

    elif keyboard.is_pressed("F8"):
        web.action_button_click(ht.ID.월분기별목록)

    elif keyboard.is_pressed("F9"):
        config.Web.toggle_alert()
        print("알람", "자동 끔" if config.Web.alert_off else "켬")
        time.sleep(0.5)

    elif keyboard.is_pressed("F10"):
        print("F10")
        web.logout_and_login_strategy()
