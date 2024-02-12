from abc import ABC, abstractmethod

# Abstract class
class Post(ABC):
    def __init__(self, owner):
        self.__owner = owner

    def like(self, user):
        if user != self.__owner:
            s = f"{user.get_name()} liked your post"
            # Adding the massage to the notification history
            self.__owner.add_to_history(s)
            print(f"notification to {self.__owner.get_name()}: {s}")

    def comment(self, user, text):
        if user != self.__owner:
            s = f"{user.get_name()} commented on your post"
            # Adding the massage to the notification history
            self.__owner.add_to_history(s)
            print(f"notification to {self.__owner.get_name()}: {s}: {text}")

    @abstractmethod
    def __str__(self):
        pass