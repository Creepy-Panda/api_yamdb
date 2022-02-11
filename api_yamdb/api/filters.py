import django_filters

from reviews.models import Title


class TitleFilter(django_filters.FilterSet):
    """Custom filter for Title model."""
    category = django_filters.CharFilter(field_name='category__slug')
    genre = django_filters.CharFilter(field_name='genre__slug')
    name = django_filters.CharFilter(
        field_name='name', method='filter_by_partial_match'
    )

    def filter_by_partial_match(self, queryset, name, value):
        """Method for filtering queryset by partial match of value."""
        return queryset.filter(name__icontains=value)

    class Meta:
        model = Title
        fields = ['category', 'genre', 'name', 'year']
