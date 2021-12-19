from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    img=models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.title