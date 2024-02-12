class Post():
    def __init__(self, owner):
        self.__owner = owner

    def like(self, user):
        s = f"{user.get_name()} liked your post"
        user.add_to_history(s)
        print(f"notification to {self.__owner.get_name()}: {s}")

    def comment(self, user, text):
        s = f"{user.get_name()} commented on your post"
        user.add_to_history(s)
        print(f"notification to {self.__owner.get_name()}: {s}: {text}")

    def __str__(self):
        pass