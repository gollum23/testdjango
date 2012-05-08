__author__ = 'SISTEMAS'

from semanario.models import Article, Author, Edition
from django.contrib import admin

class SvchAdmin(admin.ModelAdmin):
    list_display = ('title','abstract','order','edition')
    list_filter = ('edition__ed',)
    search_fields = ('title','author__name')

class SvchAuthor(admin.ModelAdmin):
    list_display = ('name','bio')
    ordering = ('-name',)

class SvchEdition(admin.ModelAdmin):
    list_display = ('ed','dfrom','color')

admin.site.register(Article, SvchAdmin)
admin.site.register(Author, SvchAuthor)
admin.site.register(Edition, SvchEdition)