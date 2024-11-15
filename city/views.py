from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from .mail import *
import random
from .forms import FeedbackForm
from django.http import HttpResponseRedirect
from .forms import GreenInitiativeForm
from .forms import QueryForm
from django.views import View
from django.views.generic.detail import DetailView



# Create your views here.
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from .email_utils import send_email

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    body = (
                        "Hello,\n\n"
                        "You requested a password reset. Click the link below to reset your password:\n\n"
                        "http://example.com/password_reset_confirm"
                    )
                    send_email(user.email, subject, body)
                return redirect("/password_reset_done/")
    password_reset_form = PasswordResetForm()
    return render(request, "city/password_reset.html", {"password_reset_form": password_reset_form})


class HomeView(View):
    def get(self, request):
        total_complaints = Complaint.objects.count()
        pending = Complaint.objects.filter(status='Pending').count()
        solved = Complaint.objects.filter(status='Resolved').count()
        new = Complaint.objects.filter(status='Submitted').count()
        context = {
            'total_complaints': total_complaints,
            'pending': pending,
            'solved': solved,
            'new': new
        }
        return render(request, 'city/home.html', context=context)

    def post(self, request):
        name = request.POST['username']
        email = request.POST['email']
        message = request.POST['message']
        Queries.objects.create(name=name, email=email, message=message)
        return redirect('home')
def about(request):

    return render(request,'city/about.html')

def login_page(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None and user.is_user==True:
            login(request,user)
            print(user.is_user)
            # return render(request,"city/login.html")
            return redirect('home')
        else:
            messages.info(request,'uername or password is incorrect')
        
    return render(request,"city/login.html")
 
def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            email=form.cleaned_data['email']
            sub='Account Created Successfully'
            messages.success(request,'Account Created '+ user)
            body=f'Hello {user},\n\tYou have successfully created the user account in Clean Dream. Kindly login to raise the complaints. Hope you will help us to make the city clean and green\n\t\t Thank You\n\nRegards,\nClean Dream\nWindsor'
            #mail(email,sub,body)
            return redirect('login')
    context={
        'form':form
    }
    return render(request,"city/register.html",context)

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST,request.FILES)
        if form.is_valid():
            types=form.cleaned_data['complaint_type']
            area=form.cleaned_data['area']
            tracking_id=(request.user.email[0:4]+str(random.randint(100,999))+types[0:2]+str(random.randint(0,9))+types[-1:-3]+area[1:3]).upper()
            complaint = form.save(commit=False)
            complaint.user_name = request.user
            complaint.tracking_id=tracking_id
            complaint.save()
            
            email_reciever=request.user.email
            sub='Complaint Registered'
            body=f'Hello {request.user}, \n\tYour complaint on {types} at {area}, It will be solved within two working days. You can track the complaint with this tracking {tracking_id}. \n\nClean Dream\nWindsor'
            #mail(email_reciever,sub,body)
            return redirect('user_complaints')
    else:
        form = ComplaintForm()
    return render(request, 'city/complaint.html', {'form': form})

@login_required(login_url='login')
def user_complaints(request):
    complaint=Complaint.objects.all().filter(user_name=request.user).order_by('-complaint_date')
    return render(request,'city/user_complaints.html',{'complaint':complaint})


