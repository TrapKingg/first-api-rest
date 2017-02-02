from rest_framework import serializers
from Series.models import serie, actor, GENDER_CHOICES
from versatileimagefield.serializers import VersatileImageFieldSerializer
from django.contrib.auth.models import User

class actorSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    pic = VersatileImageFieldSerializer(
    sizes='image_cut'
)
    class Meta:
        model = actor
        fields = ('url', 'first_name', 'last_name', 'get_full_name', 'pic', 'gender', 'age', 'owner')

class serieSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    pic = VersatileImageFieldSerializer(
    sizes='image_cut'
)
    actors = actorSerializer(many=True)

    class Meta:
        model = serie
        fields = ('url', 'name', 'actors', 'pic', 'release', 'review', 'seasons', 'owner')

#############################->ESTO SE BORRA SI NO FUNCIONA
class UserSerializer(serializers.HyperlinkedModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(many=True, queryset=actor.objects.all())
    series = serializers.PrimaryKeyRelatedField(many=True, queryset=serie.objects.all())

    class Meta:
        model = User
        fields = ('url', 'username', 'actors', 'series')
