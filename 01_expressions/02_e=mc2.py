
def main():
    mass: float = float(input("Enter the mass(kg) of the object: "))
    speed_of_light: float = float(299792458)
    energy: float = mass*(speed_of_light**2)

    print(f"e = m*C^2")

    print(f"mass = {mass} kg")

    print(f"C = {speed_of_light} m/s")
    
    print(f"{energy} joules of energy!")


if __name__ == "__main__":
    main()