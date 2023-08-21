import json

class Storage:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email, password):
        if username in self.users:
            return False
        self.users[username] = {'email': email, 'password': password}
        self.save_data()
        return True

    def save_data(self):
        with open('data.json', 'w') as file:
            json.dump(self.users, file)

storage = Storage()
