STUDENTS
---------
id (PK)
name
email
class_id (FK → classes.id)

TEACHERS
---------
id (PK)
name
email

CLASSES
---------
id (PK)
name
section
class_teacher_id (FK → teachers.id)

SUBJECTS
---------
id (PK)
name

TEACHER_SUBJECTS
----------------
id (PK)
teacher_id (FK → teachers.id)
subject_id (FK → subjects.id)

-------------------------------------

SCHEDULE   (🔥 CORE TABLE)
---------
id (PK)
class_id (FK → classes.id)
subject_id (FK → subjects.id)
teacher_id (FK → teachers.id)
type ('LECTURE' / 'ASSESSMENT')
title
date
start_time
end_time
status

-------------------------------------

ASSESSMENTS
------------
id (PK)
schedule_id (FK → schedule.id)
total_marks
passing_marks
description

ASSESSMENT_ATTEMPTS
--------------------
id (PK)
assessment_id (FK → assessments.id)
student_id (FK → students.id)
score
status (attempted / absent)
submitted_at

-------------------------------------

ATTENDANCE
------------
id (PK)
student_id (FK → students.id)
schedule_id (FK → schedule.id)
status (present / absent)

-------------------------------------

FEES (optional future)
------------
id (PK)
student_id (FK → students.id)
amount
status
date