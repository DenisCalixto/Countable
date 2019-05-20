from django.db import models

class Game(models.Model):

    creation_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def formated_creation_date(self):
        return self.creation_date.strftime('%b %e %Y')
