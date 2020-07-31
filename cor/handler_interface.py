from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    """
    Абстрактный интерфейс обработчика.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass
