class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.following = []
        self.connected = True

    def follow(self, other):
        if other.name not in self.following:
            self.following.append(other.name)
            print(f"{self.name} started following {other.name}")

    def unfollow(self, other):
        if other.name in self.following:
            self.following.remove(other.name)
            print(f"{self.name} unfollowed {other.name}")

    #needs change
    def print_notifications(self):
        print("notification")

    def connection(self, state):
        if state == True and self.connected == False:
            self.connected = True
            print("connected")
        elif state == False and self.connected == True:
            self.connected = False
            print("disconnected")

    def __str__(self):
        return f"User name: {self.name}, Number of posts: , Number of followers: "