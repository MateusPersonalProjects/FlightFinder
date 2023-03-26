import requests

SHEETY_ENDPOINT = "https://api.sheety.co/27f6d5cdcf9d22abe71a6c043fe4aac3/flightDeals/prices"
SHEETY_AUTH = ("mateuzote", "mateuzote1234")


class DataManager:
    # This class is responsible for get data from the sheet and update it.

    def getting_data(self):
        endpoint = SHEETY_ENDPOINT
        auth = SHEETY_AUTH

        response = requests.get(url=endpoint, auth=auth)
        return response.json()

    def updating_data(self, data, id):
        endpoint = SHEETY_ENDPOINT
        auth = SHEETY_AUTH

        response = requests.put(url=f"{endpoint}/{id}", json=data, auth=auth)
        response.raise_for_status()
