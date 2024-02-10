class SocialNetwork():

    # Singleton class constractor
    def __new__(cls, name):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SocialNetwork, cls).__new__()
            cls.instance.name = name
        return cls.instance

    def sign_up(self, name, password):

    def log_in(self, name, password):

    def log_out(self, name):

    def __str__(self):
        return "Social Network"