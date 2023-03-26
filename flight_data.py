import datetime as dt


class FlightData:
    # This class is responsible for structure the flight data.

    def __init__(self, data, stops):
        self.data = data
        self.today = dt.datetime.today().strftime('%Y-%m-%d')
        self.stops = stops

    def depure_data(self):
        flight_from = f"{self.data['cityFrom']}-{self.data['cityCodeFrom']}"
        flight_to = f"{self.data['cityTo']}-{self.data['cityCodeTo']}"
        flight_price = self.data['price']
        flight_date = self.data['route'][0]['local_departure'][:9]

        if self.stops:
            qt_flights = len(self.data['route'])
            stops_loc = []
            for st in self.data['route']:
                stops_loc.append(f"{st['cityFrom']}-{st['flyFrom']}")
                if len(stops_loc) < len(self.data['route'])+2:
                    stops_loc.append(" ➜ ")

            stop_locs_string = ''.join(stops_loc)

            string_send = f"Low price alert! With {qt_flights - 1} stops only ${flight_price} to fly from {flight_from}" \
                          f" to {flight_to}, from {self.today} to {flight_date}.\nThis is going to be your route:\n" \
                          f"{stop_locs_string}."

        else:
            string_send = f"Low price alert! Only ${flight_price} to fly from {flight_from} to {flight_to}, from " \
                 f"{self.today} to {flight_date}."

        return string_send

