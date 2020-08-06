from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Worker, Application
from django.core.mail import send_mail


# registration things


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mysite:home')
        else:
            messages.info(request, '  Username OR password is incorrect. Try again')

    context = {}
    return render(request, 'registration/login.html', context)


def registerpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mysite:login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('mysite:login')


# website things


@login_required(login_url='mysite:login')
def home(request):
    return render(request, 'mysite/home.html')


@login_required(login_url='mysite:login')
def search_labourers(request):
    return render(request, 'mysite/search_labourers.html')


@login_required(login_url='mysite:login')
def profiles(request):
    types = request.GET['type']
    location = request.GET['location']
    wage = request.GET['wage']
    all_labourers = Worker.objects.all()
    temp = 0
    return render(request, 'mysite/profiles.html',
                  {'labourers': all_labourers, 'type': types, 'location': location, 'wage': wage, 'temp': temp})


@login_required(login_url='mysite:login')
def aboutus(request):
    return render(request, 'mysite/aboutus.html')


@login_required(login_url='mysite:login')
def job(request):
    return render(request, 'mysite/job.html')


@login_required(login_url='mysite:login')
def add_application_form_submission(request):

    first_name = request.POST["inputFirstname"]
    second_name = request.POST["inputSecondname"]
    email = request.POST["inputEmail4"]
    phone_no = request.POST["inputPhoneno"]
    address = request.POST["inputAddress"]
    city = request.POST["inputCity"]
    job_type = request.POST["inputType"]
    job_experience = request.POST["inputexperience"]
    message = 'Job application from Mr ' + first_name +' ' + second_name + '\n' + 'email: ' + email + '\n' + 'phone_no: ' + \
              phone_no + '\n' + 'address: ' + address + '\n' + 'city: ' + city + '\n' + ' job_type: ' + job_type + '\n'\
              + 'job_experience: ' + job_experience + '\n'

    # adding application to database
    application = Application(first_name=first_name, second_name=second_name, email=email, phone_no=phone_no,
                              address=address, city=city, job_type=job_type, job_experience=job_experience)
    application.save()

    # send an email
    send_mail(
        'Job application: Mr ' + first_name,
        message,
        email,
        ['fixnbuildktm@gmail.com', email],
    )

    return render(request, 'mysite/job.html', {'first_name': first_name, 'second_name': second_name})


@login_required(login_url='mysite:login')
def conformation(request):
    temp = 0
    name = request.GET['name']
    # message = 'Request of hiring ' + name
    all_labourers = Worker.objects.all()

    return render(request, 'mysite/conformation.html', {'worker_name': name, 'labourers': all_labourers, 'temp': temp})


@login_required(login_url='mysite:login')
def hire_submission(request):
    temp = 1
    return render(request, 'mysite/conformation.html', {'temp': temp})
