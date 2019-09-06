from rest_framework.serializers import HyperlinkedModelSerializer
from django_api.Shoe.models import *

class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = (
            'name',
            'website'
        )
class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = (
            'style',
        )
class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = (
            'color_name',
        )

class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = (
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'
        )