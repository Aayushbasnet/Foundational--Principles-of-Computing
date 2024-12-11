"""
Student ID: u3284617
Assignment: Assessment 1: Foundational Principles of Computing.
Submission Date: 2024-09-20
Tutorial time: Tuesday 3:30 p.m. to 5:30 p.m.
"""


import time
from typing import List
import math

# Constant value for types of menu
MENU_TYPE_CONSTANTS = {
    "mainMenu": "main_menu",
    "menuAfterGearDownIsActivated": "menu_after_gear_down_is_activated",
    "monitorLandingGearAndAlignmentMenu": "monitor_landing_gear_and_alignment_menu",
    "checkGearPositionsAndAlignmentMenu": "check_gear_positions_and_alignment_menu",
    "calculateAndDisplayLiftOfAircraftMenu": "calculate_and_display_lift_of_aircraft_menu",
}

# global state with standard value (no modification on values)
global_state = {
    "gear_down_status": None,
    "nose_gear_down_status": None,
    "left_main_gear_down_status": None,
    "right_main_gear_down_status": None,
    "alignment_angle": None,
    "green_led": None,
    "red_led": None,
    "altitude": None,
    "velocity": None,
    "wing_area": None,
    "angle_of_attack": None,
    "lift": None
}

def get_global_state() -> dict:
    """
    Retrieves the current global state of the system.
    This function returns the global state dictionary, which contains information about the system's current configuration, including gear positions, alignment, LED statuses, and other relevant variables.

    :return:
        dict: The global state dictionary, which holds the current status values such as gear down status, landing gear positions, alignment angle, LED statuses, and any other relevant state data.
    """
    return global_state

# black box log
black_box_log = {
    "gear_down_switch_status": None,
    "landing_gear_position_status":{
        "nose_gear_down_switch_status": None,
        "left_main_gear_down_switch_status": None,
        "right_main_gear_down_switch_status": None,
    },
    "alignment_angle": None,
    "lift": None,
    "led_status":{
        "green_led": None,
        "red_led": None
    }
}

def convert_value_into_binary(value: int) -> str:
    """
    Converts an integer value into its binary representation.

    :param value: int: The integer value to be converted to binary.

    :returns:
        str: The binary representation of the integer value (e.g., '0b101').
        None: If the value cannot be converted, returns None and prints an error message.

    :raises Exception: Handles any exception that occurs during the conversion process.
    """
    try:
        return bin(value)
    except Exception as e:
        print(f"\n Cannot convert value {value} to binary. Error: {e}")
        return None

def set_black_box_log(state: dict) -> None:
    """
    Converts the relevant state values into binary and stores them in the black box log.

    The function handles converting gear positions, alignment angle, lift, and LED statuses into
    their respective binary forms. It also maps the alignment angle and discretizes the lift value
    into the range 0-9 before converting them to binary. If any state value is None, it skips the
    conversion for that particular value.

    :param state: dict: The shared state dictionary containing values such as gear down status, landing gear positions, alignment angle, lift, and LED statuses.

    :returns:
        None: The values are stored in the `black_box_log` in binary form.

    :raises Exception: If any error occurs during the conversion or storage process, an error message is printed.
    """
    try:
        # converts all the value into binary and store in black_box_log
        black_box_log["gear_down_switch_status"] = convert_value_into_binary(state["gear_down_status"]) if state["gear_down_status"] is not None else None
        # Convert landing gear positions into binary
        black_box_log["landing_gear_position_status"] = {
            "nose_gear_down_switch_status": convert_value_into_binary(state["nose_gear_down_status"]) if state["nose_gear_down_status"] is not None else None,
            "left_main_gear_down_switch_status": convert_value_into_binary(state["left_main_gear_down_status"]) if state["left_main_gear_down_status"] is not None else None,
            "right_main_gear_down_switch_status": convert_value_into_binary(state["right_main_gear_down_status"]) if state["right_main_gear_down_status"] is not None else None,
        }
        # Convert the alignment angle into binary equivalent by mapping it into range of 0 to 9
        mapped_alignment_angle_in_range_0_to_9 = map_alignment_angle_in_range_between_0_to_9(state["alignment_angle"]) if state["alignment_angle"] is not None else None
        black_box_log["alignment_angle"] = convert_value_into_binary(mapped_alignment_angle_in_range_0_to_9) if state["alignment_angle"] is not None else None

        # Convert the lift value into discretize value (0-9) and then into binary equivalent
        discretize_lift_value_in_range_between_0_to_9 = get_discretize_lift_value_in_range_between_0_to_9(state["lift"]) if state["lift"] is not None else None
        black_box_log["lift"] = convert_value_into_binary(discretize_lift_value_in_range_between_0_to_9) if state["lift"] is not None else None

        # Convert LED status into binary
        black_box_log["led_status"] = {
            "green_led": convert_value_into_binary(state["green_led"]) if state["green_led"] is not None else None,
            "red_led": convert_value_into_binary(state["red_led"]) if state["red_led"] is not None else None,
        }
    except Exception as e:
        print(f"\n Cannot set black box log. Error: {e}")
        handle_menu_after_gear_down_switch_is_activated()


