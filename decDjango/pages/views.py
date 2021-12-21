from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, Http404
from product.models import Course
from pages.forms import CourseForm

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1> This is Home Page </h1>")


def index_view(request, *args, **kwargs):
    context = {
        "course1" : " JAVA ",
        "course2" : " Python ",
        "course3" : " Selenium ",
        "course4" : " Business Analyst ",
        "course5" : " Software Testing ",
        }
    print(request.user)
    return render(request, "index.html", context)


def contact_view(request, *args, **kwargs):
    context = {
        "HouseNumber" : 3375,
        "AddressLine2" : " Spring Hill Pwky ",
        "State" : " Smyrna GA",
        "PhoneNumber" : " 777 380 6944 ",
        "Email" : " training@h2kinfosys.com ",
        "list_var" : [100, 200, 300, 400],
        }
    return render(request, "contact.html", context)



def course_view(request, my_id=1):
   # courseObj = Course.objects.get(id=my_id)
   # courseObj = get_object_or_404(Course, id=my_id)
    
    try:
        courseObj = Course.objects.get(id=my_id)
    except Course.DoesNotExist:
        raise Http404
    
    '''
    context = {
        "name" : courseObj.name,
        "duration" : courseObj.duration,
        "price" : courseObj.price,
       }
    '''
    context = {
        "obj" : courseObj,
        }
    
    return render(request, "Course.html", context)


def create_view(request):
    
    initial_data = {
        'name' : " Enter Name",
        'duration' : "6",
        'description': "Enter Description Here",
        'price': "999.99" ,
        'review': "Excellent!",
        }
    # courseObj = Course.objects.get(id=1)
    course_form = CourseForm(request.POST or None, initial= initial_data)
    # course_form = CourseForm(request.POST or None, instance=courseObj)
    if course_form.is_valid():
        course_form.save()
        course_form = CourseForm()
    
    context = {
        "course_form" : course_form,
        }
    
    return render(request, "create.html", context)