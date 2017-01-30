from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Select Gender')
    age = models.IntegerField()

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

# def generate_filename(self, filename):
#     url = "files/serie/%s/%s" % (self.serie.name, filename)
#     return url

class serie(models.Model):
    name = models.CharField(max_length=100)
    actors = models.ManyToManyField(actor)
    pic = models.ImageField(upload_to='series/%Y-%m-%d')
    release = models.DateField()
    review = models.TextField()
    seasons = models.IntegerField()

    def __unicode__(self):
        return '%s' % (self.name)
