from django.contrib import admin
from .models import ConstructionCategory, ConstructionProject, Images
import admin_thumbnails

# Register your models here.
class AdminConstructionCategory(admin.ModelAdmin):
    list_display = ('title', 'created_at',
                    'updated_at', 'image_tag')
    list_filter = ['title', 'status', 'created_at']
    list_per_page = 10
    search_fields = ['title']  
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(ConstructionCategory, AdminConstructionCategory)


@admin_thumbnails.thumbnail('image')
class ConstructionProjectImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 2
class AdminConstructionProject(admin.ModelAdmin):
    list_display = ('title', 'category',
                    'new_price', 'status', 'image_tag')
    list_filter = ['title', 'status', 'category']
    list_per_page = 10
    search_fields = ['title', 'category']
    inlines = [ConstructionProjectImageInline]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(ConstructionProject, AdminConstructionProject)