#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : Base.py
@Author: YuanMing
@Email : 15797642529@163.com
@Date  : 2023/6/5
@Desc  : 基本路由
'''
from fastapi import APIRouter, Request

router = APIRouter()


@router.get('/')
async def home(req: Request):
    return 'fastapi'
