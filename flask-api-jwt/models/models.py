import mongoengine as me

me.connect(host='mongodb+srv://julio:borden16@testing.zvaswda.mongodb.net/apli2?retryWrites=true&w=majority')

class User(me.Document):
    firstName = me.StringField(required=True)
    lastName = me.StringField(required=True)
    username = me.StringField(required=True)
    email = me.EmailField(required=True)
    password = me.StringField(required=True)
    crated_at = me.DateTimeField(required=True)
    updated_at = me.DateTimeField(required=True)
    is_active = me.BooleanField(required=True)
    is_admin = me.BooleanField(required=True)
    # relationships one to many (one user has many devices)
    devices = me.ListField(me.ReferenceField('Device'))

    # retrieve by username
    @classmethod
    def get_by_username(cls, username: str) -> "User":
        return cls.objects(username=username).first()

    # retrieve by email
    @classmethod
    def get_by_email(cls, email: str) -> "User":
        return cls.objects(email=email).first()
    
    # retrieve by id
    @classmethod
    def get_by_id(cls, id) -> "User":
        return cls.objects(id=id).first()

class Device(me.Document):
    deviceName = me.StringField(required=True)
    deviceType = me.StringField(required=True)
    deviceModel = me.StringField(required=True)
    created_at = me.DateTimeField(required=True)
    updated_at = me.DateTimeField(required=True)
    is_active = me.BooleanField(required=True)
    # relationships one to many (one device has many gpio)
    gpios = me.ListField(me.ReferenceField('Gpio'))
    # relationships one to many (one device has many sensors)
    # sensors = me.ListField(me.ReferenceField('Sensor'))

    # retrieve by deviceName
    @classmethod
    def get_by_deviceName(cls, deviceName: str) -> "Device":
        return cls.objects(deviceName=deviceName).first()

    # retrieve by id
    @classmethod
    def get_by_id(cls, id) -> "Device":
        return cls.objects(id=id).first()

class Gpio(me.Document):
    gpioName = me.StringField(required=True)
    gpioDescription = me.StringField(required=True)
    gpioPin = me.IntField(required=True)
    created_at = me.DateTimeField(required=True)
    updated_at = me.DateTimeField(required=True)
    # relationship one to one (one gpio has one status)
    gpioStatus = me.ListField(me.ReferenceField('GpioStatus'))

    # retrieve by gpioName
    @classmethod
    def get_by_gpioName(cls, gpioName: str) -> "Gpio":
        return cls.objects(gpioName=gpioName).first()
    
    # retrieve by gpioPin
    @classmethod
    def get_by_gpioPin(cls, gpioPin: int) -> "Gpio":
        return cls.objects(gpioPin=gpioPin).first()

    # retrieve the last gpioStatus
    @property
    def last_gpioStatus(self) -> "GpioStatus":
        if len(self.gpioStatus) > 0:
            return self.gpioStatus[-1].gpioStatus
        else:
            return None

class GpioStatus(me.Document):

    gpioStatus = me.BooleanField(required=True)
    created_at = me.DateTimeField(required=True)
    



