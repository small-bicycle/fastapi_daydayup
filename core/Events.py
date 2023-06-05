#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : Events.py
@Author: YuanMing
@Email : 15797642529@163.com
@Date  : 2023/6/5
@Desc  :  fastapi 事件监听
'''

from typing import Callable
from fastapi import FastAPI


def startup(app: FastAPI) -> Callable:
    """
    FastApi 启动完成事件
    :param app: FastAPI
    :return: start_app
    """

    async def app_start() -> None:
        # APP启动完成后触发
        print("fastapi已启动")
        pass

    return app_start


def stopping(app: FastAPI) -> Callable:
    """
    FastApi 停止事件
    :param app: FastAPI
    :return: stop_app
    """

    async def stop_app() -> None:
        # APP停止时触发
        print("fastapi已停止")

    return stop_app
