class MoneyFmt:
    def dollarize(self, number):
        if number >= 0:
            return '${:,.2f}'.format(number)
        else:
            return '-${:,.2f}'.format(-number)

    def __init__(self, number):
        self.number = number

    def update(self, value):
        self.number = value
        return round(self.number, 2)

    def __repr__(self):
        return f'{round(self.number, 2)}'

    def __str__(self):
        return self.dollarize(self.number)

moneyfmt = MoneyFmt(12345678.021)
print(moneyfmt)
moneyfmt.update(100000.4567)
print(moneyfmt)
moneyfmt.update(-0.3)
print(moneyfmt)
print(repr(moneyfmt))
