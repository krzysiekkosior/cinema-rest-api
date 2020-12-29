from datetime import datetime

import pytest

from movielist.models import Movie
from movielist.tests.utils import fake_movie_data
from showtimes.models import Cinema, Screening


@pytest.mark.django_db
def test_get_cinema_list(client, cinema):
    response = client.get('/cinemas/', {}, format='json')
    data = response.data[0]
    assert response.status_code == 200
    assert Cinema.objects.count() == len(response.data)
    assert data.get('name') == 'kino'


@pytest.mark.django_db
def test_add_cinema(client):
    existing_cinemas = Cinema.objects.count()
    cinema = {'name': 'kino',
              'city': 'wawa'}
    response = client.post('/cinemas/', cinema, format='json')
    assert response.status_code == 201
    assert Cinema.objects.count() == existing_cinemas + 1
    for key, value in cinema.items():
        assert key in response.data


@pytest.mark.django_db
def test_get_cinema_detail(client, cinema):
    test_cinema = Cinema.objects.first()
    response = client.get(f"/cinemas/{test_cinema.id}/", {}, format='json')

    assert response.status_code == 200
    for key in ('name', 'city'):
        assert key in response.data


@pytest.mark.django_db
def test_delete_cinema(client, cinema):
    test_cinema = Cinema.objects.first()
    response = client.delete(f"/cinemas/{test_cinema.id}/", {}, format='json')

    assert response.status_code == 204
    cinemas_ids = [cinema.id for cinema in Cinema.objects.all()]
    assert test_cinema.id not in cinemas_ids


@pytest.mark.django_db
def test_update_cinema(client, cinema):
    test_cinema = Cinema.objects.first()
    response = client.get(f"/cinemas/{test_cinema.id}/", {}, format='json')
    cinema_data = response.data
    cinema_data['name'] = 'testowa nazwa kina'
    cinema_data['city'] = 'testowa nazwa miasta'
    response = client.patch(f"/cinemas/{test_cinema.id}/", cinema_data, format='json')

    assert response.status_code == 200


@pytest.mark.django_db
def test_get_screening_list(client, set_up):
    response = client.get('/screenings/', {}, format='json')
    assert response.status_code == 200
    assert Screening.objects.count() == len(response.data)


@pytest.mark.django_db
def test_add_screening(client, cinema, movie):
    existing_screenings = Screening.objects.count()
    screening = {
        'movie': movie.title,
        'cinema': cinema.name,
        'date': datetime.today().date()
    }
    response = client.post('/screenings/', screening, format='json')
    assert response.status_code == 201
    assert Screening.objects.count() == existing_screenings + 1
    for key, value in screening.items():
        assert key in response.data
