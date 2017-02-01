from django.db import models
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField, PPOIField
# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pic = VersatileImageField('actors', upload_to='actors/%Y-%m-%d', ppoi_field='actors_ppoi')
    actors_ppoi = PPOIField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Select Gender')
    age = models.IntegerField()
    #owner = models.ForeignKey(User, editable=False)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

# def generate_filename(self, filename):
#     url = "files/serie/%s/%s" % (self.serie.name, filename)
#     return url

class serie(models.Model):
    name = models.CharField(max_length=100)
    actors = models.ManyToManyField(actor)
    pic = VersatileImageField('Image', upload_to='series/%Y-%m-%d', ppoi_field='series_ppoi')
    series_ppoi = PPOIField()
    release = models.DateField()
    review = models.TextField()
    seasons = models.IntegerField()
    #owner = models.ForeignKey(User, editable=False)

    def __unicode__(self):
        return '%s' % (self.name)
