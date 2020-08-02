from __future__ import annotations
from typing import Any
import subprocess
import asyncio
import os

from cor.base_handler import AbstractHandler
from helper.git import git


class GitHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request:
            asyncio.run(git.main(request), debug=True)
            super().handle(request)
        else:
            return super().handle(request)


class BuildHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request:
            path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            result = subprocess.run([path + '\\build_project.bat'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return f"BuildHandler says: {result.stdout} : {result.stderr}"
        else:
            return super().handle(request)


class DeployHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)
