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

### Example Usage
1. **Adding a Patient**
   - Choose "1. Add a new patient".
   - Enter the patient’s name, age, and Armenian phone number.
   
2. **Adding a Doctor**
   - Choose "2. Add a new doctor".
   - Enter the doctor's name, age, specialization, and contact info.
   
3. **Adding a Procedure**
   - Choose "4. Add a new procedure".
   - Specify the type (Surgery or Consultation), price, and duration if it’s a Surgery.
   
4. **Scheduling an Appointment**
   - Choose "6. Choose a procedure for a patient".
   - Enter the patient ID and select the procedure ID from the list to schedule.

### Exit
Select "8. Exit" to quit the system.

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
