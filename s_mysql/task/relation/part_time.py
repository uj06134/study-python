import datetime


class PartTime:
    def __init__(self, id: int, time: datetime.timedelta):
        self.id = id
        self.time = time
        self.status = True

    def __str__(self):
        return str(self.time)
