(See Document: "Stage_1_Lab_Student_Handout.docx" for context)

AI-USAGE ACTIVITIES FROM WORKSHOP

PART (C) AI-AS-A-TUTOR ACTIVITY PROMPT OUTPUT (from Copilot)
===================================================
**The short version:**  
Your code prints two hard‑coded appointments, then uses lists, dictionaries, and functions to store and display appointments more flexibly. It works, but it’s very bare‑bones and has some structural limitations.

---

### **1. What the code does**

**Part 1 (task 1):**  
- Prints a welcome message.  
- Stores two appointments in variables.  
- Prints each appointment using f‑strings.  
- Everything is hard‑coded — no reuse, no data structure.

**Part 2 (task1enhanced):**  
- Creates an empty list called `appointments`.  
- Defines a function `book_appointment()` that:
  - Validates the patient name.
  - Creates a dictionary representing an appointment.
  - Appends it to the `appointments` list.
- Defines `display_appointments()` to loop through the list and print each appointment.
- Books two appointments using the function.
- Displays all stored appointments.

In short: **you moved from fixed print statements to a reusable mini‑system that stores appointment data in a list of dictionaries.**

---

### **2. Three limitations**

1. **No prevention of double‑booking**  
   The system doesn’t check whether a practitioner already has an appointment at the same time.

2. **No user input**  
   All appointments are hard‑coded. A real system would accept input from a user or another program.

3. **No persistence**  
   Once the program ends, all appointments disappear because they only exist in memory.

---

### **3. Suggested improvements (without rewriting the whole app)**

- **Add validation rules**  
  Check for empty practitioner names, invalid dates, or time conflicts.

- **Introduce user interaction**  
  Use `input()` to let users enter patient names, practitioners, and times.

- **Add search or filtering**  
  For example, a function to list all appointments for a specific practitioner or date.

- **Add data persistence**  
  Save appointments to a file (JSON, CSV) so they survive after the program closes.

- **Improve error handling**  
  Use `try/except` blocks to catch invalid input or booking conflicts gracefully.

---

### **4. Two questions to test your understanding**

1. Why is a list of dictionaries a better structure for storing multiple appointments than using separate variables like `patient1_name`, `patient2_name`, etc.  
2. What would happen if you called `display_appointments()` before booking any appointments?

Let me know your answers and we’ll build on them.

===================================================

PART (D) AI GENERATED ALTERNATIVE (from Copilot)
===================================================
# A simple in‑memory appointment system (no database, no GUI)

appointments = []   # This list will store all appointment dictionaries

def add_appointment(patient, practitioner, time):
    """Store a single appointment in a list."""
    
    # Basic validation to keep things beginner-friendly
    if not patient or not practitioner or not time:
        print("All fields must be provided.")
        return
    
    appointment = {
        "patient": patient,
        "practitioner": practitioner,
        "time": time
    }
    
    appointments.append(appointment)
    print("Appointment added!")

def show_appointments():
    """Display all stored appointments."""
    if not appointments:
        print("No appointments yet.")
        return
    
    for appt in appointments:
        print(f"{appt['patient']} with {appt['practitioner']} at {appt['time']}")

# Example usage
add_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
add_appointment("Bob Johnson", "Dr. Jane Roe", "2024-07-20 11:30 AM")

show_appointments()

===================================================
