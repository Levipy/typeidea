from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS=(
        (STATUS_DELETE,'删除'),
        (STATUS_NORMAL,'正常'),
    )
    title = models.CharField(max_length=50,verbose_name='标题')
    href = models.URLField(verbose_name='链接')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS,verbose_name='状态',default=STATUS_NORMAL)
    weight = models.PositiveIntegerField(default=1,choices=zip(range(1,6),range(1,6)),verbose_name='权重',
                                         help_text='权重高展示顺序靠前')
    owner = models.ForeignKey(User,verbose_name='作者',on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class Meta:
        #db_table = 'Link'
        verbose_name = verbose_name_plural = '友链'

    def __str__(self):
        return self.name

class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_HIDE,'隐藏'),
        (STATUS_SHOW,'展示'),
    )
    SIDE_TYPE = (
        (1,'html'),
        (2,'最新文章'),
        (3,'最热文章'),
        (4,'最近评论'),
    )
    title = models.CharField(max_length=50,verbose_name='标题')
    display_type = models.PositiveIntegerField(default=1,choices=SIDE_TYPE,verbose_name='展示类型')
    content = models.CharField(max_length=500,blank=True,verbose_name='内容',help_text='如果展示的不是Html类型，可为空')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS,verbose_name='状态',default=STATUS_SHOW)
    owner = models.ForeignKey(User, verbose_name='作者',on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        #db_table = 'Side_Bar'
        verbose_name = verbose_name_plural = '侧边栏'

    def __str__(self):
        return self.name










