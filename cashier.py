from change import Money


class Cashier(Money):
    """
    A Taiwanese Cashier that works with NTD.
    """

    def __init__(self, value):
        super().__init__(value)

    def make_change(self, cargo_price: int, given_money: int):
        """
        Make change from your cashier
        :param cargo_price: int
        :param given_money: int
        :return:
        """
        if given_money < cargo_price:
            raise ValueError("Given Money should be greater than the cargo price.")

        change = given_money - cargo_price

        while change > self.value:
            print("You don't have enough money for change.")
            self.top()

        else:
            """
            The available currency that can return to the customer depends on the money you have in your cashier.
            """
            pass

    def top(self, value=1000):
        """
        Automatically top 1000 into the cashier if the value isn't specified.
        :param value: int
        :return: None
        """
        print(f"You currently have {self.value}.\n")
        self.value += value
        print(f"{value} added to your cashier\nYou currently have {self.value}.")



def main():
    c = Cashier(129)
    c.make_change(170, 1000)



if __name__ == '__main__':
    main()
