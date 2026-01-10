from rest_framework.routers import DefaultRouter
from django.urls import path

from app.settings.views import SettingsAPI

router = DefaultRouter()
router.register("settings", SettingsAPI)

urlpatterns = [
    
]

urlpatterns += router.urls