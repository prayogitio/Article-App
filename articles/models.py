from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True, upload_to='media')
    author = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

#after make a model, we should do these followings:
#python manage.py makemigrations
#python manage.py migrate

#python manage.py shell
#from articles.models import Article
#variable_name = Article()
#variable_name.title = blabalaba
#variable_name.save()
#to show content of the table, Article.objects.all()