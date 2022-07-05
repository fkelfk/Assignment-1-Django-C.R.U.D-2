from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'Actors'

    def __str__(self):
        return self.first_name


class Movies(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField(null=True)
    actors = models.ManyToManyField('Actor')

    class Meta:
        db_table = 'Movies'
    def __str__(self):
        return self.title
