from locust import HttpUser, task, between


class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    @task(1)
    def index(self):
        self.client.get("http://127.0.0.1:5000/")

    @task(2)
    def showSummary(self):
        data = {
            'club': {
                "name": "Simply Lift",
                "email": "john@simplylift.co",
                "points": "13"
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
        self.client.post("http://127.0.0.1:5000/showSummary", data)


    @task(3)
    def book(self):
        self.client.get("http://127.0.0.1:5000/book/Fall%20Classic/Simply%20Lift")

    @task(4)
    def purchasePlaces(self):
        data = {
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
        self.client.post("http://127.0.0.1:5000/purchasePlaces", data)

    @task(5)
    def logout(self):
        self.client.get("http://127.0.0.1:5000/logout")