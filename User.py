class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def follow(self, other):
        print(f"{self.name} started following {other.name}")

    def unfollow(self, other):
        print(f"{self.name} unfollowed {other.name}")

    #needs change
    def print_notifications(self):
        print("notification")