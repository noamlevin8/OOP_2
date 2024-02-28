from abc import ABC, abstractmethod

# Abstract class
class Post(ABC):
    @abstractmethod
    def __init__(self, owner):
        self.__owner = owner

    def like(self, user):
        # Checking that we don't notify on ourselves
        if user != self.__owner:
            if self.__owner.get_connection():
                s = f"{user.get_name()} liked your post"
                # Adding the massage to the notification history
                self.__owner.add_to_history(s)
                print(f"notification to {self.__owner.get_name()}: {s}")
            else:
                raise ConnectionError("User not connected")

    def comment(self, user, text):
        # Checking that we don't notify on ourselves
        if user != self.__owner:
            if self.__owner.get_connection():
                s = f"{user.get_name()} commented on your post"
                # Adding the massage to the notification history
                self.__owner.add_to_history(s)
                print(f"notification to {self.__owner.get_name()}: {s}: {text}")
            else:
                raise ConnectionError("User not connected")

    @abstractmethod
    def __str__(self):
        pass