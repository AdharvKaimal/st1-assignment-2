(See Document: "Stage_1_Lab_Student_Handout.docx" for context)

PART (E) COMPARE AI and HUMAN VERSIONS (table)

*See the "ai_gen_alternative" or "ai_usage" to see the AI-generated
 alternative booking system.

| Question                      | Human version | AI version |
| ----------------------------- | ------------- | ---------- |
| Easy to understand?		    | Yes           | No         |
| Runs successfully?		    | Yes           | Yes        |
| Uses only required features?	| Yes           | Yes        |
| Adds assumptions?		        | No            | Yes (some) |
| Handles errors?		        | Yes (some)    | No         |
| Could I explain it?	        | Yes           | Yes        |

PART(F) VERIFYING BEHAVIOUR

*Tests were implemented for both the human and AI versions.
(See files bottom of python files "smartcare_v01.py and
ai_gen_alternative.py for the unusual input tests)

Though the AI generated alternative script can book a normal
appointment using methods, it does not any checks on factors
like whether a blank patient name has been given. Furthermore
there are no checks for repeating or doubling appointments.
The AI generated alternative also does not check for strange
edge cases where the input does not make sense. Thus, the
human-created version produces a program that respects the
context and also a more testable and reliable system.
