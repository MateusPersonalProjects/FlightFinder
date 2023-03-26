from twilio.rest import Client
# -------------------------------------- TWILIO KEYS ------------------------------------------------- #
TWILIO_SID = 'YOUR TWILIO SID'
TWILIO_AUTH = 'YOUR TWILIO AUTH'


class NotificationManager:
    # This class is responsible for send the SMS

    def send_sms(self, message, tw_num, to_send):
        sid = TWILIO_SID
        auth = TWILIO_AUTH

        client = Client(sid, auth)
        send = client.messages \
            .create(
            body = message,
            from_ = tw_num,
            to = to_send
        )
        print(send.status)

