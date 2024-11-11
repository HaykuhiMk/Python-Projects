# Hospital Management System

This Python program implements a basic hospital management system. It allows hospital staff to manage patient records, doctors, nurses, and procedures. The system includes appointment scheduling, medical history tracking, and basic staff and procedure management.

## Features

1. **Add New Patient**: Registers a new patient with their details and phone number.
2. **Add New Doctor**: Registers a new doctor with their specialization and contact info.
3. **Add New Nurse**: Registers a new nurse with contact information.
4. **Add New Procedure**: Allows users to add new medical procedures (either Surgery or Consultation).
5. **View Procedures**: Displays a list of available procedures.
6. **Schedule Appointment**: Assigns a procedure (like Surgery or Consultation) to a patient.
7. **View Patient Medical History**: Displays the list of completed procedures for a specific patient.

## Requirements

- Python 3.6+
- `colorama` library (for colored console output)

To install the required packages, use:
```bash
pip install colorama
```

## Classes Overview

- **Person**: Base class for all people in the system (patients, doctors, nurses).
- **Patient**: Inherits from `Person`. Contains additional attributes such as `phone_number`, `medical_history`, and `appointments`.
- **Doctor**: Inherits from `Person`. Contains a `specialization` attribute and has methods for performing surgery.
- **Nurse**: Inherits from `Person`. Contains a `contact_info` attribute and a method for consultations.
- **Procedure** (Abstract Base Class): Represents medical procedures with attributes `duration` and `price`.
  - **Surgery**: Inherits from `Procedure`. Has additional attributes for `surgery type` and specific behavior for surgeries.
  - **Consultation**: Inherits from `Procedure`. Represents consultation procedures.
- **Hospital**: Manages the entire system, allowing for adding patients, doctors, nurses, and procedures, scheduling appointments, and displaying patient medical histories.

## How to Run the Program

To start the program, run:
```bash
python hospital_system.py
```

The system presents a command-line interface with numbered options for each action.

Here's an example of usage for each choice option:

---

### Example Usage

1. **Adding a Patient**
   - Choose "1. Add a new patient".
   - Enter the patient’s name (string), age (integer), and Armenian phone number (formatted as +374XXXXXXXX or 0XXXXXXXX).
   - Example:
     ```plaintext
     Enter patient name: John Doe
     Enter patient age: 30
     Enter patient phone number: +37477123456
     ```
   - Output:
     ```plaintext
     Patient John Doe added successfully.
     ```

2. **Adding a Doctor**
   - Choose "2. Add a new doctor".
   - Enter the doctor’s name, age, specialization (e.g., "Cardiologist"), and contact info.
   - Example:
     ```plaintext
     Enter doctor name: Dr. Jane Smith
     Enter doctor age: 45
     Enter doctor's specialization: Cardiologist
     Enter doctor's contact info: janesmith@example.com
     ```
   - Output:
     ```plaintext
     Doctor Dr. Jane Smith added successfully.
     ```

3. **Adding a Nurse**
   - Choose "3. Add a new nurse".
   - Enter the nurse’s name, age, and contact info.
   - Example:
     ```plaintext
     Enter nurse name: Sarah Brown
     Enter nurse age: 32
     Enter nurse contact info: sarahbrown@example.com
     ```
   - Output:
     ```plaintext
     Nurse Sarah Brown added successfully.
     ```

4. **Adding a Procedure**
   - Choose "4. Add a new procedure".
   - Specify the procedure type (either "Surgery" or "Consultation").
   - If it’s a Surgery, also provide the surgery type (e.g., "Appendectomy"), duration (in hours), and price.
   - If it’s a Consultation, provide only the price.
   - Example (for Surgery):
     ```plaintext
     Enter procedure type (Surgery/Consultation): Surgery
     Enter price: 5000
     Enter duration in hours: 3
     Enter surgery type: Appendectomy
     ```
   - Output:
     ```plaintext
     Surgery procedure added.
     ```
   - Example (for Consultation):
     ```plaintext
     Enter procedure type (Surgery/Consultation): Consultation
     Enter price: 200
     ```
   - Output:
     ```plaintext
     Consultation procedure added.
     ```

5. **View All Procedures**
   - Choose "5. View all procedures".
   - The system will list all procedures available, including their type (Surgery or Consultation), price, and any specific details such as duration or surgery type.
   - Output:
     ```plaintext
     Available Procedures:
     0. Surgery - Price: 5000, Type: Appendectomy, Duration: 3:00:00
     1. Consultation - Price: 200, Duration: 0:30:00
     ```

6. **Scheduling an Appointment**
   - Choose "6. Choose a procedure for a patient".
   - Enter the patient ID to associate the procedure with a specific patient.
   - Select the procedure ID from the available list.
   - Example:
     ```plaintext
     Enter patient ID: 0
     Available Procedures:
     0. Surgery - Price: 5000, Type: Appendectomy, Duration: 3:00:00
     1. Consultation - Price: 200, Duration: 0:30:00
     Choose a procedure ID: 1
     ```
   - Output:
     ```plaintext
     Appointment for Consultation Duration: 0:30:00, Price: 200 scheduled for John Doe.
     ```

7. **View Patient's Medical History**
   - Choose "7. View patient's medical history".
   - Enter the patient ID to view the history of procedures they have undergone.
   - Example:
     ```plaintext
     Enter patient ID: 0
     ```
   - Output:
     ```plaintext
     Medical History:
     Procedure: Consultation Duration: 0:30:00, Price: 200
     ```

8. **Exit**
   - Choose "8. Exit" to close the system.
   - Output:
     ```plaintext
     Exiting the system.
     ```
---

## Additional Information

### Phone Number Validation
The program validates Armenian phone numbers based on the format `+374XXXXXXXX` or `0XXXXXXXX`.

### Color Coding
This system uses the `colorama` library to highlight different sections in the console:
- Green: Success messages.
- Red: Errors or exit messages.
- Cyan: Prompt and informational text.

## Future Improvements
- **Data Persistence**: Adding a database to save and load hospital data.
- **Advanced Scheduling**: Supporting multiple appointments and managing appointment dates.
- **Enhanced Procedure Types**: Adding more types and complexity to the procedure classes.

## License
This project is free to use under the MIT License.
