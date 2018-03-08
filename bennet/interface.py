#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (C) 2018 Christian Pfarr

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
from abc import ABC, abstractmethod
from logging import getLogger


class AbstractClass(ABC):
    """
    Abstract base class
    """

    def __init__(self):
        super().__init__()
        self._log = getLogger(self.__class__.__qualname__)

    @property
    def log(self):
        """
        Return the Logger

        :return: Logger object
        :rtype: Logger
        """
        return self._log


class AbstractConfig(AbstractClass):
    """
    Abstract base class for config
    """

    def __init__(self):
        super().__init__()


class AbstractParser(AbstractClass):
    """
    Abstract base class for config parser.
    """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def parse(self, file_name: str):
        """
        Parse the configuration file into a valid configuration object.

        :param file_name: a valid path to the filename
        :type file_name: str
        :return: a new configuration object
        :rtype: AbstractConfig
        """
        pass


class AbstractException(AbstractClass, Exception):
    """
    Abstract base class for exceptions
    """

    def __init__(self, message: str):
        super().__init__(message)
        self._message = message

    def handle(self):
        """
        Handles the exception.

        :raise: AbstractException
        """
        self.log.exception(self._message)
        raise self
