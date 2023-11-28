from abc import ABC, abstractmethod
from typing import Any


class SaveBase(ABC):
    """
    SaveBase abstract class.
    """

    def __init__(self, address: str):
        self.address = address

    @abstractmethod
    def save_info(self, path: str, data: dict) -> None:
        ...

    @abstractmethod
    def read_info(self, path: str) -> Any:
        ...
