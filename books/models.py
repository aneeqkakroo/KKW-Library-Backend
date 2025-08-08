from django.db import models

# Ebook model
class Ebook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    topic = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='ebooks/')
    cover_image = models.ImageField(upload_to='covers/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
