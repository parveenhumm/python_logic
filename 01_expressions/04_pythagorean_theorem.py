import math

def  main():
    AB : float = float(input("Enter the length side AB of triangle: "))
    AC : float = float(input("Enter the length side AC of triangle: "))

    BC: float = math.sqrt(AB**2 + AC**2)

    print(f"The length of BC (the hypotenuse) is: {BC}")

if __name__ == "__main__":
    main()