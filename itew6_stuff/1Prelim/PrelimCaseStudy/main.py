class Patient:
    def __init__(self, name, age, symptoms):
        self.name = name
        self.age = age
        self.symptoms = symptoms
        self.vital_signs = {}
        self.diagnosis = ""
        self.treatment_plan = ""

    def record_vital_signs(self, vitals):
        self.vital_signs = vitals

    def assess(self):
        if "fever" in self.symptoms and "cough" in self.symptoms:
            self.diagnosis = "Possible flu"
        elif "headache" in self.symptoms and "dizziness" in self.symptoms:
            self.diagnosis = "Possible migraine"
        else:
            self.diagnosis = "Undiagnosed - Further tests needed"

    def plan_treatment(self):
        if self.diagnosis == "Possible flu":
            self.treatment_plan = "Rest, fluids, and fever medication. Follow-up in 3 days."
        elif self.diagnosis == "Possible migraine":
            self.treatment_plan = "Pain relievers, hydration, and rest. Follow-up if persistent."
        else:
            self.treatment_plan = "Refer to specialist for further diagnosis."

    def display_patient_info(self):
        print(f"Patient Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Symptoms: {', '.join(self.symptoms)}")
        print(f"Vital Signs: {self.vital_signs}")
        print(f"Diagnosis: {self.diagnosis}")
        print(f"Treatment Plan: {self.treatment_plan}")


def main():
    # Input
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    symptoms = input("Enter symptoms (comma-separated): ").split(",")
    
    # Create Patient Object
    patient = Patient(name, age, [sym.strip() for sym in symptoms])
    
    # Record Vital Signs
    temp = float(input("Enter body temperature: "))
    heart_rate = int(input("Enter heart rate: "))
    blood_pressure = input("Enter blood pressure (e.g., 120/80): ")
    patient.record_vital_signs({"Temperature": temp, "Heart Rate": heart_rate, "Blood Pressure": blood_pressure})
    
    # Assessment
    patient.assess()
    
    # Plan Treatment
    patient.plan_treatment()
    
    # Display SOAP Summary
    print("\n--- Patient Summary ---")
    patient.display_patient_info()


if __name__ == "__main__":
    main()
