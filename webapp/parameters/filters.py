import django_filters
from django_filters import CharFilter
from .models import Parameter

class DataFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = Parameter
        fields = '__all__'
        exclude = ['id','values','allowed_values','modifiable','source','apply_type','data_type','description']