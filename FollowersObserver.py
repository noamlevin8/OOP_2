from Observer import Observer


class FollowersObserver(Observer):
    def __init__(self, user):
        self.__user = user
    def update(self, other):
        self.__user.add_to_history(f"{other.get_name()} has a new post")