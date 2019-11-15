from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Category,Post,Tag
from .adminforms import PostAdminForm
from custom_site import custom_site
from base_admin import BaseOwnerAdmin

# Register your models here.

@admin.register(Category,site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    # inlines = ['PostInline',]
    list_display = ('name','status','is_nav','created_time','post_count')
    fields = ('name','status','is_nav')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request,obj,form,change)

    def post_count(self,obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'
@admin.register(Tag,site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name','status','created_time')
    fields = ('name','status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


class CategoryOwnerFilter(admin.SimpleListFilter):
    """定义自定义过滤器"""
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset

@admin.register(Post,site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm


    exclude = ('owner',)
    filter_horizontal = ('tag',)#横向展示
    # filter_vertical = ('tag',)#纵向展示
    list_display = ['title','category','status','created_time','owner']
    list_display_links = []
    list_filter = [CategoryOwnerFilter]
    search_fields = ['title','category']

    actions_on_top = True
    actions_on_bottom = True

    # save_on_top = True保存在定不显示

    # fields = (
    #     ('category','title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )

    fieldsets = (
        ('基础配置',{
            'description':'基础配置描述',
            'fields':(
                ('title','category'),
                'status',
            ),

        }),

        ('内容',{
            'fields':(
                'desc',
                'content',
            )
        }),

        ('额外信息',{
            'classes':('collapse',),
            'fields':('tag',),
        }),
    )

    #自定义方法展示自定义字段   ??????
    def operator(self,obj):
        return format_html(
            '<a href="{}"> 编辑 </a>',
            reverse('admin:bolg_post_change',args=(obj.id,))
        )
    operator.short_description = '操作'#指定表头的展示文案

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin,self).save_model(request,obj,form,change)
    def get_queryset(self,request):
        qs = super(PostAdmin,self).get_queryset(request)
        return qs.filter(owner=request.user)

# class PostInline(admin.TabularInline):
#     fields = ('title','desc')
#     extra = 1
#     model = Post


 # class Media:
    #     css = {
    #         'all':('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css',),
    #
    #     }
    #     js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)



















