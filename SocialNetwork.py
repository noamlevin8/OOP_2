from User import User

# Singleton class
class SocialNetwork():

    # Singleton class constractor
    def __new__(cls, name):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SocialNetwork, cls).__new__(cls)
            # The name of the network
            cls.instance.__name = name
            # The list of all the users in the network
            cls.instance.__user_list = []
            print(f"The social network {cls.instance.__name} was created!")
        return cls.instance

    # Signing up to the network
    def sign_up(self, name, password):
        # Checking if the username is already in use
        used = False
        for index, user in enumerate(self.__user_list):
            if user.get_name() == name:
                used = True
                break
        # Building a new user
        if not used:
            # Checking if the password is valid
            if len(password) >= 4 and len(password) <= 8:
                user = User(name, password)
                self.__user_list.append(user)
                return user
            else:
                raise ArithmeticError("Password not between 4 and 8 characters")
        else:
            raise NameError("Name already taken")

    # Logging into the network
    def log_in(self, name, password):
        # Searching the user
        for index, user in enumerate(self.__user_list):
            if user.get_name() == name:
                # Checking if it is the correct password
                if user.get_password() == password:
                    user.connection(True)
                    break
                else:
                    raise ArithmeticError("Password incorrect")

        raise Exception("User not found")

    # Logging out of the network
    def log_out(self, name):
        # Searching the user
        for index, user in enumerate(self.__user_list):
            if user.get_name() == name:
                user.connection(False)
                break

        raise Exception("User not found")

    # Print network's details
    def __str__(self):
        s = f"{self.__name} social network:"
        # Adding all of the users details
        for user in self.__user_list:
            s += "\n" + user.__str__()
        return s +"\n"