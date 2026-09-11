STAGE 2 - ASSIGNMENT 2
SMARTCARE v0.2 - Requirements and Specifications

================================================  
=> 1. PROBLEM AND SCOPE  
-covers Part (A) and Part (B)  

Specification: "SmartCare uses spreadsheets and paper records. Staff report duplicate bookings, 
difficulty finding patient information, inconsistent appointment status and limited appointment 
history. Management wants a small, maintainable patient, practitioner and appointment system."

Problem Statement: 
SmartCare currently manages patient records, practitioner data and appointment booking using 
paper files and spreadsheets. Since there is no central system, information has been fragmented 
across multiple documents. This has resulted in inconsistencies between booked appointments, 
difficulty finding patient information, limited appointment history and duplicate bookings. 
The organisation wants a small robust system that can manage patient information, practitioner 
and appointment booking.  

Scope Statement:
Deliver a small local web-based system that manages the information of patients, practitioners
and appointments. The system should enforce confirmed constraints such as enforcing appointment 
statuses, provide a fast search feature for patient information, provide per-patient 
appointment history and preventing simultaneous double booking per patient. The system will also 
enforce the provisional (assumed and additional) constaints of authenatication protocols for
security and record duplication prevention.  


================================================  
=> 2. STAKEHOLDERS  
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
=> 3. FUNCTIONAL REQUIREMENTS  
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
=> 4. NON-FUNCTIONAL REQUIREMENTS  
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
=> 5. USER STORIES  
-covers Part(E)  

US-01       "As a front-end administrator, I want a system that rejects a booking
            that conflicts with an appointment booking that the patient or
            practitioner already has, so that I can stop duplicate bookings are
            not created, resulting in conflicts in patient experience and
            practitioner workflows"

US-02       "As a receptionist, I want a system that will be able to
            quickly search through patients records, given details such as patient
            ID, name, DOB, etc, so that I can pull up correct and accurate records
            of patients quickly" 

US-03       "As a clinician, I want to be able to intuitively access a system where
            it shows me my weekly appointments, the associated details and who I
            am seeing, so that I can prepare for my patients and deliver the best
            health advice and outcomes for them."

US-04       "As a receptionist, I want to be able to quickly view a fixed set of
            statuses regarding appointment bookings, so that I can more easily
            view, manage and report to our patients and to our organisation."

US-05       "As a practitioner, I want to be able to see the full appointment
            history of a patient, including cancelled or changed appointments,
            so that I can understand the healthcare history of my patient more
            accurately."

US-06       "As the manager at SmartCare, I want to be able to manage the data and
            also be confident that our IT team can manage a small system, so that
            I can use the system in a scalable organisational context, and also
            have the redunancy of knowing that the system can be managed locally."


================================================  
=> 6. ACCEPTANCE CRITERIA  
-covers Part (E)  

*US-01, US-02, and US-03 have been chosen to create the acceptance criteria.

US-01:      GIVEN:  a practitioner has an appointment for patient "John Doe" from
                    10:30 AM to 12:30 PM on 15/09/2026 AND the patient record for 
                    "John Doe" exists AND the user is on the appointment booking 
                    screen...
            WHEN:   a user attempts to book an appointment for patient "John Doe"
                    with the same practitioner at the same time...
            THEN:   the system shall reject the appointment and display an error
                    or warning message, informing the user about the conflict.

US-02:      GIVEN:  the system has 1000 patient records AND a patient "Jane Doe"
                    with a DOB of 10/05/1980 AND the screen is on the search
                    page...
            WHEN:   a user attempts to enter the specified information (such as)
                    the parts of the name and DOB AND clicks "search"...
            THEN:   the system shall display a single specific patient record
                    detailing the patient searched OR present a list of closely
                    matching patient records sorted with surname within 10 seconds

US-03:      GIVEN:  a practitioner "Dr Doe" is active on the system AND they have
                    valid working hours AND they have booked appointments...
            WHEN:   "Dr Doe" opens the system AND searches according to weekly or
                    daily view...
            THEN:   the system shall the booking details for each appointment
                    booked within valid working hours AND provide information such
                    as the time frame, the patient name, appointment start time and
                    duration of the appointment.

================================================  
=> 7. ASSUMPTIONS AND OPEN QUESTIONS  
-covers Part (F)  

Assumptions for this system include:  
(1) There are only four main issues, including duplicate bookings, difficulty
    finding patient information, inconsistent appointment status and limited
    appointment history.  
(2) Practitioners are local and internal staff that are authorised to access
    and view the system.  
(3) There are no existing IT systems used by the organisation.  
(4) SmartCare is able to provide staff basic training using the system. This
    is important for adoption of the system.  
(5) The System is limited in scope, designed to primarily be used for a small
    regional number of people and administered by a few authorised personnel.  

Further (Open) Questions:  
(1) What does "maintainable" mean to SmartCare, at what scope must the system
    be maintainable?  
(2) Is there a specific definition for "small system" given specific constraints?  
(3) What are the roles and access levels required for staff at SmartCare?  
(4) Does the system need to integrate with pre-existing systems at the
    organisation? If so which ones?  
(5) Will the organisation provide basic training for staff and personnel in
    using this new system?  

================================================  
=> 8. AI REQUIREMENTS REVIEW RECORD  
-covers Part (F)  

(2) AI Suggestion:  Current System Uses Spreadsheets and Paper Records  
    Evidence?:      Explicitly stated at the start of the client specification.  
    Decision:       A digital system is required to centrally manage information.  
    Reason:         To fix issues such as duplicate appointments, etc.   
    Verification:   Accepted  
  
(2) AI Suggestion:  Duplicate Bookings Occur  
    Evidence?:      Staff report "duplicate bookings" within the specification.  
    Decision:       The system needs to track similar or same booking records.  
    Reason:         The system shall display and warn users of duplications in
                    appointments, which will prevent the duplication errors.  
    Verification:   Accepted  
  
(3) AI Suggestion:  Difficulty Finding Patient Information  
    Evidence?:      Staff report "difficulty finding patient information" in
                    the specification.  
    Decision:       The system shall quickly search through and display patient
                    information.  
    Reason:         This will reduce the time needed for front-desk staff to
                    find patient information.  
    Verification:   Accepted  
  
(4) AI Suggestion:  Inconsistent Appointment Status  
    Evidence?:      Reported in the client specification "inconsistent
                    appointment status"  
    Decision:       The system shall have fixed statuses based on assumed
                    booking appointment states.  
    Reason:         The system can reduce the confusion or misreporting of
                    the status of the appointment bookings.  
    Verification:   Accepted  
  
(5) AI Suggestion:  Limited Appointment History  
    Evidence?:      Reported by staff "limited appointment history".  
    Decision:       The system shall have a system that logs all appointments
                    regardless of status for every patient.  
    Reason:         The system can provide a clear picture of all appointment
                    histories for every patient.  
    Verification:   Accepted  
