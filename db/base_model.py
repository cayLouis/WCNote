#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   base_model.py    
@Contact :   815569735@qq.com
@License :   (C)Copyright 2017-2018, Louis-NLPR-CASIA
@Modify Time :    2020/3/7 0007 14:52
@Author :    louis
@Version :    1.0
@Description :    None
"""

# import lib
from django.db import models


class BaseModel(models.Model):

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=False, verbose_name="删除标识")

    class Meta:
        abstract = True
