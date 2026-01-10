from rest_framework import serializers

from app.settings.models import Settings


class SettingsSerailizers(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['id', 'title', 'descritpion', 'image']