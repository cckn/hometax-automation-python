import src.web_controller as web_controller
import keyboard
import time


def main():
    web = web_controller.WebController()
    web.init_chrome()
    while True:

        if keyboard.is_pressed("F4"):
            web.action_button_click("건별발급")
            print("F7")

        elif keyboard.is_pressed("F7"):
            web.action_button_click("발급목록조회")
            print("F7")

        elif keyboard.is_pressed("F8"):
            web.action_button_click("월/분기별 목록조회")
            print("F8")

        elif keyboard.is_pressed("F9"):
            web.action_button_click("월/분기별 목록조회")
            print("F9")

        elif keyboard.is_pressed("F10"):
            print("F10")
            web.logout_and_login_strategy()

        web.alert_handler()

        time.sleep(0.01)


if __name__ == "__main__":
    main()
