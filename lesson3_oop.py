colors = {
        "black": {"category": "hue", "type": "primary", "code": {"rgba": [255, 255, 255, 1], "hex": "#000"}},
        "white": {"category": "value", "type": "primary", "code": {"rgba": [0, 0, 0, 1], "hex": "#FFF"}},
        "red": {"category": "hue","type": "primary", "code": {"rgba": [255, 0, 0, 1], "hex": "#FF0"}},
        "blue": {"category": "hue", "type": "primary", "code": {"rgba": [0, 0, 255, 1],"hex": "#00F"}},
        "yellow": {"category": "hue", "type": "primary", "code": {"rgba": [255, 255, 0, 1],"hex": "#FF0"}},
        "green": {"category": "hue","type": "secondary","code": {"rgba": [0, 255, 0, 1],"hex": "#0F0"}}}

class Parser:
    def key_tuple(self, c):
        l = []
        l = (colors.keys())
        print(tuple(l))
        print('tuple keys')

    def value_tuple(self, a):
        l = []
        for i in a.values():
            l = (i.values())
            print(tuple(l))
            print("tuple values")

    def key_list(self, h):
        l = []
        l.append(h.keys())
        l.append(h['black'].keys())
        print([l])
        print('list keys')

    def value_list(self, w):
        l = []
        for i in w.values():
            l = (i.values())
            print(l)
            print('list values')

    def key_set(self, e):
        l = {}
        for i in e.values():
            l = (i.keys())
            print(set(l))
            print('set keys')

    def value_set(self, wer):
        l = {}
        for i in wer.values():
            l = (wer.values())
            print(l)
            print('set values')

p = Parser()
p.key_tuple(colors)

s = Parser()
s.value_tuple(colors)

d = Parser()
d.key_list((colors))

q = Parser()
q.value_list(colors)

sq = Parser()
sq.key_set(colors)

wqw = Parser()
wqw.value_set(colors)