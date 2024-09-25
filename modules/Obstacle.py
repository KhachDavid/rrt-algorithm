import math

class Obstacle:
    def __init__(self, radius, cX, cY):
        self.radius = radius
        self.cX = cX
        self.cY = cY

    def is_inside(self, givenX, givenY):
        # x and y must satisfy (x - center_x)² + (y - center_y)² > radius².
        if ((givenX - self.cX) * (givenX - self.cX) +
        (givenY - self.cY) * (givenY - self.cY) <= self.radius * self.radius):
            return True
        else:
            return False
        
    def intersects_line(self, x1, y1, x2, y2):
        cx, cy, r = self.cX, self.cY, self.radius

        dx = x2 - x1
        dy = y2 - y1

        A = dx**2 + dy**2
        B = 2 * (dx * (x1 - cx) + dy * (y1 - cy))
        C = (x1 - cx)**2 + (y1 - cy)**2 - r**2

        discriminant = B**2 - 4 * A * C

        if discriminant < 0:
            return False
        else:
            t1 = (-B + math.sqrt(discriminant)) / (2 * A)
            t2 = (-B - math.sqrt(discriminant)) / (2 * A)

            return (0 <= t1 <= 1) or (0 <= t2 <= 1)
