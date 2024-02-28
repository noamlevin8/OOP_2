from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost

# Factory
class PostFactory():
    @staticmethod
    def create_post(post_type, owner, content, price=None, loc=None):
        if post_type == "Text":
            return TextPost(owner, content)
        elif post_type == "Image":
            return ImagePost(owner, content)
        elif post_type == "Sale":
            return SalePost(owner, content, price, loc)
        else:
            raise TypeError("Invalid post type")