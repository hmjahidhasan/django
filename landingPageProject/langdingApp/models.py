from django.db import models

# Create your models here.
class about(models.Model):
    title = models.CharField(max_length=70, blank=False)
    description = models.TextField(max_length=500, blank=False)
    image = models.ImageField(upload_to='aboutt/', blank= False)

    def __str__(self):
        return self.title


