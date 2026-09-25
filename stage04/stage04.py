from datetime import datetime # to handle dates in booking/appointment
from enum import Enum # to handle status enums

# implementation as per UML created in Stage03, worked from skeleton_structure.py
# changes have been made to accomodate the new UML model

# Handles enumeration for Appointment statuses
class BookingStatus(Enum):
    REQUESTED = "Requested"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"

# Handles enumeration for Appointment statuses
class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

# PATIENT Class
class Patient:
    """Represents a patient in the SmartCare system."""

    def __init__(self, patientID:str, name:str, phone:str, email:str):
        # Attributes: patientID, name, phone, email
        self.patientID = patientID
        self.name = name
        self.phone = phone
        self.email = email
        self.history = [] # appointment history IDs and booking logs

    def getHistory(self):
        return self.history

    def updateContact(self, phone=None, email=None):
        if phone:
            self.phone = phone
        if email:
            self.email = email
    
    def getUniqueID(self):
        return self.patientID

# PRACTITIONER Class
class Practitioner:
    """Represents a clinician member who sees patients."""

    def __init__(self, practitionerID:str, name:str, specialty:str):
        # Attributes: practitionerID, name, specialty, availability
        self.practitionerID = practitionerID
        self.name = name
        self.specialty = specialty
        self.availability = [] # work date-times or work slots for practitioner

    def checkAvailability(self, requested_time):
        return requested_time in self.availability

    def addAvailability(self, slot):
        if slot not in self.availability:
            self.availability.appent(slot)
    
    def removeAvailability(self, slot):
        if slot in self.availability:
            self.availability.remove(slot)

# APPOINTMENT Class
class Appointment:
    """Represents a confirmed time slot on the calendar."""

    def __init__(self, appointmentID:str, startTime, endTime, notes=""):
        # Attributes: appointmentID, startTime, endTime, status, notes
        self.appointmentID = appointmentID
        self.startTime = startTime
        self.endTime = endTime
        self.status = AppointmentStatus.SCHEDULED
        self.notes = notes
        self.history = [] # appointment history information
        self.history.append(f"{datetime.now()}: Appointment created.")
    
    def updateStatus(self, new_status: AppointmentStatus):
        self.status = new_status
        self.history.append(f"{datetime.now()}: Status updated to {new_status.value}")

    def addClinicalNotes(self, new_notes:str):
        self.note += f"\n{new_notes}"
        self.history.append(f"{datetime.now()}: Clinical notes added.")

    def getHistoryLog(self):
        return self.history
    