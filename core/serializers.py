from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.mail import send_mail
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        send_mail(
            'Subject here',
            'Here is the message123.',
            user.email,
            ['david.89.mora@gmail.com'],
            fail_silently=False,
        )
        return user
