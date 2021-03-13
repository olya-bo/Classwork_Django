from django.contrib import admin
from .models import MyUser, Article, Customer, CustomerSettings, Book, Author, Publication


# class ArticleAdmin(admin.ModelAdmin):
#     fields = ('name', 'text')

    # def create_date(self, obj):
    #     return obj.created

    # view_birth_date.empty_value_display = '???'


admin.site.register(MyUser)
admin.site.register(CustomerSettings)
admin.site.register(Customer)
# admin.site.register(Article, ArticleAdmin)
admin.site.register(Book)
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Publication)