def get_black_box_log() -> dict:
    """
    Retrieves the current black box log after converting the global state into binary.

    This function calls `set_black_box_log()` to convert the current global state values
    into their binary representations and stores them in the `black_box_log`. It then
    returns the updated black box log.

    :returns:
        dict: The `black_box_log` dictionary containing the binary representations of the
              system state such as gear down status, landing gear positions, alignment
              angle, lift, and LED statuses.
    """
    set_black_box_log(global_state)
    return black_box_log

def map_alignment_angle_in_range_between_0_to_9(alignment_angle: int)-> int | None:
    """
    Maps the alignment angle into the range of 0 to 9 by dividing the angle by 10 and
    taking the floor value of the result.

    This is useful for discretizing the alignment angle, which can range from 0 to 90 degrees,
    into a smaller scale of 0 to 9 for further processing.

    :parameters alignment_angle: int: The alignment angle in degrees (typically from 0 to 90).

    :returns:
        int: The mapped alignment angle in the range of 0 to 9.
        None: If an exception occurs (e.g., a non-numeric input), None is returned.

    :raises Exception: Catches any error during the mapping process and prints an error message.
    """
    try:
        return math.floor(alignment_angle / 10)
    except Exception as e:
        print(f"\n Cannot map alignment angle between 0 to 9. Error: {e}")
        return None

def get_discretize_lift_value_in_range_between_0_to_9(lift_value: float)-> int | None:
    """
    Discretizes the lift value into a range between 0 and 9 based on the magnitude of the lift.

    The function divides the lift value into predefined ranges and returns an integer between 0 and 9
    representing the corresponding range. If the lift value is below 0 or cannot be classified,
    the function returns None.

    :param lift_value: float: The lift value (in Newtons) to be discretized.

    :returns:
        int: A value between 0 and 9, corresponding to the range in which the lift falls.
        None: If the lift value is invalid or outside the handled ranges.
    """

    if 0 <= lift_value <= 100000:
        return 0
    elif 100000 < lift_value <= 200000:
        return 1
    elif 200000 < lift_value <= 300000:
        return 2
    elif 300000 < lift_value <= 400000:
        return 3
    elif 400000 < lift_value <= 500000:
        return 4
    elif 500000 < lift_value <= 600000:
        return 5
    elif 600000 < lift_value <= 700000:
        return 6
    elif 700000 < lift_value <= 800000:
        return 7
    elif 800000 < lift_value <= 900000:
        return 8
    elif 900000 < lift_value:
        return 9
    else:
        return None

# coefficient of lift according to angle of attack
coefficient_of_lift_as_per_angle_of_attack = {
    0: 0.2,
    6: 0.6,
    8: 0.8,
    10: 1.0,
    12: 1.1
}

