from FollowersObserver import FollowersObserver
from PostFactory import PostFactory

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
        # Number of posts published by me
        self.__posts_num = 0
        # Me as Observer
        self.__obs = FollowersObserver(self)

    # Following another user
    def follow(self, other):
        # I have to be connected in order to follow another user
        if self.__connected:
            # Checking that I don't already follow other
            if other.get_name() not in self.__following:
                # Adding other's name to my following list
                self.__following.append(other.get_name())
                # Adding myself as an observer to other's followers list
                other.get_followers().append(self.__obs)
                print(f"{self.__name} started following {other.get_name()}")
            else:
                raise Exception("Already following")
        else:
            raise ConnectionError("User is not connected")

    # Unfollowing another user
    def unfollow(self, other):
        # I have to be connected in order to unfollow another user
        if self.__connected:
            # Checking that I follow other
            if other.get_name() in self.__following:
                # Removing other's name from my following list
                self.__following.remove(other.get_name())
                # Removing myself from other's followers list
                other.get_followers().remove(self.__obs)
                print(f"{self.__name} unfollowed {other.get_name()}")
            else:
                raise Exception("Don't already follow")
        else:
            raise ConnectionError("User is not connected")

    # Printing all notification history
    def print_notifications(self):
        print(f"{self.__name}'s notifications:")
        for notification in self.__history:
            print(f"{notification}")

    # Setting connection state
    def connection(self, status):
        # Checking if I'm not already connected
        if status == True and self.__connected == False:
            self.__connected = True
            print(f"{self.__name} connected")
        # Checking if I'm not already disconnected
        elif status == False and self.__connected == True:
            self.__connected = False
            print(f"{self.__name} disconnected")
        else:
            raise ConnectionError("Current status is the same as the given status")

    # Publishing a post
    def publish_post(self, post_type, content, price=None, loc=None):
        if self.__connected:
            # Creating a post
            post = PostFactory.create_post(post_type, self, content, price, loc)
            print(post)
            # Notifying followers
            self.notify_followers()
            self.__posts_num += 1
            return post
        else:
            raise ConnectionError("User is not connected")

    # Adding notification
    def add_to_history(self, s):
        self.__history.append(s)

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password

    def get_followers(self):
        return self.__followers

    def get_connection(self):
        return self.__connected

    # Notifying all my followers
    def notify_followers(self):
        for follower in self.__followers:
            follower.update(self)

    # Print user's details
    def __str__(self):
        return f"User name: {self.__name}, Number of posts: {self.__posts_num}, Number of followers: {len(self.__followers)}"