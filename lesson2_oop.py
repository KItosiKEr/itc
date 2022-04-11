lap = {}
class Laptops:
    def __init__(self, model, cpu, ram, vga, memory, motherboard, display):
        self.model = model
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.memory = memory
        self.motherboard = motherboard
        self.display = display
    def save(self):
        lap[self.model] = self.cpu, self.ram, self.vga, self.memory, self.motherboard, self.display

for i in range(5):
    model = input('Enter your model: ')
    cpu = input('Enter your cpu: ')
    ram = input('Enter your ram: ')
    vga = input('Enter your vga: ')
    memory = input('Enter your memory: ')
    motherboard = input('Enter your motherboard: ')
    display = input('Enter your display: ')
    laptops = Laptops(model = model, cpu = cpu, ram = ram, vga = vga, memory = memory, motherboard = motherboard, display = display)
    laptops.save()
print(lap)