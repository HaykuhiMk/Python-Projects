from abc import ABC, abstractmethod
import re
from datetime import timedelta
from random import choice
from typing import List, Dict, Union
from colorama import init, Fore, Style


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Invalid type for name; expected str.")
        if not name:
            raise ValueError("Name cannot be empty.")
        self._name = name
    
    @property
    def age(self) -> int:
        return self.__age
    
    @age.setter
    def age(self, age: int) -> None:
        if not isinstance(age, int):
            raise TypeError("Invalid type for age; expected int.")
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.__age = age

class Patient(Person):
    id_counter = 0
    
    def __init__(self, name: str, age: int, phone_number: str, medical_history: List[tuple] = None):
        super().__init__(name, age)
        self.id = Patient.id_counter
        Patient.id_counter += 1
        self.phone_number = phone_number
        self.medical_history = medical_history or []
        self.appointments: List[Procedure] = [] 
    
    @property
    def phone_number(self) -> str:
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number: str) -> None:
        if not isinstance(phone_number, str):
            raise TypeError("Invalid type for phone number; expected str.")
        if not self.__is_valid_armenian_phone_number(phone_number):
            raise ValueError("Invalid Armenian phone number format.")
        self.__phone_number = phone_number

    def __is_valid_armenian_phone_number(self, phone_number: str) -> bool:
        pattern = r"^(\+?374|0)(10|11|33|41|43|44|46|47|49|55|77|91|93|94|95|96|98|99)\d{6}$"
        return bool(re.match(pattern, phone_number))
    
    def add_medical_history(self, procedure: "Procedure") -> None:
        """ Adds a record of a procedure to the medical history """
        assert isinstance(procedure, Procedure), "Expected a Procedure instance."
        self.medical_history.append((str(procedure), procedure.price))

    def schedule_appointment(self, procedure: "Procedure") -> None:
        """ Adds an appointment for the patient """
        assert isinstance(procedure, Procedure), "Expected a Procedure instance."
        self.appointments.append(procedure)
        print(f"{Fore.GREEN}Appointment for {procedure} scheduled for {self.name}.{Style.RESET_ALL}")

class Doctor(Person):
    id_counter = 0
    
    def __init__(self, name: str, age: int, specialization: str, contact_info: str):
        super().__init__(name, age)
        self.specialization = specialization
        self.contact_info = contact_info
        self.id = Doctor.id_counter
        Doctor.id_counter += 1
    
    def make_surgery(self, surgery: "Surgery", patient_name: str, medic_name: str) -> None:
        assert isinstance(surgery, Surgery), "Expected a Surgery instance."
        surgery.make_procedure(patient_name, medic_name)

class Nurse(Person):
    id_counter = 0
    
    def __init__(self, name: str, age: int, contact_info: str):
        super().__init__(name, age)
        self.id = Nurse.id_counter
        Nurse.id_counter += 1
        self.contact_info = contact_info
    
    def make_consultation(self, consultation: "Consultation", patient_name: str, medic_name: str) -> None:
        assert isinstance(consultation, Consultation), "Expected a Consultation instance."
        consultation.make_procedure(patient_name, medic_name)

class Procedure(ABC):
    def __init__(self, duration: timedelta, price: float):
        self.duration = duration
        self.price = price

    @abstractmethod
    def make_procedure(self, patient_name: str, medic_name: str) -> None:
        pass

class Surgery(Procedure):
    def __init__(self, duration: timedelta, price: float, s_type: str):
        super().__init__(duration, price)
        self.type = s_type

    def __str__(self) -> str:
        return f"Surgery type: {self.type}, Duration: {self.duration}, Price: {self.price}"

    def make_procedure(self, patient_name: str, medic_name: str) -> None:
        print(f"{Fore.GREEN}Doctor {medic_name} operates on Patient {patient_name}: Duration = {self.duration}, Price = {self.price}, Type = {self.type}{Style.RESET_ALL}")

class Consultation(Procedure):
    def __init__(self, price: float):
        super().__init__(timedelta(minutes=30), price)

    def __str__(self) -> str:
        return f"Consultation Duration: {self.duration}, Price: {self.price}"

    def make_procedure(self, patient_name: str, medic_name: str) -> None:
        print(f"{Fore.GREEN}Nurse {medic_name} consults Patient {patient_name}: Duration = {self.duration}, Price = {self.price}{Style.RESET_ALL}")

