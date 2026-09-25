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

    def __init__(self):
        # Attributes: appointmentID, startTime, endTime, status, notes
        pass

    def update_status(self):
        # Change status, such as "active", "inactive", "cancelled", "postponed"
        pass

    def add_clinical_notes(self):
        # Attach notes from the visit
        pass

    def get_history_log(self):
        # Return history of stats changes
        pass