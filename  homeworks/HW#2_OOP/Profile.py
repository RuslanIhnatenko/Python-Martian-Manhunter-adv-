class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

        profile = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday, self.age, self.sex]
        self.profile = profile

    def list_params(self):
        return print(self.profile)


pr = Profile("Ruslan", "Ihnatenko", "+38099133488","Dnipro", "rusign29@gmail.com", "05.05.1998", 23, "Man")
pr.list_params()
