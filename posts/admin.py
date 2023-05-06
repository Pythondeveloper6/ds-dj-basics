from django.contrib import admin

# Register your models here.
from .models import Post , Author
from django_summernote.admin import SummernoteModelAdmin



class PostAdmin(admin.ModelAdmin):
    # summernote_fields = '__all__'
    list_display = ['title' , 'author']
    list_filter = ['author','tags']
    search_fields = ['title','content']
    # summernote_fields = ('content',)




admin.site.register(Post,PostAdmin)

admin.site.register(Author)