from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.urls import reverse

from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display a blank registration form
        form = UserCreationForm()
    else:
        # Process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect them to home page.
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST
                                              ['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
