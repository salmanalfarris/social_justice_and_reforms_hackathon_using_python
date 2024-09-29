from django.db import models

# Create your models here.

class LegalCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LegalArticle(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(LegalCategory, on_delete=models.SET_NULL, null=True, related_name='articles')
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    category = models.ForeignKey(LegalCategory, on_delete=models.SET_NULL, null=True, related_name='faqs')

    def __str__(self):
        return self.question