def main():
    x = 5
    y = 10
    print(Calculator.add(x,y))

class Calculator():
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def div(self, x, y):
        try:
            division = x / y
        except ZeroDivisionError:
            raise ZeroDivisionError("No division by 0!")

        return division

if __name__ == "__main__":
    main()
