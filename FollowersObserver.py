from Observer import Observer

# Observer as follower
class FollowersObserver(Observer):
    def __init__(self, user):
        self.__user = user

    # Updating the follower
    def update(self, other):
        self.__user.add_to_history(f"{other.get_name()} has a new post")