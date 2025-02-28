from rich.panel import Panel


class HarlequinExit(Exception):
    pass


class HarlequinError(Exception):
    def __init__(self, msg: str, title: str = "") -> None:
        super().__init__(msg)
        self.msg = msg
        self.title = title


class HarlequinConnectionError(HarlequinError):
    pass


class HarlequinCopyError(HarlequinError):
    pass


class HarlequinQueryError(HarlequinError):
    pass


class HarlequinThemeError(HarlequinError):
    pass


class HarlequinConfigError(HarlequinError):
    pass


class HarlequinWizardError(HarlequinError):
    pass


class HarlequinTzDataError(HarlequinError):
    pass


def pretty_print_error(error: HarlequinError) -> None:
    from rich import print

    print(pretty_error_message(error))


def pretty_error_message(error: HarlequinError) -> Panel:
    return Panel.fit(
        str(error),
        title=error.title if error.title else ("Harlequin encountered an error."),
        title_align="left",
        border_style="red",
    )
