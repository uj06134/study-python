class Office:
    def __init__(self, id: int, name: str, location: str, conference_rooms: tuple):
        self.id = id
        self.name = name
        self.location = location
        self.conference_rooms = conference_rooms

    def __str__(self):
        room_str = ""
        for i, conference_room in enumerate(self.conference_rooms):
            room_str += f"{i + 1}. {conference_room.id}번 회의실\n"
        return room_str
