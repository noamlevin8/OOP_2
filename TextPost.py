from Post import Post


class TextPost(Post):
    def __init__(self, owner, text):
        super().__init__(owner)
        self.text = text

    def __str__(self):
        return f"{self.owner} published a post:\n {self.text}"

