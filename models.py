from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Principal(models.Model):
	person = models.ForeignKey(Person)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Teacher(models.Model):
	person = models.ForeignKey(Person)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
	person = models.ForeignKey(Person)
	grade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Class(models.Model):
	name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ClassSection(models.Model):
	class_model = models.ForeignKey(Class)
	teacher = models.ForeignKey(Teacher)
	class_period = models.IntegerField()
	students = models.ManyToManyField(Student)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Quiz(models.Model):
	class_model = models.ForeignKey(Class)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# answer blank=True so that QuizQuestion can be created,
# providing a QuizQuestionID for a QuizQuestionResponse.
class QuizQuestion(models.Model):
	quiz = models.ForeignKey(Quiz)
	sequence_number = models.IntegerField()
	question = models.CharField(max_length=500)
	answer = models.ForeignKey('QuizQuestionResponse', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class QuizQuestionResponse(models.Model):
	quiz_question = models.ForeignKey(QuizQuestion)
	response = models.CharField(max_length=500)
	students = models.ManyToManyField(Student, through='StudentQuiz')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class StudentQuiz(models.Model):
	student = models.ForeignKey(Student)
	quiz_question_response = models.ForeignKey(QuizQuestionResponse)
	date_submitted = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)