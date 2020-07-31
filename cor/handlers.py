from __future__ import annotations
from typing import Any
import asyncio
import time

from cor.base_handler import AbstractHandler
from helper.git import git


class GitHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request:
            start = time.time()
            asyncio.run(git.main(request), debug=True)
            end = time.time()
            return f'Total time : {end - start:.2}'
        else:
            return super().handle(request)


class BuildHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DeployHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)
