from firebase_admin import messaging


def send_to_firebase_cloud_messaging():
    # This registration token comes from the client FCM SDKs.
    registration_token = 'f44ME0dmQfuss8yglA8yWr:APA91bH6KIekZiggF3CMCESlHRLzauZ6s8kUOo7mWOdoiJippwVaIx86C9co7vTJjxEBcFbQIPnq8H_Pc8N35Pw9o9ZedznrN7Kz8byktJuVd043Bb2JiBGU4D0fvnLfsTFH2fLbVFdC'

    # See documentation on defining a message payload.
    message = messaging.Message(
        notification=messaging.Notification(
            title='위험한 사람 발견',
            body='위험한 사람을 발견했습니다',
        ),
        token=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
