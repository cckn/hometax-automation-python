class Web:
    alert_off: bool = True

    @staticmethod
    def toggle_alert() -> None:
        Web.alert_off = not Web.alert_off
