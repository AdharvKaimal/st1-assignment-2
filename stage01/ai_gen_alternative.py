# (See Document: "Stage_1_Lab_Student_Handout.docx" for context)

# AI-GENERATED-ALTERNATIVE (as per the task)

# A simple in‑memory appointment system (no database, no GUI)

def create_appointment(patient_name, practitioner_name, appointment_time):
    """Return a simple dictionary representing an appointment."""
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    return appointment

# Example usage:
appt = create_appointment("Alice Johnson", "Dr. Smith", "2026-09-05 10:30 AM")
print(appt)

# Unusual Input Testing (tests written by me)
unusual_1 = create_appointment("None", "None", "2026-09-05 10:30 AM") # Test with unusual input "None"
unusual_2 = create_appointment("", "", "2026-09-05 10:30 AM") # Test with empty string

print(unusual_1)
print(unusual_2)