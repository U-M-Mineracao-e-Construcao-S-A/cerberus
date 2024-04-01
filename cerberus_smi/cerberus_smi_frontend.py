

from textual.app import App, ComposeResult
from textual.widgets import Footer, TabbedContent, Header, Button, Static
from textual.containers import Container, Horizontal, Vertical

from cerberus_smi.cerberus_smi_backend import CerberusSMIBackend
from cerberus_smi.cerberus_smi_widgets import *
from cerberus_smi import constants



QUESTION = "Do you want to learn about Textual CSS?"


class CerberusSMIFrontend(App):

    BINDINGS = [
        ("q, Q", "quit", "Quit"),
        ("h, H", "help", "Help"),
        ("d, D", "toggle_dark", "Toggle dark mode"),
        ("1", "tab_one", "Runners"),
        ("2", "tab_two", "DUT"),
        ("3", "tab_three", "HIL"),
    ]

    
    CSS_PATH = ["cerberus_smi_style.tcss", "foo.tcss"]
    
    def __init__(self,
            backend: CerberusSMIBackend = None,
            app_name: str = "CERBERUS-SMI",
            app_version: str = "0.0.1",
        ):

        super().__init__()
        self.app_name = app_name
        self.app_version = app_version        
        self.backend = backend

        
        print('Init App')

    def compose(self) -> ComposeResult:
        # yield Header()
        # yield Footer()
        # yield Container(
        #     Static(QUESTION, classes="question"),
        #     Horizontal(
        #         Button("Yes", variant="success"),
        #         Button("No", variant="error"),
        #         classes="buttons",
        #     ),
        #     id="dialog",
        # )

        yield TTHeader(self.app_name, self.app_version)
        with Container(id="app_grid"):
            with Vertical(id="left_col"):
                yield TTMenu(id="host_info", title="Host Info", data={"foo":"foo1"})
                yield TTCompatibilityMenu(
                    id="compatibility_menu",
                    title="Compatibility Check",
                    data={"foo":"foo1"}
                )
                yield TTMenu(
                    id="sw_ver_menu",
                    title="Latest SW Versions",
                    data={"foo":"foo1"}
                )
            with TabbedContent(
                "Information (1)", "Telemetry (2)", "FW Version (3)", id="tab_container"
            ):
                yield TTDataTable(
                    title="Device Information",
                    id="tt_smi_device_info",
                    header=constants.RUNNERS_TABLE_HEADER,
                    header_height=2,
                )
                yield TTDataTable(
                    title="Device Telemetry",
                    id="tt_smi_telem",
                    header=constants.DUT_TABLE_HEADER,
                    header_height=2,
                )
                yield TTDataTable(
                    title="Device Firmware Versions",
                    id="tt_smi_firmware",
                    header=constants.HIL_TABLE_HEADER,
                    header_height=2,
                )
        yield Footer()

