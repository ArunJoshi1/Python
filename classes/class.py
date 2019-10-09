class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print(f'point is moving')
    def draw(self):
        print(f'point is draw')
point = Point(10,20)
point.move()
print(point.x,point.y)
point.draw()