class User:
    def __init__(self, name):
        self.name = name

class Notification:
    def send(self, user):
        pass

class EmailNotification(Notification):
    def send(self, user):
        print(f"Sending email to {user.name}")

class SMSNotification(Notification):
    def send(self, user):
        print(f"Sending SMS to {user.name}")

class NotificationService:
    def __init__(self, notification):
        self.notification = notification

    def notify(self, user):
        self.notification.send(user)

user = User("Basma")
email_notification = EmailNotification()
sms_notification = SMSNotification()

# Using the notification classes
# email_notification.send(user)  
# sms_notification.send(user)    


service = NotificationService(email_notification)
service.notify(user)

service = NotificationService(sms_notification)
service.notify(user)
