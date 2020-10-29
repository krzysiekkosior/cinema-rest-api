from datetime import datetime
import pytest
from django.test import Client
from rest_framework.test import APIClient

from movielist.tests.utils import fake_movie_data
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
def screening():
    test_movie = fake_movie_data()
    test_cinema = cinema()
    date = datetime.now()
    screening = Screening.objects.create(movie=test_movie, cinema=test_cinema, date=date)
    return screening
