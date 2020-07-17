from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)                           #blank = True means optional

    def __str__(self):
       return self.title