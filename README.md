# README.md

## Introduction
This project is a Python-based solution developed for an assignment in the "Introduction to Information Technology" course at the University of Canberra. The primary objective of this assignment was to design and implement a software application that adheres to specified business rules while showcasing problem-solving, coding skills, and understanding of computational principles covered from Week 1 to Week 6.

The project focuses on monitoring an aircraft's landing gear system to ensure proper extension and alignment before landing. It includes three parts:

1. Problem-solving and planning.
2. Implementation using personal coding logic.
3. Implementation using AI-generated code.

## Project Structure
The project folder includes the following components:

### Part 1: Problem-Solving Process
This section includes:
- A detailed description of the problem.
- Inputs and outputs.
- Hand-written calculations for logic design and lift calculation.
- Truth tables and Boolean expressions.
- A flowchart and pseudocode outlining the solution.
- Test cases to validate the implementation.

### Part 2: Implementation with Personal Logic
- **Folder:** `Part 2 (coding)`
- **Description:** Contains Python code developed entirely by me, following the problem-solving process. This code includes:
  - Proper state management.
  - Conversion of analog to digital signals.
  - Logging of system states (black box) using a structured dictionary.
  - Handling of unit conversions and error management.
  - Function-based modular programming with comprehensive comments and docstrings.

### Part 3: Implementation with AI-Generated Code
- **Folder:** `Part 3 (AI-GEN coding)`
- **Description:** Contains Python code generated using an AI platform (ChatGPT). The AI-generated code addresses the problem with simpler logic and focuses on immediate outputs but lacks advanced features such as error handling and state management.

## Key Features
- **Aircraft Gear Monitoring:** Ensures all landing gears are extended and aligned before landing. Displays a green LED if all conditions are met or a red LED otherwise.
- **Aircraft Lift Calculation:** Computes the lift force based on parameters such as velocity, air density, wing area, and angle of attack in cases of gear failure.
- **Black Box Logging:** Logs all relevant aircraft data (gear statuses, alignment angle, LED statuses, lift values) in a binary format for safety and integrity.
- **User Interaction:** Provides a text-based menu for pilots to interact with the system.

## Business Rules
1. The gear-down switch activates the monitoring system.
2. A green LED is displayed if all gears are extended and aligned correctly.
3. A red LED is displayed if any gear fails or misaligns.
4. Signals remain active for 10 seconds after activation.
5. In case of failure, the lift is calculated and presented to the pilot.

## Comparison: Personal Code vs AI-Generated Code
| Feature                     | Personal Code             | AI-Generated Code         |
|----------------------------|--------------------------|---------------------------|
| **Complexity**             | Includes advanced features like error handling, state management, and unit conversion. | Focuses on immediate problem-solving with simpler logic. |
| **Efficiency**             | Slightly slower due to detailed logging and state tracking. | Faster execution but lacks robustness. |
| **Alignment with Requirements** | Fully adheres to assignment requirements. | Partially meets the requirements. |
| **Documentation**          | Detailed comments and docstrings for all functions. | Minimal documentation. |

## Running the Project
### Prerequisites
- Python greater than (>) 3.7 installed on your system. (I use Python version 3.12)
- A text editor or IDE (e.g., VSCode, PyCharm).

### Steps to Execute
1. Navigate to the respective folder (`Part 2 (coding)` or `Part 3 (AI-GEN coding)`).
2. Run the Python script:
   ```bash
   python <script_name>.py
   
`For both the <script_name>.py is main.py`
   
3. Follow the on-screen menu to interact with the system.
  
## Acknowledgement
  This project was completed as part of the "Introduction to Information Technology" course. Special thanks to the course instructors and the AI tools utilized for code generation.

`Note: For any further inquiries or clarifications, please contact the developer at aayushbasnet07@gmail.com or open issues.`
