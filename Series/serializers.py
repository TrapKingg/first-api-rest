from rest_framework import serializers
from Series.models import serie, actor, GENDER_CHOICES
from versatileimagefield.serializers import VersatileImageFieldSerializer

class actorSerializer(serializers.HyperlinkedModelSerializer):
    pic = VersatileImageFieldSerializer(
    sizes='image_cut'
)
    class Meta:
        model = actor
        fields = ('url', 'first_name', 'last_name', 'pic', 'gender', 'age')

class serieSerializer(serializers.HyperlinkedModelSerializer):
    pic = VersatileImageFieldSerializer(
    sizes='image_cut'
)
    actors = actorSerializer(many=True)

    class Meta:
        model = serie
        fields = ('url', 'name', 'actors', 'pic', 'release', 'review', 'seasons')
