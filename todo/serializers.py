from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=2000)
    description = serializers.CharField(max_length=2000)
    status = serializers.CharField(max_length = 20)


    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.status = validated_data.get('status',instance.status)
        instance.save()
        return instance