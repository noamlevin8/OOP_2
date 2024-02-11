class Post():
    def __init__(self, owner):
        self.owner = owner

    def like(self, user):
        print(f"notification to {self.owner}: {user.name} liked your post")
    def comment(self, user, text):
        print(f"notification to {self.owner}: {user.name} commented on your post: {text}")

    def __str__(self):
        pass