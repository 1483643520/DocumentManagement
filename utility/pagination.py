#!/user/bin/evn Python3 
# -*- coding:utf-8 -*-
# project:PyCharm
# pagination.py
# 从新定义分页
# author:ZhaoHeXin
# creation 2020/1/20--9:19


from rest_framework.pagination import PageNumberPagination


class ManualPageNumberPagination(PageNumberPagination):
    # 覆盖前端参数key值
    # page_query_param = 'p'
    # 前端可以指定每页最大数据量
    max_page_size = 100
    # 指认每一页数据条数
    page_size = 5
    # 覆盖指认每页数据条数的key值
    # page_size_query_param = 's'
