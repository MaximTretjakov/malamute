from __future__ import annotations
from typing import Any
import subprocess

from cor.base_handler import AbstractHandler
from helper.git import git
from helper.common import unzip_project


class GitHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request:
            git.download_project(request)
            unzip_project(request)
            super().handle(request)
        else:
            return super().handle(request)


class BuildHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request:
            result = subprocess.run([request['build_script_path']], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return f"BuildHandler says: {result.stdout} : {result.stderr}"
        else:
            return super().handle(request)


class DeployHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)
