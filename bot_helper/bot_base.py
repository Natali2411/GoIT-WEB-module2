from abc import ABC, abstractmethod
from typing import Tuple, List

from bot_helper.save_data.save_base import SaveBase


class BotBase(ABC):
    """
    SaveBot abstract class.
    """

    def __init__(self, data_save_tool: SaveBase):
        self.data_save_tool = data_save_tool


    @staticmethod
    @abstractmethod
    def input_error(func: callable) -> callable:
        ...

    @abstractmethod
    def parse_command(self, _input: str) -> Tuple[str, callable, List[str]]:
        ...

    @abstractmethod
    def hello(self) -> str:
        ...

    @abstractmethod
    def add_contact(self, *args) -> str:
        ...

    @abstractmethod
    def delete_contact(self, *args) -> str:
        ...

    @abstractmethod
    def change_phone(self, *args) -> str:
        ...

    @abstractmethod
    def update_birthday(self, *args) -> str:
        ...

    @abstractmethod
    def find_contact_phone(self, *args) -> str:
        ...

    @abstractmethod
    def show_all(self, *args) -> str:
        ...

    @abstractmethod
    def search_contact(self, *args) -> str:
        ...

    @abstractmethod
    def add_phone(self, *args) -> str:
        ...

    @abstractmethod
    def add_address(self, *args) -> str:
        ...

    @abstractmethod
    def add_email(self, *args) -> str:
        ...

    @abstractmethod
    def change_email(self, *args) -> str:
        ...

    @abstractmethod
    def change_address(self, *args) -> str:
        ...

    @abstractmethod
    def change_name(self, *args) -> str:
        ...

    @abstractmethod
    def good_bye(self) -> str:
        ...

    @abstractmethod
    def show_days_to_birthday(self, *args) -> str:
        ...

    @abstractmethod
    def upcoming_birthdays(self, *args) -> str:
        ...

    @abstractmethod
    def unknown(self) -> str:
        ...

    @abstractmethod
    def help_command(self) -> str:
        ...
