from django.contrib.auth import get_user_model

from reviews.models import Category, Comment, Genre, Review, Title

User = get_user_model()

csv_data_relation = (
    {'model': Category, 'filename': 'category.csv'},
    {'model': Genre, 'filename': 'genre.csv'},
    {'model': Title, 'filename': 'titles.csv'},
    {'model': Title.genre.through, 'filename': 'genre_title.csv'},
    {'model': User, 'filename': 'users.csv'},
    {'model': Review, 'filename': 'review.csv'},
    {'model': Comment, 'filename': 'comments.csv'}
)
