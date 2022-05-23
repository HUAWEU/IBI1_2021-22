class Stsff (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def location_role(self, other):
        print(self.x + " " + self.y + " " + other.x + " " + other.y)


name = input('Please type the staff name (just name not include last name):')
family_name = input('Please type the staff last name:')
location = input('Please type your location (International Campus or Edinburgh):')
role = input('Please type your role (leadership, faculty, or administration):')
c = Stsff(name, family_name)
d = Stsff(location, role)
print(c.location_role(d))
