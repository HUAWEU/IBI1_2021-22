class Stsff (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def location_role(self, other):
        print(self.x + " " + self.y + " " + other.x + " " + other.y)


c = Stsff("name", "family_name")
d = Stsff("location", "role")
print(c.location_role(d))
