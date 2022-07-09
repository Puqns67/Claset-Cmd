# -*- coding: utf-8 -*-
"""
# Claset-Cmd
基于 Python 的 Minecraft 启动管理器的命令行前端, 未完成
"""

__author__ = "Puqns67"
__productname__ = "Claset-Cmd"
__version__ = "0.1.0"
__build__ = 2
__fullversion__ = __version__ + "_" + str(__build__)

from . import Utils
from .CmdMainClass import CmdMainClass

__all__ = Utils.__all__ + ("CmdMainClass",)
