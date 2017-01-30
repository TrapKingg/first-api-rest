from rest_framework import serializers
from Series.models import serie, actor

# class actorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     first_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     last_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     gender = serializers.ChoiceField(choices=GENDER_CHOICES, default='Select Gender')
#     age = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return actor.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.gender = validated_data.get('gender', instance.gender)
#         instance.ager = validated_data.get('ager', instance.ager)
#         instance.save()
#         return instance
class actorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = actor
        fields = ('url', 'first_name', 'last_name', 'gender', 'age')

class serieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = serie
        fields = ('url', 'name', 'actors', 'pic', 'release', 'review', 'seasons')
