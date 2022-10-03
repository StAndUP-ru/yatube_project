from django.contrib import admin

from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-' 

#class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
#    list_display = ('pk', 'text', 'pub_date', 'author') 
    # Добавляем интерфейс для поиска по тексту постов
#    search_fields = ('text',) 
    # Добавляем возможность фильтрации по дате
#    list_filter = ('pub_date',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка 
#    empty_value_display = '-пусто-'  

# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)  

class GroupAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'pk', 
        'title', 
        'slug', 
        'description') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('title',) 
    # Добавляем возможность фильтрации по дате
    #list_filter = ('pub_date',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка 
    empty_value_display = '-пусто-' 

admin.site.register(Group, GroupAdmin)