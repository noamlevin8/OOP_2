from User import User


class SocialNetwork():

    # Singleton class constractor
    def __new__(cls, name):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SocialNetwork, cls).__new__()
            cls.instance.name = name
            cls.instance.user_list = []
        return cls.instance

    def sign_up(self, name, password):
        used = False
        for index, user in enumerate(self.user_list):
            if user.name == name:
                used = True
                break
        if not used:
            if len(password) >= 4 and len(password) <= 8:
                user = User(name, password)
                self.user_list.append(user)

    def log_in(self, name, password):
        for index, user in enumerate(self.user_list):
            if user.name == name:
                if user.password == password:
                    user.connection(True)
                # incorrect password
                break

    def log_out(self, name):
        for index, user in enumerate(self.user_list):
            if user.name == name:
                user.connection(False)
                break

    def __str__(self):
        return "Social Network"