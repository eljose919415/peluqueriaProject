from django.utils.text import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import (
    CustomUser, ImagesManage
)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "password",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "age",
            "phone_number",
        ]


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {"bad_token": _("Token invalido or expirado")}

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")


class ImageManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesManage
        fields = [
            "id",
            "name", "description", "image"
        ]
