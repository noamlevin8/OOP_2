class User():
    # User constractor
    def __init__(self, name, password):
        # The name of the user
        self.name = name
        # The password of the user
        self.password = password
        # List if the users I follow
        self.following = []
        # List of the users that follow me
        self.followers = []
        # List of all the notification history
        self.history = []
        # True if I'm connected and False if I'm not
        self.connected = True

    # Following another user
    def follow(self, other):
        # I have to be connected in order to follow another user
        if self.connected:
            # Checking that I don't already follow other
            if other.name not in self.following:
                # Adding other's name to my following list
                self.following.append(other.name)
                # Adding my name to other's followers list
                other.followers.append(self.name)
                print(f"{self.name} started following {other.name}")

    # Unfollowing another user
    def unfollow(self, other):
        # I have to be connected in order to unfollow another user
        if self.connected:
            # Checking that I follow other
            if other.name in self.following:
                # Removing other's name from my following list
                self.following.remove(other.name)
                # Removing my name from other's followers list
                other.followers.remove(self.name)
                print(f"{self.name} unfollowed {other.name}")

    # Printing all notification history
    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for notification in self.history:
            print(f"\n{notification}")

    # Setting connection state
    def connection(self, state):
        # Checking if I'm not already connected
        if state == True and self.connected == False:
            self.connected = True
            print(f"{self.name} connected")
        # Checking if I'm not already disconnected
        elif state == False and self.connected == True:
            self.connected = False
            print(f"{self.name} disconnected")

    # Publishing a post
    def publish_post(self):
        return

    # Adding notification
    def add_to_history(self, s):
        self.history.append(s)

    # Print user's details
    def __str__(self):
        return f"User name: {self.name}, Number of posts: , Number of followers: {len(self.followers)}"