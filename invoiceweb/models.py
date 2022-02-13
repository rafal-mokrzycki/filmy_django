from django.db import models

class Film(models.Model):
    # documentation: https://docs.djangoproject.com/en/4.0/ref/models/fields/
    tytul = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(default=2000)

    def __str__(self):
        return self.tytul + " (" + str(self.rok) + ")"
