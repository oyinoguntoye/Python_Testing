from server import app
import json
from datetime import datetime


def test_loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         assert len(listOfClubs)>0

def test_loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         listOfCompetitions = [c for c in listOfCompetitions if c['date'] >= datetime.today().strftime('%Y-%m-%d-%H:%M:%S')]
         assert len(listOfCompetitions) > 0

def test_index():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_showSummary():
    client = app.test_client()
    url = '/showSummary'

    mock_request_data = {
        'club': {
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points":"13"
        },
        'competitions': [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ],
        'clubs': [
    {
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points":"13"
    },
    {
        "name":"Iron Temple",
        "email": "admin@irontemple.com",
        "points":"4"
    },
    {   "name":"She Lifts",
        "email": "kate@shelifts.co.uk",
        "points":"12"
    }
]
    }

    response = client.post(url, data=mock_request_data)
    assert response.status_code == 200

def test_book():
    client = app.test_client()
    url = '/book/Fall%20Classic/Simply%20Lift'

    mock_request_data = {
        'club': "Simply Lift",
        'competition': "Fall Classic",
        'foundCompetition': {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        },
        'foundClub': {
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points":"13"
        },
        'competitions': [
            {
                "name": "Spring Festival",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25"
            },
            {
                "name": "Fall Classic",
                "date": "2020-10-22 13:30:00",
                "numberOfPlaces": "13"
            }
        ],
        'clubs': [
            {
                "name": "Simply Lift",
                "email": "john@simplylift.co",
                "points": "13"
            },
            {
                "name": "Iron Temple",
                "email": "admin@irontemple.com",
                "points": "4"
            },
            {"name": "She Lifts",
             "email": "kate@shelifts.co.uk",
             "points": "12"
             }
        ]
    }

    response = client.get(url, data=mock_request_data)
    assert response.status_code == 200

def test_purchasePlaces():
    client = app.test_client()
    url = '/purchasePlaces'

    mock_request_data = {
        'places': 10,
        'club': "Simply Lift",
        'competition': "Fall Classic",
        'competitions': [
            {
                "name": "Spring Festival",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25"
            },
            {
                "name": "Fall Classic",
                "date": "2020-10-22 13:30:00",
                "numberOfPlaces": "13"
            }
        ],
        'clubs': [
            {
                "name": "Simply Lift",
                "email": "john@simplylift.co",
                "points": "13"
            },
            {
                "name": "Iron Temple",
                "email": "admin@irontemple.com",
                "points": "4"
            },
            {"name": "She Lifts",
             "email": "kate@shelifts.co.uk",
             "points": "12"
             }
        ]
    }

    response = client.post(url, data=mock_request_data)
    assert response.status_code == 200

def test_logout():
    response = app.test_client().get('/')
    assert response.status_code == 200