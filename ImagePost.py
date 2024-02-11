from Post import Post
# from matplotlib import image as plt


class ImagePost(Post):
    def __init__(self, owner, image):
        super().__init__(owner)
        self.image = image

    # def display(self):
    #     plt.imshow(self.image)

    def __str__(self):
        return f"{self.owner} posted a picture\n"