def get_air_density_according_to_altitude(altitude: float) -> float:
    """
    Returns the air density (in kg/m³) according to the altitude, based on a conversion
    from slug/ft³ to kg/m³. The function uses approximate values for different altitude ranges.

    :param altitude: float: The altitude in meters at which to determine the air density.

    :returns:
        float: The air density in kg/m³ corresponding to the altitude.
               If the altitude is negative or an unsupported range, the function returns 0.
    """

    if 0 <= altitude < 1000:
        return 0.002377 * 515.379
    elif 1000 <= altitude < 2000:
        return 0.002308 * 515.379
    elif 2000 <= altitude < 3000:
        return 0.002241 * 515.379
    elif 3000 <= altitude < 4000:
        return 0.002175 * 515.379
    elif 4000 <= altitude < 5000:
        return 0.002111 * 515.379
    elif 5000 <= altitude < 6000:
        return 0.002048 * 515.379
    elif 6000 <= altitude < 7000:
        return 0.001987 * 515.379
    elif 7000 <= altitude < 8000:
        return 0.001927 * 515.379
    elif 8000 <= altitude < 9000:
        return 0.001868 * 515.379
    elif 9000 <= altitude < 10000:
        return 0.001811 * 515.379
    elif 10000 <= altitude < 15000:
        return 0.001755 * 515.379
    elif 15000 <= altitude < 20000:
        return 0.001496 * 515.379
    elif 20000 <= altitude < 25000:
        return 0.001266 * 515.379
    elif 25000 <= altitude < 30000:
        return 0.001065 * 515.379
    elif 30000 <= altitude < 35000:
        return 0.000889 * 515.379
    elif 35000 <= altitude < 36089:
        return 0.000737 * 515.379
    elif 36089 <= altitude < 40000:
        return 0.000706 * 515.379
    elif 40000 <= altitude < 50000:
        return 0.000585 * 515.379
    elif 50000 <= altitude < 55000:
        return 0.000362 * 515.379
    elif 55000 <= altitude:
        return 0.000285 * 515.379
    else:
        return 0



def set_gear_down_status(state: dict, status: int) -> None:
    """
    Sets the gear down status in the shared state dictionary.

    :param state: dict: The shared state containing the current status states.
    :param status: int: The status to set.

    :return: None
    """
    state["gear_down_status"] = status

def get_gear_down_status(state: dict) -> int:
    """
    Retrieves the gear down status from the shared state dictionary.

    :param state: dict: The shared state containing the gear down status

    :returns: int: The status of gear down status.
    """
    return state["gear_down_status"]

def set_nose_gear_down_status(state: dict, status: int) -> None:
    """
    Sets the nose gear down status in the shared state dictionary.

    :param state: dict: The shared state containing the current status states.
    :param status: int: The status to set.

    :return: None
    """
    state["nose_gear_down_status"] = status

def get_nose_gear_down_status(state: dict) -> int:
    """
    Retrieves the nose gear down status from the shared state dictionary.

    :param state: dict: The shared state containing the nose gear down status

    :returns: int: The status of nose gear down status.
    """
    return state["nose_gear_down_status"]

def set_left_main_gear_down_status(state: dict, status: int) -> None:
    """
    Sets the left main gear down status in the shared state dictionary.

    :param state: dict: The shared state containing the current status states.
    :param status: int: The status to set.

    :return: None
    """
    state["left_main_gear_down_status"] = status

def get_left_main_gear_down_status(state: dict) -> int:
    """
    Retrieves the left main gear down status from the shared state dictionary.

    :param state: dict: The shared state containing the left main gear down status

    :returns: int: The status of left main gear down status.
    """
    return state["left_main_gear_down_status"]

def set_right_main_gear_down_status(state: dict, status: int) -> None:
    """
    Sets the right main gear down status in the shared state dictionary.

    :param state: dict: The shared state containing the current status states.
    :param status: int: The status to set.

    :return: None
    """
    state["right_main_gear_down_status"] = status

def get_right_main_gear_down_status(state: dict) -> int:
    """
    Retrieves the right main gear down status from the shared state dictionary.

    :param state: dict: The shared state containing the right main gear down status

    :returns: int: The status of right main gear down status.
    """
    return state["right_main_gear_down_status"]

def set_alignment_angle(state: dict, angle: int) -> None:
    """
    Sets the alignment angle in the shared state dictionary.

    :param state: dict: The shared state containing the current status states.
    :param angle: int: The status to set.

    :return: None
    """
    state["alignment_angle"] = angle

def get_alignment_angle(state: dict) -> int:
    """
    Retrieves the alignment angle from the shared state dictionary.

    :param state: dict: The shared state containing the alignment angle

    :returns: int: The status of alignment angle.
    """
    return state["alignment_angle"]

