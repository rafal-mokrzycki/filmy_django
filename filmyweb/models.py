from django.db import models

class Film(models.Model):
    # documentation: https://docs.djangoproject.com/en/4.0/ref/models/fields/
    tytul = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(default="")
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2,
                                      null=True, blank=True)
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)

    def __str__(self):
        return self.tytul_z_rokiem()

    def tytul_z_rokiem(self):
        return "{} ({})".format(self.tytul, self.rok)
