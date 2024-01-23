def calculate_energy(mass):

    speed_of_light = 300000000
    # Energy calculation
    energy = mass * speed_of_light ** 2
    return energy

def main():

    mass = float(input("Enter mass in kilograms: "))
    # Calculate energy
    energy = calculate_energy(mass)
    # Print the result
    print(int(energy))


main()
