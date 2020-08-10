from django.urls import path
from app3.api.views import ProfileList

urlpatterns = [
    path("profiles/", ProfileList.as_view(), name="profile-list")
]