def set_green_led_status(state: dict, status: int) -> None:
    """
    Sets the Green LED status in the shared state dictionary.

    :param state: dict: The shared state containing the current status states.
    :param status: int: The status to set.

    :return: None
    """
    state["green_led"] = status

def get_green_led_status(state: dict) -> int:
    """
    Retrieves the Green LED status from the shared state dictionary.

    :param state: dict: The shared state containing the Green LED status

    :returns: int: The status of Green LED status.
    """
    return state["green_led"]

def set_red_led_status(state: dict, status: int) -> None:
    """
    Sets the Red LED status in the shared state dictionary.

    :param state: dict: The shared state containing the current status states.
    :param status: int: The status to set.

    :return: None
    """
    state["red_led"] = status

def get_red_led_status(state: dict) -> int:
    """
    Retrieves the Red LED status from the shared state dictionary.

    :param state: dict: The shared state containing the Red LED status

    :returns: int: The status of Red LED status.
    """
    return state["red_led"]

def set_altitude(state: dict, value: float) -> None:
    """
    Sets the altitude in the shared state dictionary.

    :param state: dict: The shared state containing the current status states.
    :param value: float: The status to set.

    :return: None
    """
    state["altitude"] = value

def get_altitude(state: dict) -> float:
    """
    Retrieves the altitude from the shared state dictionary.

    :param state: dict: The shared state containing the value of altitude.

    :returns: int: The value of altitude.
    """
    return state["altitude"]

def set_velocity(state: dict, value: float) -> None:
    """
    Sets the velocity in the shared state dictionary.

    :param state: dict: The shared state containing the current status states.
    :param value: float: The status to set.

    :return: None
    """
    state["velocity"] = value

def get_velocity(state: dict) -> float:
    """
    Retrieves the velocity from the shared state dictionary.

    :param state: dict: The shared state containing the value of velocity.

    :returns: int: The value of velocity.
    """
    return state["velocity"]

def set_wing_area(state: dict, value: float) -> None:
    """
    Sets the wing area in the shared state dictionary.

    :param state: dict: The shared state containing the current status states.
    :param value: float: The status to set.

    :return: None
    """
    state["wing_area"] = value

def get_wing_area(state: dict) -> float:
    """
    Retrieves the wing area from the shared state dictionary.

    :param state: dict: The shared state containing the value of wing area.

    :returns: int: The value of wing area.
    """
    return state["wing_area"]

def set_angle_of_attack(state: dict, value: int) -> None:
    """
    Sets the angle of attack in the shared state dictionary.

    :param state: dict: The shared state containing the current status states.
    :param value: float: The status to set.

    :return: None
    """
    state["angle_of_attack"] = value

def get_angle_of_attack(state: dict) -> int:
    """
    Retrieves the wing area from the shared state dictionary.

    :param state: dict: The shared state containing the value of wing area.

    :returns: int: The value of wing area.
    """
    return state["angle_of_attack"]

def get_menu_message(menu_type: str) -> str:
    """
    Generates the appropriate menu message to display based on the menu type provided.

    :param menu_type: The type of menu to be displayed, as defined in MENU_TYPE_CONSTANTS.

    :return:
        str: A string containing the appropriate menu options for the user.

    :raises ValueError: If the menu type is not a valid menu type.
    """

    if "main_menu" == menu_type.lower():
        return "--*** Main Menu ***-- \n 1) Activate Gear down switch \n 2) Exit System"
    elif "menu_after_gear_down_is_activated" == menu_type.lower():
        return "\n--*** Gear down activation Menu ***-- \n 1) Monitor landing gears and their alignments \n 2) View Black Box Log \n 3) Deactivate gear down switch \n 4) Exit System"
    elif "monitor_landing_gear_and_alignment_menu" == menu_type.lower():
        return "\n--*** Monitor landing gear and alignment menu ***-- \n 1) Check Gear Positions and Alignment \n 2) Calculate and Display the lift of aircraft \n 3) <- Go back \n 4) Deactivate the gear down switch \n 5) Exit System"
    elif "check_gear_positions_and_alignment_menu" == menu_type.lower():
        return "\n--*** Check gear positions and alignment menu ***-- "
    elif "calculate_and_display_lift_of_aircraft_menu" == menu_type.lower():
        return "\n--*** Calculate and display lift of the aircraft menu ***--"
    else:
        raise ValueError(f"Invalid menu type provided: {menu_type}")

