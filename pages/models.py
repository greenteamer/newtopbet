#coding: utf-8
from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    image = models.ImageField(upload_to='Page_thumb')
    # проверка на главной ли сранице этот Page
    main_page_choice = models.CharField(
        max_length=10,
        choices=(
            ('notmain' , 'нет'),
            ('main' , 'да'),
        ),
        default='',
    )
    def page_in_main(self):
        return self.main_page_choice == 'main'
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/page/%i/" % self.id
