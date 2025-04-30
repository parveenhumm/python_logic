
def main():
    divider1 : int = int(input("Please enter an integer to be divided:  "))
    quotient1 : int = int(input("Please enter an integer to divide by:  "))
    divider : int = divider1 // quotient1
    remainder: int = divider1 % quotient1

    print(f"The result of this division is {divider} with a remainder of {remainder}")
    

if __name__ == "__main__":
    main()