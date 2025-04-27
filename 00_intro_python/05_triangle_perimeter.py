
def main():
    side1 : float = float(input("The length of Triangle side 1 is: "))
    side2 : float = float(input("The length of Triangle side 2 is: "))
    side3 : float = float(input("The length of Triangle side 3 is: "))

    result = str(side1 + side2 + side3)
    print(f"The perimeter of Triangle is: {result}")

if __name__ == "__main__":
 main()