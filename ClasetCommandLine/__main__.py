# -*- coding: utf-8 -*-
#! /usr/bin/python

from sys import version, exit
from platform import uname
from time import time

from . import __fullversion__
from .Utils.I18n import getI18nProcessor
from .Utils.ArgumentParsers import addArgumentToParsers
from .CmdMainClass import CmdMainClass

import Claset


def main(Debug: bool = False):
    # 启动 Claset
    StartTime = time()

    # 启用日志功能
    if Debug:
        Claset.setLoggerHandler(Stream="DEBUG", File="DEBUG")
    else:
        Claset.setLoggerHandler(Stream="WARNING")
    Claset.ProcessLogs()
    Claset.GolbalLogger.info("Starting Claset-Cmd...")
    Claset.GolbalLogger.info(
        "Claset-Core - Version: %s, Claset-Cmd - Version: %s, Powered By Python %s", Claset.__fullversion__, __fullversion__, version
    )
    Claset.GolbalLogger.info('Running in "%s"', " ".join(uname()))

    i18nProcessor = getI18nProcessor()

    addArgumentToParsers(i18nProcessor=i18nProcessor)

    MainClass = CmdMainClass()
    MainClass.setI18nProcessor(Method=i18nProcessor)

    # 进入命令循环
    Return = MainClass.cmdloop()

    # 退出程序
    Claset.GolbalLogger.info(
        "Stopping Claset, running time as %s, returned %s", time() - StartTime, Return
    )
    exit(Return)


if __name__ == "__main__":
    main()
