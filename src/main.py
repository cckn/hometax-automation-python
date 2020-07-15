import time
import sentry_sdk

import src.key_handler as key_handler
import src.config as config
import src.web.controller as web_controller

sentry_sdk.init("https://5901248f3e404f26a23cf974eacdc523@o289916.ingest.sentry.io/5338690")


def main() -> None:
    web = web_controller.WebController()
    web.init_chrome()

    while True:

        key_handler.handler(web)

        if config.Web.alert_off:
            web.alert_handler()

        time.sleep(0.01)


if __name__ == "__main__":
    main()
