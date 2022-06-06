class Money:
    """
    Money class automatically change the input value into the maximum required currency.
    """
    def __init__(self, value: int):
        if value < 0:
            raise ValueError("Input value should be greater than 0.")
        self.value = value
        self.thousand = self.value // 1000
        self.five_hundred = (self.value % 1000) // 500
        self.two_hundred = ((self.value % 1000) % 500) // 200
        self.hundred = (((self.value % 1000) % 500) % 200) // 100
        self.fifty = ((((self.value % 1000) % 500) % 200) % 100) // 50
        self.one = self.value % 5
        self.five = ((self.value - self.one) % 10) // 5
        self.ten = ((self.value - self.one - 5 * self.five) % 50) // 10

    def __str__(self):
        return f"(1000, 500, 200, 100, 50, 10, 5, 1):" \
               f" {(self.thousand, self.five_hundred, self.two_hundred, self.hundred, self.fifty, self.ten, self.five, self.one)}"


def main():
    m1 = Money(0)
    print(m1)


if __name__ == '__main__':
    main()
