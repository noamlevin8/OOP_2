from FollowersObserver import FollowersObserver


class User():
    # User constractor
    def __init__(self, name, password):
        # The name of the user
        self.__name = name
        # The password of the user
        self.__password = password
        # List if the users I follow
        self.__following = []
        # List of the users that follow me
        self.__followers = []
        # List of all the notification history
        self.__history = []
        # True if I'm connected and False if I'm not
        self.__connected = True

    # Following another user
    def follow(self, other):
        # I have to be connected in order to follow another user
        if self.__connected:
            # Checking that I don't already follow other
            if other.get_name() not in self.__following:
                # Adding other's name to my following list
                self.__following.append(other.get_name())
                # Adding my name to other's followers list
                other.get_followers().append(FollowersObserver(self))
                print(f"{self.__name} started following {other.get_name()}")

    # Unfollowing another user
    def unfollow(self, other):
        # I have to be connected in order to unfollow another user
        if self.__connected:
            # Checking that I follow other
            if other.get_name() in self.__following:
                # Removing other's name from my following list
                self.__following.remove(other.get_name())
                # Removing my name from other's followers list
                other.get_followers().remove(self)
                print(f"{self.__name} unfollowed {other.get_name()}")

    # Printing all notification history
    def print_notifications(self):
        print(f"{self.__name}'s notifications:")
        for notification in self.__history:
            print(f"\n{notification}")

    # Setting connection state
    def connection(self, state):
        # Checking if I'm not already connected
        if state == True and self.__connected == False:
            self.__connected = True
            print(f"{self.__name} connected")
        # Checking if I'm not already disconnected
        elif state == False and self.__connected == True:
            self.__connected = False
            print(f"{self.__name} disconnected")

    # Publishing a post
    def publish_post(self):
        self.notify_followers()

    # Adding notification
    def add_to_history(self, s):
        self.__history.append(s)

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password

    def get_followers(self):
        return self.__followers

    def notify_followers(self):
        for follower in self.__followers:
            follower.update(self)

    # Print user's details
    def __str__(self):
        return f"User name: {self.__name}, Number of posts: , Number of followers: {len(self.__followers)}"