def employee_login(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        
        if user is not None and user.is_employee==True:
            login(request,user)
            print(user.is_employee)
            # return render(request,"city/login.html")
            return redirect('emp_main')
        else:
            messages.info(request,'username or password is incorrect')
    
    return render (request,'city/employee_login.html')

@login_required(login_url='employee_login')
def emp_main(request):
    if request.user.is_employee==True:
        new=Complaint.objects.all().filter(status='Submitted').count()
        pending=Complaint.objects.all().filter(status='Pending').count()
        solved=Complaint.objects.all().filter(status='Resolved').count()
        query=Queries.objects.all().count()
        context={
            'new':new,
            'pending':pending,
            'solved':solved,
            'query':query
        }
        return render(request,'city/emp_main.html',context=context)
    else:
        return redirect('employee_login')


@login_required(login_url='employee_login')
def new_complaints(request):
    
    if request.user.is_employee==True:
        new=Complaint.objects.all().filter(status='Submitted')
        return render(request,'city/new_complaints.html',{'new':new})
    else:
        return redirect('employee_login')
    
@login_required(login_url='employee_login')
def pending_complaints(request):
    
    if request.user.is_employee==True:
        pending=Complaint.objects.all().filter(status='Pending')
        return render(request,'city/pending_complaints.html',{'pending':pending})
    else:
        return redirect('employee_login')

@login_required(login_url='employee_login')
def solved_complaints(request):
    
    if request.user.is_employee==True:
        solved=Complaint.objects.all().filter(status='Resolved')
        return render(request,'city/solved_complaints.html',{'solved':solved})
    else:
        return redirect('employee_login')



@login_required(login_url='employee_login')
def update_new_complaints(request,pk):
    
    if request.user.is_employee==True:
        complaints=Complaint.objects.get(id=pk)
        form =UpdateForm(instance=complaints)
        context={
            'form':form
        }
        if request.method=='POST':
            form=UpdateForm(request.POST,instance=complaints)
            if form.is_valid():
                form.save()
                return redirect('new_complaints')
        return render(request,'city/update_complaints.html',context=context)
    else:
        return redirect('employee_login')

@login_required(login_url='employee_login')
def update_pending_complaints(request,pk):
    
    if request.user.is_employee==True:
        complaints=Complaint.objects.get(id=pk)
        form =UpdateForm(instance=complaints)
        context={
            'form':form
        }
        if request.method=='POST':
            form=UpdateForm(request.POST,instance=complaints)
            if form.is_valid():
                email_reciever=complaints.user_name.email
                sub='Complaint Resolved'
                body=f'Hello {complaints.user_name}, \nYour complaint on {complaints.complaint_type} at {complaints.area} has been resolved. \n\t\tThank You\nClean Dream'
                form.save()
                #mail(email_reciever,sub,body)
                return redirect('pending_complaints')
        return render(request,'city/update_complaints.html',context=context)
    else:
        return redirect('employee_login')


@login_required(login_url='employee_login')
def update_solved_complaints(request,pk):
    
    if request.user.is_employee==True:
        complaints=Complaint.objects.get(id=pk)
        form =UpdateForm(instance=complaints)
        context={
            'form':form
        }
        if request.method=='POST':
            form=UpdateForm(request.POST,instance=complaints)
            if form.is_valid():
                form.save()
                return redirect('solved_complaints')
        return render(request,'city/update_complaints.html',context=context)
    else:
        return redirect('employee_login')


@login_required(login_url='employee_login')
def queries(request):
    if request.user.is_employee==True:
        queries=Queries.objects.all()
        if request.method=='POST':
            queries.all().delete()
            return redirect('queries')
        return render (request,'city/queries.html',{'queries':queries})
    else:
        return redirect('employee_login')

def check_status(request):
    if request.method=='POST':
        tracking_id=request.POST['id']
        try:
            complaints=Complaint.objects.get(tracking_id=tracking_id)
            return render(request,'city/check_status.html',{'complaints':complaints})
        except:
            messages.warning(request,'Invalid Tracking ID')
    return render(request,'city/check_status.html')

@login_required
def add_green_initiative(request):
    if request.method == 'POST':
        form = GreenInitiativeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('green_initiatives')
    else:
        form = GreenInitiativeForm()

    return render(request, 'city/add_green_initiative.html', {'form': form})


def green_initiatives(request):
    initiatives = GreenInitiative.objects.all()
    return render(request, 'city/green_initiatives.html', {'initiatives': initiatives})


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                feedback = form.save(commit=False)
                feedback.name = request.user.username
                feedback.save()
            else:
                form.save()
    else:
        feedback_list = Feedback.objects.all().order_by(
            '-date')  # Fetch all feedback, ordered by date (most recent first)
        numbers = range(1, 6)  # Example range from 1 to 5

        return render(request, 'city/feedback_list.html', {'feedback_list': feedback_list, 'numbers':numbers})

    # Get the previous URL from the referer header
    previous_url = request.META.get('HTTP_REFERER')
    if previous_url:
        return HttpResponseRedirect(previous_url)
    else:
        return redirect('home')  # Redirect to home if no referer is found



from django.shortcuts import render
from django.db.models import Q
from .models import Complaint, GreenInitiative

def search_results(request):
    query = request.GET.get('query')
    category = request.GET.get('category')
    results = []

    if category == 'complaints':
        results = Complaint.objects.filter(info__icontains=query)
    elif category == 'initiatives':
        results = GreenInitiative.objects.filter(
            Q(information__icontains=query) | Q(title__icontains=query)
        )

    return render(request, 'city/search_results.html', {'results': results, 'query': query, 'category': category})
class ComplaintDetailView(DetailView):
    model = Complaint
    template_name = 'city/complaint_detail.html'
    context_object_name = 'complaint'

def query_view(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can add a success message or redirect to a thank you page
            return redirect('home')  # Replace with your URL name for success page
    else:
        form = QueryForm()

    return render(request, 'city/query_form.html', {'form': form})


@login_required
def user_history(request):
    visit_history = request.session.get('visit_history', {})
    return render(request, 'city/user_history.html', {'visit_history': visit_history})

def services(request):
    services = Service.objects.all()
    return render(request, 'city/services.html', {'services':services})

@login_required(login_url='employee_login')
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            return redirect('services')
    else:
        form = ServiceForm()
        return render(request, 'city/add_service.html', {'form':form})
    
from django.shortcuts import render, get_object_or_404
def green_initiative_detail(request, pk):
    initiative = get_object_or_404(GreenInitiative, pk=pk)
    comments = GreenInitiativeComment.objects.filter(green_initiative=initiative).order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = GreenInitiativeCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.green_initiative = initiative
                comment.save()
                return redirect('green_initiative_detail', pk=initiative.pk)
        else:
            return redirect('login')
    else:
        form = GreenInitiativeCommentForm()

    return render(request, 'city/green_initiative_detail.html', {
        'initiative': initiative,
        'comments': comments,
        'form': form,
    })

@login_required()
def add_employee(request):
    user = request.user
    manager = Manager.objects.get(user=user)
    if(not manager):
        return redirect('home')
    if request.method == 'POST':
        user_ids = request.POST.getlist('users')
        MyUser.objects.filter(id__in=user_ids).update(is_employee=True)
        MyUser.objects.exclude(id__in=user_ids).update(is_employee=False)
        return redirect('manage_employees')
    else:
        return render(request, 'city/add_employees.html', {'users': MyUser.objects.all()})


def manager_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        manager = Manager.objects.filter(user=user).first()
        if user is not None and manager is not None:
            login(request, user)
            # return render(request,"city/login.html")
            return redirect('manage_employees')
        else:
            logout(request)
            messages.info(request, 'username or password is incorrect')

    return render(request, 'city/manager_login.html')