from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import User


class GroupPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class UserAndPermissionsSerializer(serializers.ModelSerializer):
    groups = GroupPermissionsSerializer(many=True, required=False)
    is_superuser = serializers.BooleanField(label='is_superuser', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'avatar', 'groups', 'is_superuser']
