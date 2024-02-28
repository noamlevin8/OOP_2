from Post import Post

# Extends Post
class SalePost(Post):
    def __init__(self, owner, product, price, location):
        super().__init__(owner)
        self.__product = product
        self.__price = price
        self.__location = location
        self.__sold = False

    def discount(self, discount_rate, password):
        if self._Post__owner.get_connection():
            # Checking the password
            if self._Post__owner.get_password() == password:
                # Updating the price
                self.__price = self.__price*((100-discount_rate)/100)
                print(f"Discount on {self._Post__owner.get_name()} product! the new price is: {self.__price}")
            else:
                raise ArithmeticError("Password incorrect")
        else:
            raise ConnectionError("User not connected")

    def sold(self, password):
        if self._Post__owner.get_connection():
            # Checking the password
            if self._Post__owner.get_password() == password:
                # Updating status
                self.__sold = True
                print(f"{self._Post__owner.get_name()}'s product is sold")
            else:
                raise ArithmeticError("Password incorrect")
        else:
            raise ConnectionError("User not connected")

    def __str__(self):
        s = f"{self._Post__owner.get_name()} posted a product for sale:\n"
        if not self.__sold:
            s += "For sale!"
        else:
            s += "Sold!"
        return f"{s} {self.__product}, price: {self.__price}, pickup from: {self.__location}\n"
