from django.db import models
from db.base_model import BaseModel
# 数据库中可总结为三种数据类型：数字，字符串，时间
# 字段类型定义在django.db.models.fields中，可通过models.Fields创建字段类型的对象。


# Create your models here.
class User(BaseModel):
    # 只有展示时才显示汉字
    SEX_CHOICE = (
        (0, "女"),
        (1, "男")
    )
    open_id = models.CharField(max_length=50, primary_key=True, verbose_name="用户标识")
    sex = models.SmallIntegerField(default=0, choices=SEX_CHOICE, verbose_name="性别")
    subscribe = models.SmallIntegerField(default=0, verbose_name="是否关注")
    subscribe_time = models.DateTimeField(auto_now=True, verbose_name="关注时间")

    # 内部类，用于设置元信息
    class Meta:
        db_table = "User_info"  # 设置表名
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


class Thing(BaseModel):
    open_id = models.ForeignKey("User", verbose_name="标识")
    id = models.AutoField(primary_key=True, verbose_name="事件编号")
    content = models.TextField(verbose_name="内容")
    time = models.DateTimeField(verbose_name="提醒时间")

    class Meta:
        db_table = "thing_info"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

