<<<<<<< HEAD
class Stsff (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def location_role(self, other):
        print(self.x + " " + self.y + " " + other.x + " " + other.y)


c = Stsff("name", "family_name")
d = Stsff("location", "role")
print(c.location_role(d))
=======
class Stsff (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def location_role(self, other):
        print(self.x + " " + self.y + " " + other.x + " " + other.y)


c = Stsff("name", "family_name")
d = Stsff("location", "role")
print(c.location_role(d))
>>>>>>> e22e09b592cc8a054107ad38ad83d7f407d9cd31
