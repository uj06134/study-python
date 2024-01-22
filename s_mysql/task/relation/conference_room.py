import datetime
from part_time import PartTime


class ConferenceRoom:
    def __init__(self, id: int, part_times: tuple):
        self.id = id
        self.part_times = part_times
        self.reservations = None

    def __check_reservation(self, part_time: PartTime):
        check = False
        for reservation in self.reservations:
            if str(reservation.get("time")) == part_time.__str__():
                part_time.status = False
                check = True
                break
        return "예약 불가" if check else "예약 가능"

    def __str__(self):
        time_str = ""
        for i, part_time in enumerate(self.part_times):
            time_str += f"{i + 1}. {part_time.__str__()} ({self.__check_reservation(part_time)})\n"
        return time_str












