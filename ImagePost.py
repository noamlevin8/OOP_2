from Post import Post
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Extends Post
class ImagePost(Post):
    def __init__(self, owner, image):
        super().__init__(owner)
        self.__image = image

    # Displaying the image
    def display(self):
        img = mpimg.imread(self.__image)
        plt.imshow(img)
        plt.show()
        print("Shows picture")

    def __str__(self):
        return f"{self._Post__owner.get_name()} posted a picture\n"