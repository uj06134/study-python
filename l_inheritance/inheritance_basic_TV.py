class TV:
    def __init__(self):
        self.power = False
        self.channel = 1
        self.volume = 1

    def display_info(self):
        print(f'전원: {self.power}')
        print(f'채널: {self.channel}')
        print(f'볼륨: {self.volume}')


tv = TV()
tv.display_info()


class SmartTV(TV):
    def __init__(self):
        # 직접 자식 생성자를 선언하면, 반드시 부모 생성자도 직접 호출한다.
        super().__init__()
        self.ip = "192.168.1.1"

    def display_info(self):
        super().display_info()
        print(f'IP: {self.ip}')


smart_tv = SmartTV()
smart_tv.display_info()