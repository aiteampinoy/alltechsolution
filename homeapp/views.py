from django.shortcuts import render, redirect

def home(request):
    return render(request, 'homeapp/home.html')

def index(request):
    return render(request, 'homeapp/index.html')

def applications_view(request):
    applications = [
        {'name': 'App 1', 'description': 'Description of App 1'},
        {'name': 'App 2', 'description': 'Description of App 2'},
        # Add more applications as needed
    ]
    return render(request, 'homeapp/applications.html', {'applications': applications})

def about(request):
    return render(request, 'homeapp/about.html')

def mission(request):
    return render(request, 'homeapp/mission.html')

def vision(request):
    return render(request, 'homeapp/vision.html')

def clientdataentry(request):
    return render(request, 'homeapp/clientdataentry.html')

def contact(request):
    return render(request, 'homeapp/contact.html')

def apps(request):
    return render(request, 'homeapp/apps.html')

from django.shortcuts import render

# Existing views
def home(request):
    return render(request, 'homeapp/home.html')

def index(request):
    return render(request, 'homeapp/index.html')

# Add views for the new URLs
def attendance_view(request):
    return render(request, 'homeapp/attendance.html')

def payroll_view(request):
    return render(request, 'homeapp/payroll.html')

def tasks_management_view(request):
    return render(request, 'homeapp/tasks_management.html')

def inventory_view(request):
    return render(request, 'homeapp/inventory.html')

def online_grocery_view(request):
    return render(request, 'homeapp/online_grocery.html')
