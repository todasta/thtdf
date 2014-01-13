from django.contrib import admin
from .models import Post, Image, Category

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('title', 'created', 'modified', 'status', 'adopted')
    list_filter = ('categories', 'modified', 'status', 'adopted')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    radio_fields = {"status": admin.HORIZONTAL}
    date_hierarchy = 'created'
    filter_horizontal = ('categories',)

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
