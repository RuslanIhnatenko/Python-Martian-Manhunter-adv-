class Human:
    def __init__(self):
        tattoo1 = Arm("It's my life")
        tattoo2 = Arm("We have a time")
        self.tattoos = [tattoo2, tattoo1]


class Arm:
    def __init__(self, content):
        self.content = content


human = Human()
for tattoo in human.tattoos:
    print(tattoo.content)



class CellPhone:
    def __init__(self, mobile_connection):
        self.mobile_connection = mobile_connection




class Screen:
    def __init__(self, type_connection):
        self.type_connection = type_connection


screen = Screen("MTC")
print(screen.type_connection)
my_phone = CellPhone(screen)
print(my_phone.mobile_connection.type_connection)