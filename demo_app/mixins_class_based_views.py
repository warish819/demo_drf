from rest_framework import mixins,generics
from demo_app.models import Entry
from demo_app.serializers import DemoSerializer
from rest_framework.views import APIView


class CreateList(
                mixins.CreateModelMixin,
                mixins.DestroyModelMixin,
                mixins.UpdateModelMixin,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                generics.GenericAPIView):
    queryset = Entry.objects.all()
    serializer_class = DemoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    

    def put(self, request,pk):
        return self.update(request)    

    def get(self, request,pk):
        return self.retrieve(request)
    
    def delete(self, request,pk):
        return self.destroy(request)




