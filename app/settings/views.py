from django.shortcuts import render
from rest_framework import mixins 
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from app.settings.models import Settings
from app.settings.serializers import SettingsSerailizers

class SettingsAPI(mixins.ListModelMixin, GenericViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerailizers
    permission_classes = [AllowAny, ]