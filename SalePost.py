from Post import Post


class SalePost(Post):
    def __init__(self, owner, product, price, location):
        super().__init__(owner)
        self.product = product
        self.price = price
        self.location = location
        self.sold = False

    def discount(self, discount_rate, password):
        if self.owner.password == password:
            self.price = self.price*((100-discount_rate)/100)
            print(f"Discount on {self.owner.name} product! the new price is: {self.price}")

    def sold(self, password):
        if self.owner.password == password:
            self.sold = True
            print(f"{self.owner.name}'s product is sold")

    def __str__(self):
        s = f"{self.owner.name} posted a product for sale:\n"
        if self.sold == False:
            s += "For sale!"
        else:
            s += "Sold!"
        return f"{s} {self.product}, price: {self.price}, pickup from: {self.location}"
