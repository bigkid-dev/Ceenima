from rest_framework import serializers
from .models import Shows


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = ('id','title','description','summary','link','image_link','time_showing','second_time_showing','third_time_showing','fourth_time_showing')


