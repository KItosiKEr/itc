# class House:
#     a = 1
#     def open_door(self):
#             return 'doors is open'

# class Apartments(House):
#     pass

# a = Apartments()
# print(a.open_door())

'''
class Factory:
    def engine(self):
        return ('двигатель создан')
    def bridge(self):
        return ('ходовая часть создана')

class Toyota(Factory):
    def wheels(self):
        return ('колёса готовы')    
    def windows(self):
        return ('стёкла готовы') 

list = []
a = Toyota()
a.windows()
a.bridge()
a.engine()
a.wheels()
list.append(a.engine())
list.append(a.bridge())
list.append(a.wheels())
list.append(a.windows())
print(list)
'''

class Zoo:
    def __init__(self):
        self.animal_1 = 'тигр'
        self.animal_2 = 'бегемот'
        self.animal_3 = 'жираф'

a = Zoo()
a.animal_1 = 'лев'
a.animal_4 = [a.animal_2 + ' , ' + a.animal_3]
a.animal_3 = 'змея'
print(a.animal_1)
print(a.animal_3)
print(a.animal_4)


