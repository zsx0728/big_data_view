# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from show1Model.models import show1_month_plan
 
# 数据库操作
def completedb():
    # 获取单个对象
    response = show1_month_plan.objects.get(id=1) 
    return response.complete

def plandb():
    # 获取单个对象
    response = show1_month_plan.objects.get(id=1) 
    return response.plan
