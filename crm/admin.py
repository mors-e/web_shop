from django.contrib import admin
from .models import Order, StatusCrm, CommentsCrm


class Comment(admin.StackedInline):
    model = CommentsCrm
    fields = ('comments_data', 'comments_text', )
    readonly_fields = ('comments_data',)
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_data')
    list_display_links = ('id', 'order_name')
    list_filter = ('order_status',)
    search_fields = ('id', 'order_name', 'order_phone', 'order_data')
    list_editable = ('order_status', 'order_phone')
    list_per_page = 10
    fields = ('id', 'order_status', 'order_data', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_data')
    # поле класса комментарий
    inlines = [Comment]


admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(CommentsCrm)