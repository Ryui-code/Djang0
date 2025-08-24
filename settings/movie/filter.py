import django_filters
from .models import Movie

class MovieFilter(django_filters.FilterSet):
    published_after = django_filters.DateFilter(field_name='published_date', Lookup_expr='gte')
    published_before = django_filters.DateFilter(field_name='published_date', Lookup_expr='lte')



    class Meta:
        model = Movie
        fields = ['country', 'director']