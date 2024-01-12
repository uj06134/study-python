class NameCard:
    def print_info(self, name):
        print(name)

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, type, value, traceback):
        print('exit')

    def __del__(self):
        print('del')

with NameCard() as name_card:
    name_card.print_info('실행할 문장')