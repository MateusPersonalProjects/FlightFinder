import requests

SHEETY_ENDPOINT = "YOUR SHEETY"
SHEETY_AUTH = "YOUR SHEETY AUTH"


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
