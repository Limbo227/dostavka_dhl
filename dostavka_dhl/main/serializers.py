from rest_framework import serializers
from .models import *


class MainSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dostavka
        fields = ['amount', 'length', 'width', 'height', 'weight', 'scale', 'scale_weight',]

    def create(self, validated_data):
        print(validated_data)
        t = (validated_data['amount'], validated_data['length'], validated_data['width'], validated_data['height'], validated_data['weight'])
        t2 = sum(t)
        total_price = t2/5
        return Dostavka.objects.create(**validated_data, total_price=total_price)



class MainListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dostavka
        fields = '__all__'




class ScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scale
        fields = '__all__'


class ScaleWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scale_weight
        fields = '__all__'

