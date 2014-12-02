Modeling a Performance-tracking Quiz App Within a School
========================================================

Models
------

### Person
- Person ID (primary key)
- First Name
- Last Name
- Username
- Password

#### Optional Fields
- Any other biographical data desired.

`Person` will keep a record for all people associated with our app. The following three classes will all extend information about this person, distinguishing them as Principals, Teachers` and `Students`. The `Person`'s username and credentials are stored here and used for logging in.

### Principal
- Principal ID (primary key)
- Person ID (foreign key)

#### Optional Fields
- Date Active
- Date Inactive

Each row in `Principal` will designate the person associated with person_id as the school's principal. Keeping this separate from the `Teacher` table (instead of having a Faculty table with different types, for instance) ensures that this model will be robust should it be the case that a person can be both a principal and a teacher. Or, if there's a possibility that more than one person has `Principal`designation. If neither is a possibility, then one Faculty table could work.

### Teacher
- Teacher ID (primary key)
- Person ID (foreign key)

#### Optional Fields
- Date Active
- Date Inactive

A row in this table designates the person as a teacher.

### Student
- Student ID (primary key)
- Person ID (foreign key)
- Grade

#### Optional Fields
- Date Started
- Date Finished

A row in this table designates the person as a student.

### Class
- Class ID (primary key)
- Name

#### Optional Fields
- Maximum Students
- Subject

One row each for each class. This modeling assumes that the same class (say, "Algebra 1") can have several `Class Sections`. `Quizzes` will belong to `Classes`, not `Class Sections`. Therefore, if multiple `Teachers` teach different `Class Sections` of the same `Class` they can share quizzes. 

### Class Sections
- Class Section ID (primary key)
- Class ID (foreign key)
- Teacher ID (foreign key)
- Period (or Start Time)

This class represents an instance of a `Class`, being taught by a particular `Teacher` at a particular class Period.

### Student Class Section
- Student Class Section ID (primary key)
- Student ID (foreign key)
- Class Section ID (foreign key)

This model ties a particular `Student` to a `Class Section`. In Django, this is defined as a Many to Many relationship and does not require an additional model.

### Quiz
- Quiz ID (primary key)
- Class ID (foreign key)
- Person ID (foreign key)

Each row of this table represents a Quiz which is offered to those taking its associated `Class`. (If a certain quiz could be given to multiple classes, then that would require another model, something like "Quiz Class"). `Person` ID would keep track of who created the quiz.

### Quiz Question
- Quiz Question ID (primary key)
- Quiz ID (foreign key)
- Sequence Number
- Question
- Correct Quiz Question Response ID (foreign key)

This connects `Quiz Questions` to a Quiz. The idea is to make `Quizzes` as flexible as possible with regard to number of questions, and number of possible responses. The part of the app that deals with `Quiz` creation and editing would allow for re-ordering the Sequence Numbers.

### Quiz Question Response
- Quiz Question Response ID (primary key)
- Quiz Question ID (foreign key)
- Response

Each `Quiz Question Response` will be displayed as possible answers to the `Quiz Question` to which it is related. The correct answer is the one contained in the `Quiz Question`'s Correct Quiz Question Response ID. Responses can be displayed in random order, to keep the kids on their toes.

### Student Quiz
- Student Quiz ID (primary key)
- Student ID (foreign key)
- Quiz ID (foreign key)
- Date Submitted

This model represents a submitted quiz by a student. It can be queried simply to find out how many quizzes a student has completed, and also keeps a record of when the student submitted the quiz.

### Student Quiz Question Response
- Student Quiz Question Response ID (primary key)
- Student ID (foreign key)
- Quiz Question ID (foreign key)
- Quiz Question Response ID (foreign key)

This is about the end goal of this modeling. When a student submits answer(s) to a quiz, for each question in the quiz, there will be a new instance of this class made. To evaluate a certain quiz taken by a certain student, the database would be queried to show all of these, where the sought Quiz's ID corresponds to the Quiz ID of the Quiz Question ID.

Fulfillment of Broad Requirements
---------------------------------
### Allow students to take quizzes

Quizzes and their corresponding questions are stored, linked to the class they are being used in. When a Student logs on, Class Sections will be queried to find instances where the Student is associated. Quizzes will then be queried based on that Class Section's Class. These quizzes can then be displayed to the student.

### A student can submit a response to any of the quizzes, which can then be viewed by that student's teachers.
If a Teacher logs in, they can be shown a live feed of quizzes being submitted

they can be shown a menu of Students who are associated in the Class Section instances in which they are the designated Teacher. To choose a student from this menu would then query the model for Quizzes for that Class Section's Class, and then Quiz Questions based on those Quizzes and then Quiz Question Responses linked to that Quiz Question that are related to that Student.

### A principal can see a list of all the teachers within their school who are using the app.
A logged-in principal can be given access to two pieces of data to find out which teachers are using the app. 1) They can be shown data pertaining to Quizzes, in particular the Persons who are creating quizzes. More importantly, 2) They can be shown data chronicling which Teachers lead the Class Sections that have Students that are associated with submitted Student Quizzes.

Questions to Help Development
-----------------------------
The biggest question I had was a basic structural question: Is a quiz defined as having just one question, or can it be a battery of questions. I decided to build it more extensibly as the former. If the latter is desired, that simplifies development by removing the need for the Quiz model, being basically a header for QuizQuestions.

Can a student retake a quiz? With the current structure, any retakes could overwrite previous attempts. Building a History of attempts would allow Teaehers to monitor progress more closely and could be desired.

Can a Principal also be a Teacher?
