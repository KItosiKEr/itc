class House:
    a = 1
    def open_door(self):
        return 'doors is open'

class Apartments(House):
    pass

a = Apartments()
print(a.open_door())