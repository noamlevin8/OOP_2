from Post import Post


class SalePost(Post):
    def __init__(self, owner, product, price, location):
        super().__init__(owner)
        self.product = product
        self.price = price
        self.location = location
        self.sold = False

    def __str__(self):
        s = f"{self.owner} posted a product for sale:"
        if self.sold == False:
            s += "For sale! "
        else:
            s += "Sold!"
        return s + f"{self.product}, price: {self.price}, pickup from: {self.location}"
