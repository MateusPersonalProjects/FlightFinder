import requests

# --------------------------------------- KIWI KEYS --------------------------------------------------- #
KIWI_API_KEY = "Adixhx9FQrK1LJHWaYiyrVdzz_rMyUKu"
KIWI_END_POINT = "https://api.tequila.kiwi.com/v2/search?"
KIWI_LOCATION_END_POINT = "https://api.tequila.kiwi.com/locations/query?"

headers_kiwi = {
    "apikey": KIWI_API_KEY,
}


class FlightSearch:
    # This class is responsible for search new flights and iata codes.

    def search_iata(self, params):
        location_endpoint = KIWI_LOCATION_END_POINT
        headers = headers_kiwi

        response_iata = requests.get(url=location_endpoint, params=params, headers=headers)
        response_iata.raise_for_status()
        data_iata = response_iata.json()
        return data_iata['locations'][0]['code']

    def search_prices(self, params):
        search_endpoint = KIWI_END_POINT
        headers = headers_kiwi
        response_search = requests.get(url=search_endpoint, params=params, headers=headers)
        response_search.raise_for_status()
        data_search = response_search.json()
        return data_search


