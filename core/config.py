import os
import json
import logging
from json import JSONDecodeError
from typing import Dict, NoReturn, AnyStr

from core.errors import EmptyConfigError

logger = logging.getLogger('malamute_global_logger')


class Config:
    def __init__(self, conf_file_name):
        self._conf_file_name = conf_file_name

    def get_file_size(self) -> int:
        try:
            return os.path.getsize(self.get_conf_path())
        except FileNotFoundError as e:
            logger.debug(e)

    def read_from_conf(self) -> Dict:
        try:
            path = self.get_conf_path()
            if not self.get_file_size():
                raise EmptyConfigError(f'Config file {self.get_conf_path()} is empty or corrupted')
            with open(path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, JSONDecodeError, EmptyConfigError) as e:
            logger.debug(e)

    def write_to_conf(self, conf_obj) -> NoReturn:
        try:
            path = self.get_conf_path()
            with open(path, 'w') as f:
                json.dump(conf_obj, f, indent=4)
        except FileNotFoundError as e:
            logger.debug(e)

    def get_conf_path(self) -> AnyStr:
        current_dir = os.path.dirname(__file__)
        try:
            return os.path.join(current_dir + '\\config\\', self._conf_file_name)
        except OSError as e:
            logger.debug(e)


config = Config('malamute.json')
