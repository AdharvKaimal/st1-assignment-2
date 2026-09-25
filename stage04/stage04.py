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

    def __init__(self, patientID:str, name:str, phone:str, email:str) -> None:
        """Initialisation of Patient Class."""
        # Attributes: patientID, name, phone, email
        self.patientID = patientID
        self.name = name
        self.phone = phone
        self.email = email
        self.history = [] # appointment history IDs and booking logs

    def getHistory(self) -> list[str]:
        """Returns the patient history log."""
        return self.history

    def updateContact(self, phone=None, email=None) -> None:
        """Updates the phone and email of the patient."""
        # IF phone or email exist, set both to the new phone and email.
        if phone:
            self.phone = phone
        if email:
            self.email = email
    
    def getUniqueID(self) -> str:
        """Returns the Patient's unique ID."""
        return self.patientID

# PRACTITIONER Class
class Practitioner:
    """Represents a clinician member who sees patients."""

    def __init__(self, practitionerID:str, name:str, specialty:str) -> None:
        """Initialisation of Practitioner Class."""
        # Attributes: practitionerID, name, specialty, availability
        self.practitionerID = practitionerID
        self.name = name
        self.specialty = specialty
        self.availability = [] # work date-times or work slots for practitioner

    def checkAvailability(self, requested_time) -> bool:
        """Checks the practitioner availability for the given requested time."""
        return requested_time in self.availability

    def addAvailability(self, slot) -> None:
        """Adds an available time to the practitioner's list of available times."""
        # If the slot is not taken up, the slot will be added to the availability
        if slot not in self.availability:
            self.availability.append(slot)
    
    def removeAvailability(self, slot) -> None:
        """Removes an available time from the list of the practitioner's available times."""
        # If the slot is taken up, the slot will be removed to the availability
        if slot in self.availability:
            self.availability.remove(slot)

# APPOINTMENT Class
class Appointment:
    """Represents a confirmed time slot on the calendar."""

    def __init__(self, appointmentID:str, startTime, endTime, notes="") -> None:
        """Initialisation of Appointment Class."""
        # Attributes: appointmentID, startTime, endTime, status, notes
        self.appointmentID = appointmentID
        self.startTime = startTime
        self.endTime = endTime
        self.status = AppointmentStatus.SCHEDULED
        self.notes = notes
        self.history = [] # appointment history information
        self.history.append(f"{datetime.now()}: Appointment created.")
    
    def updateStatus(self, new_status: AppointmentStatus) -> None:
        """Updates the status of the appointment and appends history to the log."""
        # setting new status and adding it to the history log
        self.status = new_status
        self.history.append(f"{datetime.now()}: Status updated to {new_status.value}")

    def addClinicalNotes(self, new_notes:str) -> None:
        """Adds clinical notes to the list of appointment notes and appends history to the log."""
        # adding clinical notes and adding it to the history log
        self.notes += f"\n{new_notes}"
        self.history.append(f"{datetime.now()}: Clinical notes added.")

    def getHistoryLog(self) -> list[str]:
        """Returns the appointment history log."""
        return self.history
    
# BOOKING Class
class Booking:
    """Represents booking requests made in the SmartCare System"""
    
    def __init__(self, patientID:str, requestDate, source:str) -> None:
        """Initialisation of Booking Class."""
        # Attributes: patientID, requestDate, source, status
        self.patientID = patientID
        self.requestDate = requestDate
        self.source = source
        self.status = BookingStatus.REQUESTED
        self.log = []
        self.log.append(f"{datetime.now()}: Booking created.")

    def checkforDupes(self, existing_bookings) -> bool:
        """Checking if other bookings exist with the same patient and date."""
        # if the booking has the same patient ID and booking request date, there has been a duplicate.
        for booking in existing_bookings:
            if booking.patientID == self.patientID and booking.requestDate == self.requestDate:
                return True
        # ...else, there are no dupliccates.
        return False
    
    def confirmToAppt(self) -> None:
        """Confirming booking status to the an appointment."""
        # setting the status of the booking to confirmed and adding to the log
        self.status = BookingStatus.CONFIRMED
        self.log.append(f"{datetime.now()}: Booking confirmed")

    def cancelRequest(self) -> None:
        """Cancelling booking request."""
        # setting the status of the booking to cancelled and adding to the log
        self.status = BookingStatus.CANCELLED
        self.log.append(f"{datetime.now()}: Booking cancelled")

    def getBookingLog(self) -> list[str]:
        """Getting booking log history."""
        return self.log

# Basic Testing for Functionality ==========================================
if __name__ == "__main__":

    # PATIENT CLASS TEST 
    # (checking for accessing ID and updating contact)
    print("\n=== TESTING PATIENT CLASS ===")
    p1 = Patient("P001", "Alice Smith", "0400 123 456", "alice@canberra.com")
    print("Patient ID:", p1.getUniqueID())
    p1.updateContact(phone="0400 999 888")
    print("Updated Phone:", p1.phone)

    # PRACTITIONER CLASS TEST
    # (checking availability for practitioner)
    print("\n=== TESTING PRACTITIONER CLASS ===")
    pr1 = Practitioner("PR001", "Dr. John Kumar", "Physiotherapy")
    slot1 = datetime(2026, 9, 26, 10, 0)
    pr1.addAvailability(slot1)
    print("Availability added:", pr1.availability)
    print("Check availability:", pr1.checkAvailability(slot1))

    # BOOKING CLASS TEST
    # (checking if duplicate bookings can be detected)
    print("\n=== TESTING BOOKING CLASS ===")
    bookings = []
    b1 = Booking("P001", datetime(2026, 9, 27), "Phone")
    bookings.append(b1)

    b2 = Booking("P001", datetime(2026, 9, 27), "Online")
    print("Duplicate booking?", b2.checkforDupes(bookings))

    b1.confirmToAppt()
    print("Booking 1 status:", b1.status)
    print("Booking log:", b1.getBookingLog()) # Printing Booking Log

    # APPOINTMENT CLASS TEST
    # (checking if status can be updated and clinical notes can be added)
    print("\n=== TESTING APPOINTMENT CLASS ===")
    appt1 = Appointment("A001", datetime(2026, 9, 27, 10, 0), datetime(2026, 9, 27, 10, 30))
    appt1.addClinicalNotes("Initial assessment completed.")
    appt1.updateStatus(AppointmentStatus.COMPLETED)

    print("Appointment status:", appt1.status)
    print("Appointment notes:", appt1.notes)
    print("Appointment history:", appt1.getHistoryLog())

    print("\n=== ALL TESTS COMPLETE ===\n")

# ==========================================================================