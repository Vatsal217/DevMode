from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app3.models import Profile
from app3.api.serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]