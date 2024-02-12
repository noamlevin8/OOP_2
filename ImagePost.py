from Post import Post
# from matplotlib import image as plt

# Extends Post
class ImagePost(Post):
    def __init__(self, owner, image):
        super().__init__(owner)
        self.__image = image

    # def display(self):
    #     plt.imshow(self.__image)

    def __str__(self):
        return f"{self.__owner.get_name()} posted a picture\n"