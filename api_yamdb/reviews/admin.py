from django.contrib import admin
from django.db.models import Avg

from reviews.models import Category, Comment, Genre, Review, Title


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', 'slug')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', 'slug')


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'year', 'get_rating', 'get_genres', 'category'
    )
    search_fields = ('name',)
    list_filter = ('year', 'category')
    list_editable = ('category',)
    filter_horizontal = ('genre',)
    empty_value_display = '-пусто-'

    def get_genres(self, obj):
        return "/".join([genre.name for genre in obj.genre.all()])

    def get_rating(self, obj):
        avg_rating = obj.reviews.all().aggregate(Avg('score'))['score__avg']
        return int(avg_rating) if avg_rating else None


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'score', 'pub_date')
    search_fields = ('title', 'author')
    list_filter = ('score',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'review', 'pub_date')