class Hospital:
    def __init__(self):
        self.staff: Dict[str, Dict[int, Union[Doctor, Nurse]]] = {"doctors": {}, "nurses": {}}
        self.patients: Dict[int, Patient] = {}
        self.procedures: List[Procedure] = []
    
    def add_doctor(self, doctor: Doctor) -> None:
        assert isinstance(doctor, Doctor), "Expected a Doctor instance."
        self.staff["doctors"][doctor.id] = doctor
    
    def add_nurse(self, nurse: Nurse) -> None:
        assert isinstance(nurse, Nurse), "Expected a Nurse instance."
        self.staff["nurses"][nurse.id] = nurse
    
    def add_patient(self, patient: Patient) -> None:
        assert isinstance(patient, Patient), "Expected a Patient instance."
        self.patients[patient.id] = patient
    
    def add_procedure(self, procedure: Procedure) -> None:
        assert isinstance(procedure, Procedure), "Expected a Procedure instance."
        self.procedures.append(procedure)

    def administration(self) -> None:
        print(f"\n{Fore.CYAN}Welcome to the Hospital System!{Style.RESET_ALL}")
        while True:
            print(f"{Fore.CYAN}1.{Style.RESET_ALL} Add a new patient")
            print(f"{Fore.CYAN}2.{Style.RESET_ALL} Add a new doctor")
            print(f"{Fore.CYAN}3.{Style.RESET_ALL} Add a new nurse")
            print(f"{Fore.CYAN}4.{Style.RESET_ALL} Add a new procedure")
            print(f"{Fore.CYAN}5.{Style.RESET_ALL} View all procedures")
            print(f"{Fore.CYAN}6.{Style.RESET_ALL} Choose a procedure for a patient")
            print(f"{Fore.CYAN}7.{Style.RESET_ALL} View patient's medical history")
            print(f"{Fore.CYAN}8.{Style.RESET_ALL} Exit\n")

            usr_choice = input(f"{Fore.CYAN}Please select an option: {Style.RESET_ALL}")

            if usr_choice == "1":
                name = input(f"{Fore.CYAN}Enter patient name: {Style.RESET_ALL}")
                age = int(input(f"{Fore.CYAN}Enter patient age: {Style.RESET_ALL}"))
                phone_number = input(f"{Fore.CYAN}Enter patient phone number: {Style.RESET_ALL}")
                patient = Patient(name, age, phone_number)
                self.add_patient(patient)
                print(f"{Fore.GREEN}Patient {name} added successfully.{Style.RESET_ALL}")

            elif usr_choice == "2":
                name = input(f"{Fore.CYAN}Enter doctor name: {Style.RESET_ALL}")
                age = int(input(f"{Fore.CYAN}Enter doctor age: {Style.RESET_ALL}"))
                specialization = input(f"{Fore.CYAN}Enter doctor's specialization: {Style.RESET_ALL}")
                contact_info = input(f"{Fore.CYAN}Enter doctor's contact info: {Style.RESET_ALL}")
                doctor = Doctor(name, age, specialization, contact_info)
                self.add_doctor(doctor)
                print(f"{Fore.GREEN}Doctor {name} added successfully.{Style.RESET_ALL}")

            elif usr_choice == "3":
                name = input(f"{Fore.CYAN}Enter nurse name: {Style.RESET_ALL}")
                age = int(input(f"{Fore.CYAN}Enter nurse age: {Style.RESET_ALL}"))
                contact_info = input(f"{Fore.CYAN}Enter nurse contact info: {Style.RESET_ALL}")
                nurse = Nurse(name, age, contact_info)
                self.add_nurse(nurse)
                print(f"{Fore.GREEN}Nurse {name} added successfully.{Style.RESET_ALL}")

            elif usr_choice == "4":
                proc_type = input(f"{Fore.CYAN}Enter procedure type (Surgery/Consultation): {Style.RESET_ALL}").lower()
                price = float(input(f"{Fore.CYAN}Enter price: {Style.RESET_ALL}"))
                if proc_type == "surgery":
                    doctor = choice(list(self.staff["doctors"].values()))
                    duration = timedelta(hours=int(input(f"{Fore.CYAN}Enter duration in hours: {Style.RESET_ALL}")))
                    surgery_type = input(f"{Fore.CYAN}Enter surgery type: {Style.RESET_ALL}")
                    surgery = Surgery(duration, price, surgery_type)
                    self.add_procedure(surgery)
                    print(f"{Fore.GREEN}Surgery procedure added.{Style.RESET_ALL}")
                elif proc_type == "consultation":
                    nurse = choice(list(self.staff["nurses"].values()))
                    consultation = Consultation(price)
                    self.add_procedure(consultation)
                    print(f"{Fore.GREEN}Consultation procedure added.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Invalid procedure type.{Style.RESET_ALL}")

            elif usr_choice == "5":
                print(f"{Fore.BLUE}\nAvailable Procedures:{Style.RESET_ALL}")
                for i, proc in enumerate(self.procedures):
                    proc_type = "Surgery" if isinstance(proc, Surgery) else "Consultation"
                    print(f"{Fore.CYAN}{i}. {proc_type} - Price: {proc.price}{Style.RESET_ALL}")

            elif usr_choice == "6":
                patient_id = int(input(f"{Fore.CYAN}Enter patient ID: {Style.RESET_ALL}"))
                if patient_id in self.patients:
                    patient = self.patients[patient_id]
                    print(f"{Fore.CYAN}\nAvailable Procedures:{Style.RESET_ALL}")
                    for i, proc in enumerate(self.procedures):
                        proc_type = "Surgery" if isinstance(proc, Surgery) else "Consultation"
                        print(f"{Fore.CYAN}{i}. {proc_type} - Price: {proc.price}{Style.RESET_ALL}")
                    proc_id = int(input(f"{Fore.CYAN}Choose a procedure ID: {Style.RESET_ALL}"))
                    if proc_id < len(self.procedures):
                        procedure = self.procedures[proc_id]
                        patient.schedule_appointment(procedure)
                    else:
                        print(f"{Fore.RED}Invalid procedure ID.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Patient ID not found.{Style.RESET_ALL}")

            elif usr_choice == "7":
                patient_id = int(input(f"{Fore.CYAN}Enter patient ID: {Style.RESET_ALL}"))
                if patient_id in self.patients:
                    patient = self.patients[patient_id]
                    print(f"{Fore.CYAN}\nMedical History: {Style.RESET_ALL}")
                    for record in patient.medical_history:
                        print(f"{Fore.CYAN}Procedure: {record[0]}, Price: {record[1]}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Patient ID not found.{Style.RESET_ALL}")

            elif usr_choice == "8":
                print(f"{Fore.RED}Exiting the system.{Style.RESET_ALL}")
                break

            else:
                print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

