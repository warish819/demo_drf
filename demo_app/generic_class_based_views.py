from .models import Entry
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveAPIView
from .serializers import *
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication

class CreateListGenerics(ListCreateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["admin"]
    queryset = Entry.objects.all()
    serializer_class = DemoSerializer

class RetrieveView(RetrieveAPIView):
    queryset = Entry.objects.all()
    serializer_class = DemoSerializer

class DestroyView(DestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = DemoSerializer


 


