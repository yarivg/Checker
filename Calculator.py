def main():
	x = 5
	y = 10
	print(Calculator.add(x,y))

class Calculator():

	def add(x, y):
		return x + y

	def sub(x, y):
		return x - y

if __name__ == "__main__":
    main()