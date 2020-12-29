from datetime import datetime
import pytest
from django.test import Client
from rest_framework.test import APIClient

from movielist.models import Person, Movie
from movielist.tests.utils import fake_movie_data, faker, create_fake_movie
from showtimes.models import Cinema, Screening


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def cinema():
    cinema = Cinema.objects.create(name='kino', city='wawa')
    return cinema


@pytest.fixture
def screening(cinema, movie):
    date = datetime.now()
    screening = Screening.objects.create(movie=movie, cinema=cinema, date=date)
    return screening


@pytest.fixture
def director():
    director = Person.objects.create(name='directors_name')
    return director


@pytest.fixture
def actor():
    actor = Person.objects.create(name='actors_name')
    return actor


@pytest.fixture
def movie(director, actor):
    movie = Movie.objects.create(
        title='test_title',
        description='test_description',
        director=director,
        year=2000
    )
    movie.save()
    movie.actors.add(actor)
    movie.save()
    return movie


def create_fake_cinema():
    pass


@pytest.fixture
def set_up():
    for _ in range(5):
        Person.objects.create(name=faker.name())
    for _ in range(10):
        create_fake_movie()
    for _ in range(3):
        create_fake_cinema()
