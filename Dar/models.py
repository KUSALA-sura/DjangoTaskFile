from django.db import models
# Create your models here.
class myreg(models.Model):
	uname=models.CharField(max_length=30)
	uemail=models.EmailField(max_length=20)
	Rollno=models.CharField(max_length=10)
	sage=models.IntegerField()
	dob=models.DateField(default=False)
	addres=models.CharField(max_length=30)

class Register(models.Model):
	name=models.CharField(max_length=20)
	email=models.EmailField(max_length=30)
	age=models.IntegerField(default=False)

	def __str__(self):
		return str(self.id)+""+self.name+str(self.age)
class SingUp(models.Model):
	fname=models.CharField(max_length=20)
	age=models.IntegerField(verbose_name = "age")
	def __str__(self):
		return self.fname


	class Meta:
		db_table = 'signup'
			
class profile(models.Model):
	name=models.CharField(max_length=20)
	email=models.EmailField(max_length=30)
	age=models.IntegerField()
	rollno=models.CharField(max_length=10)
	addres=models.TextField(null=True)
	sgpa=models.DecimalField(max_digits=6, decimal_places=4)
	cgpa=models.FloatField(null=True)
	dob=models.DateField()
	timet=models.DateTimeField(auto_now=True)
	img =models.ImageField(upload_to = "images/")
	upload = models.FileField(upload_to ="uploads/")
	done=models.BooleanField(default=False,verbose_name="languages")
	def __str__(self):
		return self.name




    