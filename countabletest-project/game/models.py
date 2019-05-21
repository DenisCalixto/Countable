from django.db import models

class Game(models.Model):

    creation_date = models.DateTimeField()

    # not the best solution but I ran out of time and could not create lists
    # I tried to focus on the rest of the requirements

    phrase01 = models.TextField(null=True)

    image01 = models.ImageField(null=True, upload_to='images/')

    phrase02 = models.TextField(null=True)

    image02 = models.ImageField(null=True, upload_to='images/')

    phrase03 = models.TextField(null=True)

    image03 = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return str(self.creation_date)

    def formated_creation_date(self):
        return self.creation_date.strftime('%b %e %Y')
