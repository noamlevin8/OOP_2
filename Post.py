class Post():
    def __init__(self, owner):
        self.owner = owner

    def like(self, user):
        s = f"{user.name} liked your post"
        user.add_to_history(s)
        print(f"notification to {self.owner}: {s}")

    def comment(self, user, text):
        s = f"{user.name} commented on your post"
        user.add_to_history(s)
        print(f"notification to {self.owner}: {s}: {text}")

    def __str__(self):
        pass