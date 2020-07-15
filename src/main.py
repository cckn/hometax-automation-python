from os import error

import src.web_controller as web_controller
import keyboard
import time
import src.hometax as ht


def main():
    web = web_controller.WebController()
    web.init_chrome()

    turn_off_the_alert = True

    while True:

        if keyboard.is_pressed("F4"):
            web.action_button_click(ht.ID.건별발급)
            print("F7", str(ht.ID.건별발급))

        elif keyboard.is_pressed("F7"):
            web.action_button_click(ht.ID.발급목록)
            print("F7")

        elif keyboard.is_pressed("F8"):
            web.action_button_click(ht.ID.월분기별목록)
            print("F8")

        elif keyboard.is_pressed("F9"):
            turn_off_the_alert = not turn_off_the_alert
            print("알람", "켬" if turn_off_the_alert else "끔")
            time.sleep(1)

        elif keyboard.is_pressed("F10"):
            print("F10")
            web.logout_and_login_strategy()

        if turn_off_the_alert:
            web.alert_handler()

        time.sleep(0.01)


if __name__ == "__main__":
    main()
