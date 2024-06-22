from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    text = models.TextField()
    city = models.CharField(max_length=120)
    published_date = models.DateField()  # Sadece tarih bilgisi içerir
    isActive = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)  # Tarih ve saat bilgisi içerir
    updated_date = models.DateTimeField(auto_now=True)  # Tarih ve saat bilgisi içerir
    
    def __str__(self):
        return self.title
