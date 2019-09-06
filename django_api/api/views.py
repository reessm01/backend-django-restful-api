from rest_framework.viewsets import ModelViewSet
from django_api.api.serializers import *
from django_api.Shoe.models import *

class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    basename = 'manufacturer'
    queryset = Manufacturer.objects.all()

class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    basename = 'shoetype'
    queryset = ShoeType.objects.all()

class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    basename = 'shoecolor'

    queryset = ShoeColor.objects.all()


class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    basename = 'shoe'
    
    def get_queryset(self):
        queryset = Shoe.objects.all()
        id_value = self.request.query_params.get('id', None)

        if id_value:
            queryset = queryset.filter(id=id_value)
        
        return queryset