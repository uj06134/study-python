class Reservation:
    def __init__(self, id, time, created_date, client_email, conference_room_id, partime):
        self.id = id
        self.time = time
        self.created_date = created_date
        self.client_email = client_email
        self.conference_room = conference_room_id
        self.partime = partime
