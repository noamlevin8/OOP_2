class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.following = []
        self.followers = []
        self.history = []
        self.connected = True

    def follow(self, other):
        if other.name not in self.following:
            self.following.append(other.name)
            other.followers.append(self.name)
            print(f"{self.name} started following {other.name}")

    def unfollow(self, other):
        if other.name in self.following:
            self.following.remove(other.name)
            other.followers.remove(self.name)
            print(f"{self.name} unfollowed {other.name}")

    # needs change
    def print_notifications(self):
        print(f"{self.name}'s notifications:")

    def connection(self, state):
        if state == True and self.connected == False:
            self.connected = True
            print(f"{self.name} connected")
        elif state == False and self.connected == True:
            self.connected = False
            print(f"{self.name} disconnected")

    def __str__(self):
        return f"User name: {self.name}, Number of posts: , Number of followers: {len(self.followers)}"