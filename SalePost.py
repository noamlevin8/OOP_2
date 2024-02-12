from Post import Post


class SalePost(Post):
    def __init__(self, owner, product, price, location):
        super().__init__(owner)
        self.__product = product
        self.__price = price
        self.__location = location
        self.__sold = False

    def discount(self, discount_rate, password):
        if self.__owner.get_password() == password:
            self.__price = self.__price*((100-discount_rate)/100)
            print(f"Discount on {self.__owner.get_name()} product! the new price is: {self.__price}")

    def sold(self, password):
        if self.__owner.get_password() == password:
            self.__sold = True
            print(f"{self.__owner.get_name()}'s product is sold")

    def __str__(self):
        s = f"{self.__owner.get_name()} posted a product for sale:\n"
        if not self.__sold:
            s += "For sale!"
        else:
            s += "Sold!"
        return f"{s} {self.__product}, price: {self.__price}, pickup from: {self.__location}"
