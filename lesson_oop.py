data = {
"markers": [{"name": "Rixos The Palm Dubai",
"position": [25.1212, 55.1535],},
{"name": "Shangri-La Hotel",
"location": [25.2084, 55.2719]},
{"name": "Grand Hyatt",
"location": [25.2285, 55.3273]}]}

class Hotels:
    def key_names(self, a):
        names = []
        names = [i['name'] for i in a['markers']]
        print(names)


    def loc_hotel(self, b):
        loc = []
        loc = b.values()
        print(loc)


h = Hotels()
h.key_names(data)

l = Hotels()
l.loc_hotel(data)