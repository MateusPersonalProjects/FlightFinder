# ALIENS PRA KCT

import data_manager
import flight_search
import flight_data
import notification_manager
import datetime as dt
from dateutil.relativedelta import relativedelta

# -------------------------------------- TWILIO ------------------------------------------------- #
TWILIO_NUM = '+16067157741'
TWILIO_TO_SEND = '+5514996615410'


# -------------------------- Function that return the city IATA code --------------------------------------------- #
def asking_city(city):
    pop_params = {
        "term": city,
        "location_types": "city"
    }
    return searcher.search_iata(pop_params)


# ----------------------------- POPULATE IATA CODES ---------------------------------------- #
def iata_populate(data):
    """ This function populates the IATA column if it's empty """
    for row in data['prices']:
        if row['iataCode'] == "":
            print("Empty Column, populating")
            to_pop = {
                "price": {
                    'iataCode': asking_city(row['city'])
                }
            }
            data_maid.updating_data(to_pop, row['id'])
        else:
            print("Everything Alright")


# Setting up the classes.
searcher = flight_search.FlightSearch()
data_maid = data_manager.DataManager()


# Get Sheet data.
sheet_data = data_maid.getting_data()


# Get today date.
date_today = dt.datetime.today()
# Adding 6 months to the current date
date_after_month = dt.datetime.now() + relativedelta(months=6)


# Check if the IATA codes are empty, if it's add IATA codes to it.
iata_populate(sheet_data)


# Ask the user his current city and getting the IATA code for his city.
user_city = input("Which city you want to get your flight? ")
iata_user_city = asking_city(user_city)

# First for loop, it gets the information in the row of the sheet, and adds it into the params to search.
for row in sheet_data['prices']:

    # Variables to control if we found a new flight.
    store_status = False
    stops_status = False

    # Storing the flight with better price and its current price.
    current_flight = {}
    current_price = row['lowestPrice']

    # Params to get the data from the API.
    params_search = {
        "fly_from": iata_user_city,
        "fly_to": row['iataCode'],
        "date_from": date_today.strftime('%d/%m/%Y'),
        "date_to": date_after_month.strftime('%d/%m/%Y'),
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "one_for_city": 1,
        "max_stopovers": 0
    }

    # Get all the flights for the current date.
    all_flights = searcher.search_prices(params_search)

    # Check all flights for the better price and storing it.
    for flight in all_flights['data']:
        if flight['price'] < current_price:
            current_price = flight['price']
            current_flight = flight
            store_status = True

    # Check if we found a better price.
    if store_status:

        att_price = {
            'price': {
                'lowestPrice': current_price
            }
        }

        # Update our sheet
        data_maid.updating_data(att_price, row['id'])

        # Set up our SMS message and send it
        depurer = flight_data.FlightData(current_flight, stops_status)
        sms_string = depurer.depure_data()
        sms_sender = notification_manager.NotificationManager()
        sms_sender.send_sms(sms_string, TWILIO_NUM, TWILIO_TO_SEND)

    # Check if we can find a better price with 2 stops.
    else:
        print(f"\nWe do not found a new flight price for {row['city']}\nTrying with 2 stop overs.")

        params_search['max_stopovers'] = 2
        all_flights = searcher.search_prices(params_search)

        for flight in all_flights['data']:
            if flight['price'] < current_price:
                current_price = flight['price']
                current_flight = flight
                store_status = True
                stops_status = True

        if store_status:
            att_price = {
                'price': {
                    'lowestPrice': current_price
                }
            }

            # Get all the flights for the current date.
            data_maid.updating_data(att_price, row['id'])

            # Set up our SMS message and sending it
            depurer = flight_data.FlightData(current_flight, stops_status)
            sms_string = depurer.depure_data()
            sms_sender = notification_manager.NotificationManager()
            sms_sender.send_sms(sms_string, TWILIO_NUM, TWILIO_TO_SEND)

        else:
            print(f"Unfortunately we do not found a new flight price for {row['city']}")






