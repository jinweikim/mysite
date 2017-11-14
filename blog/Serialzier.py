from rest_framework import serializers
from .models import Author,Category,Train

class AuthorSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class CategorySeralizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class TrainSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ('train_id','start','dest','time')