def get_integer_input_from_user(prompt: str = "Select an option ") -> int:
    """
    Prompts the user to input an integer value and validates the input.

    :param prompt: The message to display to the user when asking for input. Defaults to "Select an option:".

    :return: int: The user's input as a valid integer.

    :raises ValueError: If the user input is not a valid integer.
    :raises Exception: If an unexpected error occurs during input handling.
    """

    try:
        choice = int(input(prompt))
        return choice
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid integer.")
    except Exception as e:
        raise Exception(f"Unexpected error: {str(e)}. Please try again.")


def display_menu(menu_type: str) -> None:
    """
    Displays the menu message

    :return: None
    """

    print(get_menu_message(menu_type))


def validate_menu_selection_with_validation_option_list(menu_choice: int, validation_option_list: List[int] = [1, 2]) -> bool:
    """
    Validates the menu selection made by the user against a provided list of valid options.

    :param menu_choice: int: The option selected by the user in the main menu.
    :param validation_option_list: List[int], (optional): A list of valid menu options to validate against. Defaults to [1, 2].

    :return:
        bool: True if the menu selection is valid (i.e., exists in `validation_option_list`) or false otherwise
    """

    return menu_choice in validation_option_list


def handle_main_menu_selection(menu_choice: int) -> None:
    """
    Handles the user's selection from the main menu and triggers the corresponding action.

    :param menu_choice: int: The user's selected option from the main menu.

    :return: None

    :raises ValueError: If the user input is not a valid option (1 or 2).
    """

    if 1 == menu_choice:
        print("\n***** Gear Down Switch Activated... *****")
        set_gear_down_status(global_state, 1)    # Activating gear down switch. Setting Gear down status to 1
        handle_menu_after_gear_down_switch_is_activated()
    elif 2 == menu_choice:
        exit_system()
    else:
        raise ValueError("Invalid selection. Please choose a valid option (1 or 2)")


def exit_system() -> None:
    """
    Exits the system gracefully by a message and exits the program.
    After printing the exit message, the program waits for 2 seconds before exiting

    :return: None
    """

    print("\nExiting System...")
    time.sleep(2)  # Pause for 2 seconds before exiting
    exit()  # Terminate the program

def handle_menu_after_gear_down_switch_is_activated() -> None:
    """
    Handles the user interaction after the gear down switch is activated by displaying a menu, accepting a valid selection, and executing the corresponding action.

    The function continues to loop until a valid option is selected, including options to monitor landing gear, view the box log, deactivate the gear down switch, or exit the system.

    :return: None

    :raises ValueError: If the user input is not a valid option (1 or 2).
    :raises Exception: If an unexpected error occurs during the menu handling process.
    """
    try:
        display_menu(MENU_TYPE_CONSTANTS["menuAfterGearDownIsActivated"])
        menu_choice = get_integer_input_from_user()  # Get user selection from the menu

        if not validate_menu_selection_with_validation_option_list(menu_choice, [1,2,3,4]):
            print("\nInvalid selection. Please try again.")
            handle_menu_after_gear_down_switch_is_activated()

        # Switch case for the handling the menu
        if 1 == menu_choice:
            # TODO: process landing gear and alignment logics
            print("\n***** Monitoring landing gear and alignment... *****")
            time.sleep(0.6)
            handle_monitor_landing_gear_and_alignment_process()

        elif 2 == menu_choice:
            # TODO: display stored black box log
            print("\n***** Viewing Black Box Log *****")
            print("User input values are: \n", global_state)
            print(f"Black box log: \n {get_black_box_log()}")
            time.sleep(1)
            handle_monitor_landing_gear_and_alignment_process()
        elif 3 == menu_choice:
            deactivate_gear_down_switch()
        elif 4 == menu_choice:
            exit_system()
        else:
            print("\nInvalid selection. Please try again.")
            handle_menu_after_gear_down_switch_is_activated()
    except ValueError:
        print("\nInvalid selection. Please try again.")
        handle_menu_after_gear_down_switch_is_activated()
    except Exception as e:
        print("\n", e)
        handle_menu_after_gear_down_switch_is_activated()


