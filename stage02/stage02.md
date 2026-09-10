STAGE 2 - ASSIGNMENT 2
SMARTCARE v0.2 - Requirements and Specifications

================================================
1. PROBLEM AND SCOPE
-covers Part (A) and Part (B)

Specification: "SmartCare uses spreadsheets and paper records. Staff report duplicate bookings, 
difficulty finding patient information, inconsistent appointment status and limited appointment 
history. Management wants a small, maintainable patient, practitioner and appointment system."

=> Problem Statement: 
SmartCare currently manages patient records, practitioner data and appointment booking using 
paper files and spreadsheets. Since there is no central system,  information has been fragmented 
across multiple documents. This has resulted in inconsistencies between booked appointments, 
difficulty finding patient information, limited appointment history and duplicate bookings. 
The organisation wants a small robust system that can manage patient information, practitioner 
and appointment booking.

=> Scope Statement:
Deliver a small local web-based system that manages the information of patients, practitioners
and appointments. The system should enforce confirmed constraints such as enforcing appointment 
statuses, provide a fast search feature for patient information, provide per-patient 
appointment history and preventing simultaneous double booking per patient. The system will also 
enforce the provisional (assumed and additional) constaints of authenatication protocols for
security and record duplication prevention.


================================================
2. STAKEHOLDERS
-covers Part (B)

STAKEHOLDER (1) - Management (Owners/Leadership)
NEED:       Management is the owner of clinic/practice. They require a small, manageable system
            that can validate appointment statuses, easily find patient information and find
            per-patient appointment history. They need the system to be maintainable and applied
            across their staff and service times.
EVIDENCE:   "Management wants a small, maintainable patient, practitioner and appointment system"
            Management ordered this system to unify these areas into a single workable system.

STAKEHOLDER (2) - Reception/Clerical Staff
NEED:       Reception is part of the staff. They require a system thats able to quickly find the
            patient information based on information provided, verify appointment statuses and
            access appointment history. The system needs to be intuitive and quick enough for
            them to use, and also prevent duplication errors.
EVIDENCE:   "Staff report..."; It is clear that the main users for this system will be the
            clerical and administrative workers of the clinic.

STAKEHOLDER (3) - Practitioners (Clinicians)
NEED:       Practitioners staff, including clinicians, need a system that is conflict-free and
            accurate, in terms of appointment bookings. They need a system that validates and
            updates the information and statuses of the booked appointments. They also need a
            system that will securely handle their information.
EVIDENCE:   "...maintainable patient, practitioner and appointment system."; the practitioners
            and their information and interactions, are also a key part of this system.

STAKEHOLDER (4) - Patients
NEED:       Patients need a system that handle their appointment bookings accurately. The
            system needs to validate the status of their appointments and prevent duplication.
            The system also needs to be secure to handle sensitive patient information, but
            accessible enough for patients to be easily identified.
EVIDENCE:   "...maintainable patient, practitioner and appointment system."; patients are a
            major part of this system since their information is being managed and they are
            the patrons managed by this system.

STAKEHOLDER (5) - System (IT) Administrator
NEED:       A system adminstrator or clinic IT team manages this system. This group needs a
            system that is small, maintainable and secure for operations at the clinic.
EVIDENCE:   "Management wants a small... system"; the system needs to be operationally small
            and usable by the organisation. The assumption can be made that a small IT team
            will administer this system.

================================================
3. FUNCTIONAL REQUIREMENTS
-covers Part(C)

FR-01       Create Patient Record:
            An authorised user shall be able to create a patient record, within the system
            given patient information like name, date of birth, contacts, and additionals.
            The system shall assign a unique identifier (ID) for each patient.

FR-02       Warning for Patient Duplication:
            The system shall provide a warning certain details are similar between patients,
            like surname, DOB, and contacts, to confirm the creation of a new patient record
            and reduce duplication potential.

FR-03       Patient Search:
            An authorised user shall be able to enter patient information, such as patient
            ID, name, DOB, and the system shall filter records or return matching records.
            The search should be completed within a reasonable time-frame (<10 seconds)

FR-04       Patient Record Update:
            An authorised user shall be able to access patient records and manually update
            information within the record. Additionally the system shall allow the record
            to be activated or deactivated.
    
FR-05       Manage Practitioner Records:
            An administrator shall be able to add and edit practitioner records including
            their role, personal details, active/inactive status, and their work hours.

FR-06       Book Appointment:
            An authorised user shall be able to create an appointment booking by selecting
            a patient, practitioner, a date, an appointment time and an appointment
            duration. The system shall check whether all fields are filled and valid.

FR-07       Search Availability:
            An authorised user will be able to quickly search through availability times
            for a given practitioner and a date. The system will only allow appointments
            within the given practitioner's work hours, and exclude existing appointments.

FR-08       Reject Conflicting Appointments:
            The system shall refuse to save appointments that conflict or overlap with
            existing appointment bookings. The system shall display the conflict clearly
            to the authorised user and provide an error message.

FR-09       Appointment Cancellation and Rescheduling:
            The system shall allow an authorised user to reschedule an existing
            appointment booking to another time, given that this does not violate FR-08.
            The system shall also allow the cancellation of appointments. All changes, 
            including cancellation, shall be logged by the system within the system
            per-patient appointment history.

FR-10       Log and Display Appointment History
            For any patient and any appointment, the system shall display an entire
            history of all appointments, showing information including date, time,
            patient, practitioner, and status.


================================================
4. NON-FUNCTIONAL REQUIREMENTS
-covers Part(D)

NFR-01      Reliability and Availability:
            The system shall be operational for all operating hours of the clinic
            and must be accessible even outside this time. Automated backups shall
            be made at the end of every operational day to ensure data is secure.

NFR-02      Performance:
            The system shall provide accurate available search information for
            nearly all (at least >90%) searches during operation. This includes
            patient searches, appointment history searches, 

NFR-03      Maintenance:
            The system shall provide relevant documentation to the clinc and users
            such that it can be maintained within the organisation. The system
            shall be small within scope to help with ease of maintenance.

NFR-04      Data Integrity and Security:
            All appointments shall reference at least one patient, one practitioner
            and one time frame. No appointments shall overlap or duplicate within
            given time frames. The system shall require an authorised user
            (system administrator, management or reception staff) to access the
            modify information within it.

NFR-05      Testability:
            All functional requirements shall be able to locally run integrated
            unit tests, within the system, to ensure that the system is processing
            and managing information correctly. These integrated tests must be able
            to run within a reasonable timeframe and occassionally (weekly) to
            ensure system integrity.

================================================
5. USER STORIES
-covers Part(E)

================================================
6. ACCEPTANCE CRITERIA
-covers Part (E)

================================================
7. ASSUMPTIONS AND OPEN QUESTIONS
-covers Part (F)

================================================
8. AI REQUIREMENTS REVIEW RECORD
-covers Part(F)