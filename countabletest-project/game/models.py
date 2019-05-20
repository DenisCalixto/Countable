from django.db import models

class Game(models.Model):

    creation_date = models.DateTimeField()
    phrase01 = models.TextField(null=True)
    image01 = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.title

    def formated_creation_date(self):
        return self.creation_date.strftime('%b %e %Y')
