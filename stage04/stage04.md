STAGE 4 - ASSIGNMENT 2  
SMARTCARE v0.4 - IMPLEMENTING THE DOMAIN LAYER  

 - all non-AI implementation has been completed in stage04.py
 - all AI generated responses have been recorded in AI-prompt-response.md

================================================  
=> A. REVISITING APPROVED UML
 - Relevant work has been done in "stage04.py"  
 - Code is being implemented according to UML developed in Stage 03
 - This includes the new BOOKING Class to break down functionality
 - Main classes wil be created for: PATIENT, PRACTITIONER, APPOINTMENT and BOOKING

================================================  
=> B. IMPLEMENTING PATIENT  
 - Relevant work has been done in "stage04.py"  

================================================  
=> C. IMPLEMENTING PRACTITIONER  
 - Relevant work has been done in "stage04.py"  

================================================  
=> D, E, G, H. Gen AI Section, Review, Refactor, Log
 - Relevant work has been done in "stage04.py"  
 - The GenAI prompt for Appointment class been added with "AI-prompt-response.md"  
  
 - CLASS "BOOKING" has also been implemented seperately without AI.  
    
Notes: Copilot used many more libraries features and also implemented enumeration
for the conditions/statuses in appointment. The AIs interpretation of the functions
were limited to the requirements of the prompt, however additional complexity was
introduced that may not be optimal. For example, the AI version of appointment
introduced a number of helper functions as well. This can be further simplified into
regular OOP and classses within Python without additional complexity. The choice
has been made to further simplify the implementation by removing additional
helper functions, minimising library usage, and closely adhering to traditional
simple Python OOP.  

================================================  
=> F. MANUAL BEHAVIOR CHECKS (TESTING)
 - Relevant work has been done in "stage04.py"  
 - Testing has been implemented at the bottom of the script.