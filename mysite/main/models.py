from django.db import models
from datetime import datetime 
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Tutorial(models.Model): 
    tutorial_title=models.CharField(max_length=200)
    tutorial_content=models.TextField()
    tutorial_published=models.DateTimeField("data published", default=datetime.now())

    def __str__(self):
        return self.tutorial_title



class School(models.Model):
    #fields 
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)

    def __str__(self):
    	return self.name

class Department(models.Model):
	name=models.CharField(max_length=30)
	school=models.ManyToManyField(School) #connects DepartmentName to School (i think)
	#many departments belong to one school 
	
	def __str__(self):
		return self.name

class Course(models.Model):
	#general info
	courseNumber=models.CharField(max_length=10)
	name=models.CharField(max_length=30, null=True, blank=True)
	department=models.ForeignKey('Department', on_delete=models.DO_NOTHING) #connects Course to DepartmentName
	#a class only belongs to a single department(usually)
	gradeReceived=models.CharField(max_length=2)

	#ratings, 1-10
	easyRating=models.IntegerField(
		validators=[MaxValueValidator(5), MinValueValidator(1)],
		help_text='(1)= :D (5)= >:(', null=True, blank=True)
	InterestingRating=models.IntegerField(
		validators=[MaxValueValidator(5), MinValueValidator(1)],
		help_text='(1)= :D (5)= >:(', null=True, blank=True)

	#amount of work
	homework=models.BooleanField()
	numProjects=models.IntegerField(
		validators=[MaxValueValidator(10), MinValueValidator(1)], null=True, blank=True)
	numTests=models.IntegerField(
		validators=[MaxValueValidator(15), MinValueValidator(0)], null=True, blank=True)
	testDiff=models.IntegerField(
		validators=[MaxValueValidator(5), MinValueValidator(1)],
		help_text='(1)= :D (5)= >:(', null=True, blank=True) #rated 1-10
	time_spent=models.IntegerField(
		validators=[MaxValueValidator(15), MinValueValidator(0)],
		help_text='For classes that took more than 15 hours, just put 15', null=True, blank=True)

	def __str__(self):
		return self.courseNumber

# class MyModelName(models.Model):
    # """A typical class defining a model, derived from the Model class."""

    # # Fields
    # my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    # ...

    # # Metadata
    # class Meta: 
    #     ordering = ['-my_field_name']

    # # Methods
    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of MyModelName."""
    #     return reverse('model-detail-view', args=[str(self.id)])
    
    # def __str__(self):
    #     """String for representing the MyModelName object (in Admin site etc.)."""
    #     return self.my_field_name