def deactivate_gear_down_switch() -> None:
    """
    Deactivates the gear down switch, prints confirmation messages, and returns to the main menu.

    This function simulates the deactivation process by printing status messages with a delay to
    mimic the real-world deactivation time.

    After the deactivation is complete, the function redirects the user back to the main menu.

    :return: None

    :raises Exception: If any unexpected error occurs during the deactivation process.
    """
    print("\n Deactivating gear down switch...")
    time.sleep(1)
    set_gear_down_status(global_state, 0)
    print("\n Gear down switch successfully deactivated")
    main()

def handle_monitor_landing_gear_and_alignment_process() -> None:
    """
    Handles the user interaction for monitoring landing gear and alignment processes.

    This function presents a menu to the user to perform various operations such as:
    - Check Gear Positions and Alignment.
    - Calculate and Display the lift of aircraft.
    - <- Go back
    - Deactivate the gear down switch
    - Exit System.

    Based on the user's menu selection, it processes the appropriate actions and continues
    the menu flow or handles errors when invalid input is provided.

    :returns:
        None: The function performs actions based on the user's input and either
              displays results or redirects to other processes.

    :raises ValueError: Raised when the user's menu selection is invalid.
    :raises Exception: Catches any other unexpected errors during the process.
    """
    try:
        display_menu(MENU_TYPE_CONSTANTS["monitorLandingGearAndAlignmentMenu"])
        menu_choice = get_integer_input_from_user()

        # Validate menu selection
        if not validate_menu_selection_with_validation_option_list(menu_choice, [1,2,3,4,5]):
            print("\nInvalid selection. Please try again.")
            handle_monitor_landing_gear_and_alignment_process()

        #Switch case to handle the menu
        if 1 == menu_choice:
            print("\n***** Checking Gear Positions and Alignments... *****")
            process_gear_positions_and_alignments()
        elif 2 == menu_choice:
            print("\n***** Calculating lift of aircraft... *****")
            set_nose_gear_down_status(global_state, None)
            set_left_main_gear_down_status(global_state, None)
            set_right_main_gear_down_status(global_state, None)
            set_alignment_angle(global_state, None)
            set_green_led_status(global_state, None)
            set_red_led_status(global_state, None)
            calculated_lift_value = calculate_lift_of_aircraft()
            print(f"\n***The lift of aircraft is {calculated_lift_value:.2f} Newtons ***")
            handle_monitor_landing_gear_and_alignment_process()
        elif 3 == menu_choice:
            print("\n***** Going back... *****")
            handle_menu_after_gear_down_switch_is_activated()
        elif 4 == menu_choice:
            deactivate_gear_down_switch()
        elif 5 == menu_choice:
            exit_system()

    except ValueError:
        print("\nInvalid selection. Please try again.")
        handle_monitor_landing_gear_and_alignment_process()
    except Exception as e:
        print("\n", e)
        handle_monitor_landing_gear_and_alignment_process()

def process_gear_positions_and_alignments():
    """
    Processes the gear positions and alignment of the aircraft by interacting with the user
    and performing the necessary calculations.

    The function follows these steps:
    1. Retrieves the user's inputs for the gear positions and alignment and stores the values
       in the global state.
    2. Performs calculations on the gear positions and alignment status based on the input values.

    This function integrates gear and alignment handling by managing user input and triggering
    necessary computations.

    :returns:
        None: This function does not return any value but updates the global state and performs
              alignment and gear position calculations.
    """
    get_user_inputs_for_gear_positions_and_alignments_calculations_and_set_in_global_state()
    perform_gear_positions_and_alignments_calculations()
    return

