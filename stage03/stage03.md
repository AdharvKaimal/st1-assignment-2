STAGE 2 - ASSIGNMENT 2  
SMARTCARE v0.3 - SMARTCARE DOMAIN MODELLING  

================================================  
=> 1. REQUIREMENTS REVIEW  
 - Note: assuming that SmartCare V.02 refers to Stage02 SmartCare Client Statement
   and the main planning requirements/brainstorming developed in the previous stages.  
 - This has been done according to the provided table in
   "Stage_3_SmartCare_v03_Domain_Model_Workbook.docx" file.  
 - State/Behaviour will document potential functions used in a python program solution.
  
| Requirement | Concept | State/Behaviour | Decision |
|:-----|:------:|:------:|:------|
| Staff Reporting Duplicate Bookings | BOOKING | checkForDupes(), confirmToAppointment() | There will be a class "BOOKING" and class "APPOINTMENT" to validate and manage booking statuses and slots |
| Difficulty Finding Patient Information | PATIENT | getUniqueID(), search(criteria), getHistory()| There will be a class "PATIENT" that manages all patient data and records. This includes the ability for front-desk or other clinicans to search this information |
| Inconsistent Appointment Statuses | APPOINTMENT | updateStatus(newStatus), getStatus() | Class "APPOINTMENT" will manage the statuses in booked slots, including statuses such as "active", "inactive", "cancelled" or "postponed" |
| Limited Appointment History | BOOKING and APPOINTMENT | getBookingLog(), getHistoryLog() | Class "BOOKING" will manage a permanent history of all bookings made. Whereas Class "APPOINTMENT" manages the booked slots themselves and the related history. |
| Small Maintainable System | All main classes | All main functions | Additional systems, like managing numerous clinics, and additional classes must be minimised into the minimum necessary for a small-scope system. |
| Practitioner Scheduling and Appointment System | APPOINTMENT | checkAvailability(), addAvailability() | Part of class "PRACTITIONER", the practitioner needs to be included in the systme to manage their own availability
and the working hours for bookings and appointments. |
   
================================================  
=> 2. CANDIDATE CLASSES  
  
Considering the candidates from the providided table:  
| Candidate | Class? | Reason |
|:-----|:------:|:------|
| Patient | Yes | Core part of the system; and essential for tracking patient history and information. |   
| Practitioner | Yes | Core part of the system; essential for tracking practitioner credentials and availability times. |   
| Appointment | Yes | Core part of the system; essential for tracking appointments and history. |   
| Name | No | This is an attribute, not a class, it can belong to many classes. |   
| Clinic | No | This depends on whether SmartCare has many clinics, however in this case there is only one. |   
| Database | No | This is a technical part, not necessarily a class within the program. |   
| Cancellation | No | This has been refactored into Class "BOOKING" and "APPOINTMENT" to manage statuses as a whole. |   
| Status | No | This is an enumeration and an attribute for classes like "APPOINTMENT" |   
  
Additional classes could include:  
- Class "BOOKING", the class that checks whether a booking is avaiable and connects into class "APPOINTMENT".  
- Class "AVAILABILITY_SLOT" to check, in the class "APPOINTMENT" if a slot is open for class "BOOKING".  
- Class "NOTIFICATION" to set reminders and track appointment slots within the system.
- Class "MEDICAL RECORD" to track specific notes or information related to patients in class "PATIENT".    
  
================================================  
=> 3. CRC CARDS  
  
Class - PATIENT:  
- Responsibility (1) - Storing and maintaining patient information, including information like a unique patient 
  identifier (ID), first name, last name, address, phone number, patient email.  
- Validation (1) = Another possible class "MEDICAL_RECORD" which links to health history for the patient.  
  
- Responsibility (2) - Validating uniqueness and preventing duplication or patient records or profiles.  
- Validation (2) - Another possible class "BOOKING" to retrieve the patient history and compare data.  
  
- Responsibility (3) - Providing search dialogue or criteria to look up patients based on ID, DOB or name.   
- Validation (3) - Another possible class "PRACTITIONER" to assign a carer or "APPOINTMENT" to assign
  or book a specific appointment session.  
  
- Responsibility (4) - Providing the ability to update or modify patient information when changes occur.  
- Validation (4) - A possible class "NOTIFICATION" or "BOOKING" to send and manage appointment reminders.  
  
Class - PRACTITIONER:  
- Responsibility (1) - Storing practitioner credentials, including specialty and contact info.  
- Validation (1) - Class "BOOKING" or "APPOINTMENT" to assign specific appointment times.  
  
- Responsibility (2) - Managing practitioner working schedules, inclduing working hours and days off.  
- Validation (2) - Class "PATIENT" for consulation history and potentially Class "BOOKING".  
   
- Responsibility (3) - Validating time slot availability to prevent the double-booking issue.  
- Validation (3) - Class "APPOINTMENT" to record consultation notes and display availability.  
  
- Responsibility (4) - Updating the status of the practitioner dynamically within the system.  
- Validation (4) - Class "AVAILABILITY_SLOT" to define open times and sync with practitioner work days.  
  
Class - APPOINTMENT:  
  
- Responsibility (1) - Defining a specific time slot for the appointment, including start time, duration
and end time.  
- Validation (1) - Class "PRACTITIONER" to link to the assigned clinician.  
  
- Responsibility (2) - Tracking the current status of the slot; whether it is active, inactive, postponed.  
- Validation (2) - Class "BOOKING" to confirm that the slot has been requested.  
  
- Responsibility (3) - Maintaining the history of past appointments for the specified slot.  
- Validation (3) - Class "MEDICAL RECORD" to attach and save clinical notes and history for patients.
  
- Responsibility (4) - Enforcing or validating consistency in appointment status updates.  
- Validation (4) - Class "NOTIFICATION" to alert the staff (and potentially patient) of status changes.
  
Class - BOOKING:  
  
- Responsibility (1) - Recording the request made by a patient or receptionist for an appointment.  
- Validation (1) - Class "PATIENT" to identify the patient the booking is for.
    
- Responsibility (2) - Checking for duplicate requests, essentially same patient, practitioner and time.  
- Validation (2) - Class "APPOINTMENT" to link a booking to a specific time slot when confirmed.  
  
- Responsibility (3) - Storing additional data related to the booking, including notes, booker, booked date.  
- Validation (3) - Class "PRACTITIONER" to check the capacity and specialty notes before confirming.
  
- Responsibility (4) - Managing status and lifecycle of the booking request made, including statuses like
active, inactive, cancelled, postponed.  
- Validation (4) - Class "AVAILABILITY_SLOT" to ensure that the slot exists and has a valid status.  
  
================================================  
=> 4. UML MODEL  
 - The UML diagram within a free software known as "Draw.io". An image file has been attached within the
   stage03 folder for this UML diagram (open it separately).  
 - The PNG file is: "UML_SmartCare.png"  
  
================================================  
=> 5. AI DESIGN REVIEW  
 - The AI prompt and response has been recorded in a different file: "AI-prompt-response.md"

================================================  
=> 6. AI DESIGN REVIEW: COMPARE AND DECIDE  



================================================  
=> 7. PYTHON SKELETON STRUCTURE FOR CLASSES
 - This structure has been completed in a separate Python file: "skeleton_structure.py"  
