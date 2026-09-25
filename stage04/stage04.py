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
        """Initialisation of Patient Class."""
        # Attributes: patientID, name, phone, email
        self.patientID = patientID
        self.name = name
        self.phone = phone
        self.email = email
        self.history = [] # appointment history IDs and booking logs

    def getHistory(self):
        return self.history

    def updateContact(self, phone=None, email=None):
        # IF phone or email exist, set both to the new phone and email.
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
        """Initialisation of Practitioner Class."""
        # Attributes: practitionerID, name, specialty, availability
        self.practitionerID = practitionerID
        self.name = name
        self.specialty = specialty
        self.availability = [] # work date-times or work slots for practitioner

    def checkAvailability(self, requested_time):
        return requested_time in self.availability

    def addAvailability(self, slot):
        # If the slot is not taken up, the slot will be added to the availability
        if slot not in self.availability:
            self.availability.append(slot)
    
    def removeAvailability(self, slot):
        # If the slot is taken up, the slot will be removed to the availability
        if slot in self.availability:
            self.availability.remove(slot)

# APPOINTMENT Class
class Appointment:
    """Represents a confirmed time slot on the calendar."""

    def __init__(self, appointmentID:str, startTime, endTime, notes=""):
        """Initialisation of Appointment Class."""
        # Attributes: appointmentID, startTime, endTime, status, notes
        self.appointmentID = appointmentID
        self.startTime = startTime
        self.endTime = endTime
        self.status = AppointmentStatus.SCHEDULED
        self.notes = notes
        self.history = [] # appointment history information
        self.history.append(f"{datetime.now()}: Appointment created.")
    
    def updateStatus(self, new_status: AppointmentStatus):
        # setting new status and adding it to the history log
        self.status = new_status
        self.history.append(f"{datetime.now()}: Status updated to {new_status.value}")

    def addClinicalNotes(self, new_notes:str):
        # adding clinical notes and adding it to the history log
        self.note += f"\n{new_notes}"
        self.history.append(f"{datetime.now()}: Clinical notes added.")

    def getHistoryLog(self):
        return self.history
    
# BOOKING Class
class Booking:
    """Represents booking requests made in the SmartCare System"""
    
    def __init__(self, patientID:str, requestDate, source:str):
        """Initialisation of Booking Class."""
        # Attributes: patientID, requestDate, source, status
        self.patientID = patientID
        self.requestDate = requestDate
        self.source = source
        self.status = BookingStatus.REQUESTED
        self.log = []
        self.log.append(f"{datetime.now()}: Booking created.")

    def checkforDupes(self, existing_bookings):
        """Checking if other bookings exist with the same patient and date."""
        # if the booking has the same patient ID and booking request date, there has been a duplicate.
        for booking in existing_bookings:
            if booking.patientID == self.patientID and booking.requestDate == self.requestDate:
                return True
        # ...else, there are no dupliccates.
        return False
    
    def confirmToAppt(self):
        """Confirming booking status to the an appointment."""
        # setting the status of the booking to confirmed and adding to the log
        self.status = BookingStatus.CONFIRMED
        self.log.append(f"{datetime.now()}: Booking confirmed")

    def cancelRequest(self):
        """Cancelling booking request."""
        # setting the status of the booking to cancelled and adding to the log
        self.status = BookingStatus.CANCELLED
        self.log.append(f"{datetime.now()}: Booking cancelled")

    def getBookingLog(self):
        """Getting booking log history."""
        return self.log
    