def get_user_inputs_for_gear_positions_and_alignments_calculations_and_set_in_global_state():
    """
    Prompts the user to input gear positions and alignment angle, validates the inputs,
    and updates the global state with these values.

    The function ensures the user inputs valid gear statuses (1 or 0) and an alignment
    angle between 0 and 90 degrees. If an invalid input is detected, the user is prompted
    to re-enter the value.

    :returns:
        None
    """

    nose_main_gear_down_status = int(input("\n Please enter the nose gear status (1 or 0): "))

    if not (nose_main_gear_down_status in [0,1]):
        print("\nInvalid nose main gear down status. Please try again.")
        get_user_inputs_for_gear_positions_and_alignments_calculations_and_set_in_global_state()

    left_main_gear_down_status = int(input("\n Please enter the left main gear status (1 or 0): "))

    if not (left_main_gear_down_status in [0,1]):
        print("\nInvalid left main gear down status. Please try again.")
        get_user_inputs_for_gear_positions_and_alignments_calculations_and_set_in_global_state()

    right_main_gear_down_status = int(input("\n Please enter the right main gear status (1 or 0): "))

    if not (right_main_gear_down_status in [0,1]):
        print("\nInvalid right main gear down status. Please try again.")
        get_user_inputs_for_gear_positions_and_alignments_calculations_and_set_in_global_state()

    alignment_angle = int(input("\n Please enter the alignment angle from 0 to 90 degrees: "))

    if not(0 <= alignment_angle <= 90):
        print("\nInvalid alignment status. Please try again.")
        get_user_inputs_for_gear_positions_and_alignments_calculations_and_set_in_global_state()

    set_nose_gear_down_status(global_state, nose_main_gear_down_status)
    set_left_main_gear_down_status(global_state, left_main_gear_down_status)
    set_right_main_gear_down_status(global_state, right_main_gear_down_status)
    set_alignment_angle(global_state, alignment_angle)

def perform_gear_positions_and_alignments_calculations():
    """
    Performs calculations to check if the landing gear is correctly deployed and aligned.

    Based on the current state, this function checks if all gear positions are down (1)
    and the alignment angle is zero. If these conditions are met, the green LED is activated,
    otherwise, the red LED is turned on, and the aircraft's lift is calculated.

    :returns:
        None
    """
    gear_down_status = get_gear_down_status(global_state)
    nose_main_gear_down_status = get_nose_gear_down_status(global_state)
    left_main_gear_down_status = get_left_main_gear_down_status(global_state)
    right_main_gear_down_status = get_right_main_gear_down_status(global_state)
    alignment_angle = get_alignment_angle(global_state)

    # Convert the alignment angle from directional sensor to scale 0 to 9
    convert_alignment_angle_into_range_0_to_9(alignment_angle)

    if 1 == gear_down_status:
        if 1 == nose_main_gear_down_status and 1 == left_main_gear_down_status and 1 == right_main_gear_down_status and 0 == alignment_angle:
            print("\n*** Landing gear processing successfull. Green LED is turned on ***")
            print(f"\nDisplaying reports: {get_gear_down_status(global_state)}")

            # Green LED is turned on and Red LED is turned off
            set_green_led_status(global_state, 1)
            set_red_led_status(global_state, 0)

            time.sleep(10)
            handle_monitor_landing_gear_and_alignment_process()
        else:
            print("\n*** Landing gear failure. Red LED is turned on ***")
            print("\n*** Calculating aircraft's lift... ***")

            # Red LED is turned on and Green LED is turned off
            set_red_led_status(global_state, 1)
            set_green_led_status(global_state, 0)

            calculated_lift_value = calculate_lift_of_aircraft()
            print(f"\n The lift of the aircraft is {calculated_lift_value:.2f} Newtons")
            print(f"\nDisplaying failure reports: {get_gear_down_status(global_state)}")
            time.sleep(10)
            handle_monitor_landing_gear_and_alignment_process()
    else:
        print("*** Gear down switch is deactivated ***")
        time.sleep(0.7)
        main()

def convert_alignment_angle_into_range_0_to_9(alignment_angle: int) -> int:
    """
    Converts the alignment angle to a value between 0 and 9 by dividing the angle by 10 and rounding down.

    :param alignment_angle: int: The alignment angle in degrees.

    Returns:
        int: The alignment angle mapped to a range between 0 and 9.
    """
    return math.floor(alignment_angle/10)

