#initalization
class Thing:
    def __init__(self,price,size):
        self.price = price
        self.size = size

box = Thing(100,100)
print(box.price)
print(box.size)

class Desk(Thing):
    def __init__(self, price, size, width, height):
        #Thing.__init__(self,price,size)
        super().__init__(price,size)
        self.width = width
        self.height = height

    def __add__(self,desk):
        p=self.price+desk.price
        s=self.size+desk.size
        w=self.width+desk.width
        h=self.height+desk.height
        return Desk(p,s,w,h)
    def __str__(self):
        stats = """Price\tSize\tWidth\tHeight {price!s}\t{size!s}\t{width!s}\t{height!s}\t""".format(**vars(self))
        return stats
    def __repr__(self):
        stats = '''Desk({price!s},{size!s},{width!s},{height!s})'''.format(**vars(self))
        return stats
desk=Desk(400,300,200,100)
things = {"box":Thing(10,10),"desk":Desk(700,80,20,40),"thing":Desk(800,600,20,300)}
for key, item in things.items():
    print(key, item, repr(item))
print(desk)
print(repr(desk))
desk2 = eval(repr(desk))
print(desk2)

a = Desk(300,400,500,600)
b= Desk(500,600,700,800)
        
