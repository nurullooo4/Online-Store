from django.contrib import admin

from app_main.models import Product, Comment, Category, Cart, ProductImage

admin.site.register(Cart)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']
    # list_editable = ['old_price', 'new_price']
    save_on_top = True
    list_per_page = 3


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['owner', 'product', 'body']
    list_display_links = ['owner']
    search_fields = ['body', 'owner']
    list_editable = ['body']
    list_per_page = 1


