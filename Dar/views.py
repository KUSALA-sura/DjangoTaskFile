from django.shortcuts import render,redirect
from django.http import HttpResponse
from Dar.models import myreg,Register

# Create your views here.
def darling(requset):
	return HttpResponse("<h1><center><i>Heloo Darling your my Bestie Forever and ever @R...! </i></center></h1>")
def htmltag(y):
	return HttpResponse("<h2>Hi welcome to Kushii World</h2>")
def uname(requset,name):
	return HttpResponse("<h2><center><i>Hello...<span style='color:green'>{}</span></i></center></h2>".format(name))
def userage(requset,un,ag):
	return HttpResponse("<h2 style='background-color:green;padding:23px'><center>Darling .... <span style='color:blue'>{}</span> and age <span style='color:pink'>{}</span></center></h2>".format(un,ag))
def student(requset,sid,sage,sname):
	return HttpResponse("<script>alert('Heloo Welcome {}')</script><h1> Hii darling {} my age is {} my id is{}</h1>".format(sname,sname,sage,sid))
def basic(requset):
	return render(requset,'html/basic.html')
def sample(requset):
	return render(requset,'html/sample.html')

def ytname(requset,kname):
	return render(requset,'html/ehtml.html',{'kn':kname})
def ptname(requset,id,sn):
	k={'i':id,'n':sn}
	return render(requset,'html/ptname.html',k)

def reddy(requset):
	return render(requset,'html/reddy.html')
def employee(requset):
	return render(requset,'html/emp.html')

def student(requset):
	if requset.method=='POST':
		stname=requset.POST.get('stname')
		stage=requset.POST.get('stage')
		ext={'stname':stname,'stage':stage}
		#st.objects.create(stname=stname,stage=stage)
		#return HttpResponse('sucessfully data entered')
		return render(requset,'html/studea.html',ext)
	return render(requset,'html/student.html')

def internalJS(requset):
	return render(requset,'html/internalJS.html')
	
def register(requset):
	if requset.method=='POST':
		uname=requset.POST.get('uname')
		Rollno=requset.POST.get('Rollno')

		uemail=requset.POST.get('uemail')
		sage=requset.POST.get('sage')
		dob=requset.POST.get('dob')
		addres=requset.POST.get('addres')
		#ext={'uname':uname,'rollno':Rollno,'uemail':uemail}
		myreg.objects.create(uname=uname,uemail=uemail,Rollno=Rollno,sage=sage,dob=dob,addres=addres)
		return redirect('deatiles')
		
		#print(requset.POST)
	return render(requset,'html/register.html')

def deatiles(requset):
	data=myreg.objects.all()
	return render(requset,'html/deatiles.html',{'data1':data})

def update(requset,num):
	info=myreg.objects.get(id=num)
	if requset.method=='POST':
		info.uname=requset.POST.get('uname')
		info.uemail=requset.POST.get('uemail')
		info.Rollno=requset.POST.get('Rollno')
		info.sage=requset.POST.get('sage')
		info.dob=requset.POST.get('dob')
		info.addres=requset.POST.get('addres')
		info.save()
		#return HttpResponse("<h1>Upated sucessfully</h1>")
		return redirect('deatiles')
	return render(requset,'html/update.html',{'info':info})
def raju(requset):
	return render(requset,'html/raju.html') 

def btfun(requset):
	return render(requset,'html/btfun.html')



def basicbt(requset):
	return render(requset,'html/basicbt.html')

def kushala(requset):
	if requset.method=='POST':
		
		print(requset.POST)
	return render(requset,'html/kushala.html')
def btrg(requset):
	return render(requset,'html/btrg.html')
def newrg(requset):
	return render(requset,'html/newrg.html')
# superusercreaation  and  in admin whoto access and database

def kushi(requset):
	#name="kushala"
	#email="kushalashetty@gmail.com"
	#age=20
	sk=Register(name="kushii",email="kushalashetty@gmail.com",age=20)
	sk.save()
	return HttpResponse("sucessfully data Entered into database")
#24/0/2021
def Reg(requset):
	if requset.method=='POST':
		name=requset.POST.get('name')
		email=requset.POST.get('email')
		#age=requset.POST.get('age')
		con=Register(name=name,email=email)

		con.save()
		return redirect('display')
		#Register.objects.create(name=name,email=email,age=age)
		#return HttpResponse("Data sucessfully Entered ")

	return render(requset,'html/Reg.html')
def display(requset):
	kk=Register.objects.all()
	return render(requset,'html/display.html',{'kk':kk})
def viw(requset,y):
	w=Register.objects.get(id=y)
	#return HttpResponse("Your name {} and yourmail {}".format(w.name,w.email))
	return render(requset,'html/viw.html',{'w':w})
### 25/06/2021
def rupdate(requset,x):
	t=Register.objects.get(id=x)
	if requset.method=='POST':
		name=requset.POST.get('name')
		email=requset.POST.get('email')
		t.name=name
		t.email=email
		t.save()
		return redirect('display')
	return render(requset,'html/rupdate.html',{'t':t})
def Del(requset,s):
	b=Register.objects.get(id=s)
	if requset.method=='POST':
		b.delete()
		return redirect('display')
	return render(requset,'html/Del.html',{'b':b})
def register2(requset):
	if requset.method=="POST":
		name=requset.POST.get('name')
		email=requset.POST.get('email')
		q=Register.objects.create(name=name,email=email)
		return HttpResponse("Data enetred successfully")
	return render(requset,'html/register2.html')
def display2(requset):
	a=Register.objects.all()
	return render(requset,'html/display2.html',{'a':a})
def viw2(requset,num):
	sk=Register.objects.get(id=num)
	return HttpResponse("your name {}".format(sk.name))