from django.db import models



class Activitie(models.Model):
    title = models.CharField(max_length = 60, blank = False)
    body = models.CharField(max_length = 1000, blank = False)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

