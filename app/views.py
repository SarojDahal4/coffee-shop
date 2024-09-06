from django.shortcuts import render, redirect
from.models import reservation, contact, image
from .forms import ReservationForm, contactform
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home (request):
    context = {(home): home}
    return render (request , "app/home.html")
def menu (request):
    context = {(menu): menu}
    return render (request , "app/menu.html")


def about (request):
    context = {(about): about}
    return render (request , "app/about.html")

def service (request):
    context = {(service): service}
    return render (request , "app/service.html")


def reservation_p(request):
    submitted = False
   
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect(f"{reverse('reservation')}?submitted=True")
    else:
        form = ReservationForm
        if 'submitted' in request.GET:
            submitted = True

    
    
    context = {
        'form': form,
        'submitted': submitted
    }
    
    return render(request, 'app/reservation_p.html', context)



def contact(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            # Handle form submission, e.g., save data or send email
            form.save()  # or any other processing you want to do
            return redirect('contact')  # Redirect to a success page or elsewhere
    else:
        form = contactform()  # Initialize an empty form for GET request

    context = {'form': form}
    return render(request, 'app/contact.html', context)



def testimonial (request):
    context = {(testimonial): testimonial}
    return render (request , "app/testimonial.html")

def gallery (request):
    images=image.objects.all()
    context = {('images'): images}
    return render (request , "app/gallery.html", context)