def calculate_lift_of_aircraft() -> float:
    """
    Calculates the lift of the aircraft based on user inputs and stores the result in the global state.

    The lift is calculated using the standard lift equation, which takes into account air density,
    velocity, wing area, and the coefficient of lift (based on the angle of attack).
    The calculated lift value is stored in the global state.

    :returns:
        float: The calculated lift value in Newtons.
    """
    get_user_inputs_for_aircraft_lift_calculation_and_set_in_global_state()
    velocity = get_velocity(global_state)
    wing_area = get_wing_area(global_state)
    altitude = get_altitude(global_state)
    angle_of_attack = get_angle_of_attack(global_state)

    # Convert velocity and wing area as per SI unit
    velocity_in_standard_si_unit = convert_unit_knots_to_meter_per_second(velocity)
    wing_area_in_standard_si_unit = convert_unit_square_foot_to_square_meters(wing_area)

    # Get air density as per altitude.
    air_density = get_air_density_according_to_altitude(altitude)

    # Getting coefficient of lift as per the angle of attack selected by user
    coefficient_of_lift = get_coefficient_of_lift_according_to_angle_of_attack(angle_of_attack)

    # Calculate the lift using the lift equation
    calculated_lift = 0.5 * air_density * velocity_in_standard_si_unit**2 * wing_area_in_standard_si_unit * coefficient_of_lift

   # Store the value of lift in the global state dictionary
    global_state["lift"] = calculated_lift

    return calculated_lift

def convert_unit_knots_to_meter_per_second(knots: float) -> float:
    """
    Converts speed from knots to meters per second.

    :param knots: float: Speed in knots.

    :returns:
        float: Speed in meters per second.
    """
    return knots * 0.51444

def convert_unit_square_foot_to_square_meters(wing_area: float) -> float:
    """
    Converts wing area from square feet to square meters.

    :param wing_area: float: Wing area in square feet.

    :returns:
        float: Wing area in square meters.
    """
    return wing_area * 0.092903

def get_user_inputs_for_aircraft_lift_calculation_and_set_in_global_state():
    """
    Prompts the user for altitude, velocity, wing area, and angle of attack to calculate the lift.

    The inputs are validated and stored in the global state. If the user provides an invalid angle
    of attack, they are prompted to re-enter the value.

    :returns:
        None
    """
    altitude = float(input("\nPlease enter the altitude in feet: "))
    velocity = float(input("Please enter the velocity in knots: "))
    wing_area = float(input("Please enter the wing area in square feet: "))
    angle_of_attack = int(input("Please select the angle of attack (0, 6, 8, 10, 12): "))

    if not angle_of_attack in [0, 6, 8, 10, 12]:
        print("\nInvalid angle. Please try again.")
        get_user_inputs_for_aircraft_lift_calculation_and_set_in_global_state()

    set_altitude(global_state, altitude)
    set_velocity(global_state, velocity)
    set_wing_area(global_state, wing_area)
    set_angle_of_attack(global_state, angle_of_attack)

def get_coefficient_of_lift_according_to_angle_of_attack(angle_of_attack: int) -> float:
    """
    Retrieves the coefficient of lift based on the selected angle of attack.

    :param angle_of_attack: int: The angle of attack in degrees (typically 0, 6, 8, 10, or 12).

    :returns:
        float: The corresponding coefficient of lift.
    """
    return coefficient_of_lift_as_per_angle_of_attack[angle_of_attack]


def main():
    """
    The main function that handles the program flow by displaying the main menu and
    processing the user's selection.

    It validates the user's input and calls the appropriate functions based on the selection.
    If an invalid selection is made, the user is prompted to try again.

    returns:
        None
    """
    try:
        print("\n-***- WELCOME TO AIRCRAFT MONITORING SYSTEM -***-\n")
        display_menu(MENU_TYPE_CONSTANTS["mainMenu"])  # Display main menu message
        main_menu_user_selection = get_integer_input_from_user()  # Get user selection from main menu

        # Validate main menu selection
        if not validate_menu_selection_with_validation_option_list(main_menu_user_selection, [1,2]):
            print("Invalid selection. Please try again.")
            main()

        # Handling main menu selection
        handle_main_menu_selection(main_menu_user_selection)

        return
    except Exception as e:
        print(e)


if __name__ == "__main__":
    """
    Entry point of the program. This block ensures that the main() function is called 
    when the script is executed directly, but not when it is imported as a module.
    """
    main()
