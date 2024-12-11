# Constants
FULLY_EXTENDED = 1  # Gear fully extended signal
NOT_EXTENDED = 0    # Gear not extended signal
GEAR_DOWN_SWITCH = 1  # Gear down switch activated
ALIGNMENT_PROPER = 0  # Proper alignment angle (in degrees)
MAX_LIFT_INTERVAL = 90  # Maximum angle for calculating lift

# Function to print the menu
def print_menu():
    print("Welcome to the Airplane Landing Gear Monitoring System")
    print("1. Check Landing Gear Status")
    print("2. Check Directional Gear Alignment")
    print("3. Calculate Lift")
    print("4. Exit")

# Function to check landing gear status
def check_landing_gear_status(gear1, gear2, gear3, gear_down_switch):
    if gear_down_switch == GEAR_DOWN_SWITCH:
        if gear1 == FULLY_EXTENDED and gear2 == FULLY_EXTENDED and gear3 == FULLY_EXTENDED:
            print("All landing gears are fully extended. Green LED ON for 10 seconds.")
        else:
            print("One or more landing gears failed to extend properly. Red LED ON.")
    else:
        print("Gear down switch is not activated.")

# Function to check directional gear alignment
def check_directional_gear_alignment(angle):
    if angle == ALIGNMENT_PROPER:
        print("Directional gear is properly aligned.")
    else:
        print(f"Directional gear is misaligned by {angle} degrees. Red LED ON.")

# Function to calculate airplane lift
def calculate_lift(velocity, air_density, wing_area, lift_coefficient):
    lift = 0.5 * air_density * velocity**2 * wing_area * lift_coefficient
    return lift

# Function to convert analog sensor data to binary (for directional gear)
def convert_to_binary(angle):
    if 0 <= angle <= MAX_LIFT_INTERVAL:
        return format(angle, '04b')  # Converting to 4-bit binary
    else:
        print("Invalid angle for conversion.")
        return None

# Main function to drive the program
def main():
    while True:
        print_menu()
        choice = input("Please enter your choice (1-4): ")

        if choice == "1":
            # Simulating gear status input
            gear1 = int(input("Enter status for Gear 1 (1 for extended, 0 for not extended): "))
            gear2 = int(input("Enter status for Gear 2 (1 for extended, 0 for not extended): "))
            gear3 = int(input("Enter status for Gear 3 (1 for extended, 0 for not extended): "))
            gear_down_switch = int(input("Enter status of Gear Down Switch (1 for activated, 0 for not activated): "))
            check_landing_gear_status(gear1, gear2, gear3, gear_down_switch)

        elif choice == "2":
            # Simulating directional gear input
            angle = int(input("Enter the angle of the directional gear (in degrees): "))
            check_directional_gear_alignment(angle)

        elif choice == "3":
            # Calculating lift
            velocity = float(input("Enter the velocity of the airplane (in m/s): "))
            air_density = float(input("Enter the air density (in kg/m^3): "))
            wing_area = float(input("Enter the wing area (in m^2): "))
            lift_coefficient = float(input("Enter the lift coefficient: "))
            lift = calculate_lift(velocity, air_density, wing_area, lift_coefficient)
            print(f"The calculated lift is {lift:.2f} Newtons.")

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
