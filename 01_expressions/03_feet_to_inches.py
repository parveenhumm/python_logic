
inches_in_foot  : int = 12 

def main():
    length_in_feet : float = float(input("Enter the length in feets: "))
    conversion:float = float(inches_in_foot)
    result:float = length_in_feet*conversion

    print(f"The {length_in_feet} in inches: {result}")


if __name__ == "__main__":
    main()