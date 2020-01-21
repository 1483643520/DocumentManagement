from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import validate_comma_separated_integer_list


# Create your models here.


class User(models.Model):
    """
    存储用户信息表
    """
    # 性别分组
    Gender_ = ((1, "男"), (2, "女"), (3, "其他"))
    # 用户状态分组
    Status_ = ((1, "在用"), (2, "停用"))
    # 级别分组
    Level_ = ((1, "管理员"), (2, "普通用户"))
    user_name = models.CharField(help_text="用户名", verbose_name="用户名", max_length=10)
    nickname = models.CharField(help_text="昵称", verbose_name="昵称", max_length=50, default="", blank=True, null=True)
    gender = models.IntegerField(help_text="性别:1男、2女，3其他", verbose_name="性别", choices=Gender_)
    phone = PhoneNumberField(help_text="电话", verbose_name="电话", default="", blank=True, null=True)
    email = models.EmailField(help_text="邮箱", verbose_name="邮箱")
    status = models.IntegerField(help_text="在用状态:1在用、2停用", verbose_name="在用状态")
    level = models.IntegerField(help_text="用户级别:1管理员、2普通用户", verbose_name="用户级别")
    last_time = models.DateTimeField(help_text="上次登录时间", verbose_name="上次登录时间")
    superior_role = models.CharField(help_text="所关联角色", verbose_name="所关联角色", max_length=255,
                                     validators=[validate_comma_separated_integer_list], default="", blank=True,
                                     null=True)
    update_time = models.DateTimeField(help_text="上次修改时间", verbose_name="上次修改时间", auto_now=True)
    create_time = models.DateTimeField(help_text="创建时间", verbose_name="创建时间", auto_now_add=True)

    class Meta:
        db_table = "tb_user"
        verbose_name = "用户注册表"


class Directory(models.Model):
    """
    目录配置表
    """

    icon = models.CharField(help_text="菜单图标", verbose_name="菜单图标", max_length=50,
                            default="", blank=True, null=True)
    is_outside = models.BooleanField(help_text="是否为外链接:true/false", verbose_name="是否为外部链接")
    is_show = models.BooleanField(help_text="非管理员是否可见:true/false", verbose_name="非管理员是否可见")
    name = models.CharField(help_text="菜单名称", verbose_name="菜单名称", max_length=50)
    url = models.CharField(help_text="路由地址", verbose_name="路由地址", max_length=255)
    sort = models.IntegerField(help_text="菜单顺序", verbose_name="菜单顺序", default=999, blank=True, null=True)
    superior = models.IntegerField(help_text="上级菜单ID", verbose_name="上级菜单ID", default=0, blank=True, null=True)
    update_time = models.DateTimeField(help_text="上次修改时间", verbose_name="上次修改时间", auto_now=True)
    create_time = models.DateTimeField(help_text="创建时间", verbose_name="创建时间", auto_now_add=True)

    class Meta:
        db_table = "tb_directory"
        verbose_name = "目录配置表"


class Menu(models.Model):
    """
    菜单配置表
    """

    icon = models.CharField(help_text="菜单图标", verbose_name="菜单图标", max_length=50,
                            default="", blank=True, null=True)
    is_outside = models.BooleanField(help_text="是否为外链接:true/false", verbose_name="是否为外部链接")
    is_show = models.BooleanField(help_text="非管理员是否可见:true/false", verbose_name="非管理员是否可见")
    is_cache = models.BooleanField(help_text="是否菜单缓存:true/false", verbose_name="是否菜单缓存")
    name = models.CharField(help_text="菜单名称", verbose_name="菜单名称", max_length=50)
    authority = models.CharField(help_text="权限标识", verbose_name="权限标识", max_length=10)
    url = models.CharField(help_text="路由地址", verbose_name="路由地址", max_length=255)
    sort = models.IntegerField(help_text="菜单顺序", verbose_name="菜单顺序", default=999, blank=True, null=True)
    component_name = models.CharField(help_text="组件名称", verbose_name="组件名称", max_length=50)
    component_url = models.CharField(help_text="组件路径", verbose_name="组件路径", max_length=255)
    superior_directory = models.CharField(help_text="所关联目录ID", verbose_name="所关联目录ID", max_length=255,
                                          validators=[validate_comma_separated_integer_list], default="", blank=True,
                                          null=True)
    superior_button = models.CharField(help_text="所关联按钮", verbose_name="所关联按钮", max_length=255,
                                       validators=[validate_comma_separated_integer_list], default="", blank=True,
                                       null=True)
    update_time = models.DateTimeField(help_text="上次修改时间", verbose_name="上次修改时间", auto_now=True)
    create_time = models.DateTimeField(help_text="创建时间", verbose_name="创建时间", auto_now_add=True)

    class Meta:
        db_table = "tb_menu"
        verbose_name = "菜单配置表"


class Button(models.Model):
    """
    按钮配置表
    """
    name = models.CharField(help_text="按钮名称", verbose_name="按钮名称", max_length=50)
    authority = models.CharField(help_text="权限标识", verbose_name="权限标识", max_length=10)
    sort = models.IntegerField(help_text="按钮顺序", verbose_name="按钮顺序", default=999, blank=True, null=True)
    update_time = models.DateTimeField(help_text="上次修改时间", verbose_name="上次修改时间", auto_now=True)
    create_time = models.DateTimeField(help_text="创建时间", verbose_name="创建时间", auto_now_add=True)

    class Meta:
        db_table = "tb_button"
        verbose_name = "按钮配置表"


class UserRole(models.Model):
    """
    角色配置表
    关联用户、关联功能配置
    """
    # 定义数据查询范围权限
    DataAuthority_ = ((1, "所有数据"), (2, "当前用户数据"))
    name = models.CharField(help_text="角色名称", verbose_name="角色名称", max_length=50)
    data_authority = models.CharField(help_text="数据权限", verbose_name="数据权限",
                                      max_length=1, choices=DataAuthority_)
    role_authority = models.CharField(help_text="角色权限", verbose_name="角色权限", max_length=10)
    sort = models.IntegerField(help_text="角色顺序", verbose_name="角色顺序", default=999, blank=True, null=True)
    description = models.TextField(help_text="角色描述", verbose_name="角色描述", default="", blank=True, null=True)
    superior_menu = models.CharField(help_text="所配置菜单ID集合", verbose_name="所配置菜单ID集合", max_length=255,
                                     validators=[validate_comma_separated_integer_list], default="", blank=True,
                                     null=True)
    update_time = models.DateTimeField(help_text="上次修改时间", verbose_name="上次修改时间", auto_now=True)
    create_time = models.DateTimeField(help_text="创建时间", verbose_name="创建时间", auto_now_add=True)

    class Meta:
        db_table = "tb_user_role"
        verbose_name = "角色配置表"
