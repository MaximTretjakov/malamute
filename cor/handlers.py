from __future__ import annotations
from typing import Any
import subprocess

from cor.base_handler import AbstractHandler
from helper.git import download_project
from helper.common import unzip_project
from helper.log import malamute_logger


class GitHandler(AbstractHandler):
    def handle(self, request: Any):
        try:
            if request:
                download_project(request)
                unzip_project(request)
                super().handle(request)
            else:
                return super().handle(request)
        except Exception as e:
            malamute_logger.error(e)


class BuildHandler(AbstractHandler):
    def handle(self, request: Any):
        try:
            if request:
                process = subprocess.Popen(request['build_script_path'], cwd=request['cwd'])
                stdout, stderr = process.communicate()
                print(f'build handler says : {stdout} | {stderr}')
            else:
                return super().handle(request)
        except Exception as e:
            malamute_logger.error(e)


class DeployHandler(AbstractHandler):
    def handle(self, request: Any):
        try:
            if request == "MeatBall":
                return f"Dog: I'll eat the {request}"
            else:
                return super().handle(request)
        except Exception as e:
            malamute_logger.error(e)
