from twilio.rest import Client
# -------------------------------------- TWILIO KEYS ------------------------------------------------- #
TWILIO_SID = 'ACa6f6baa41a98225d6a0c40d2a64c4803'
TWILIO_AUTH = 'd9354d16564de42da28667d2700f466c'


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

