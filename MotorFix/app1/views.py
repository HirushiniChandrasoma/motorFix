from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Profile  # Import Profile model
from .forms import UserUpdateForm, ProfileUpdateForm


# Profile Page View - Displays the profile details
@login_required
def ProfilePage(request):
    try:
        profile = Profile.objects.get(user=request.user)  # Get the associated profile
    except Profile.DoesNotExist:
        profile = None  # Handle case where no profile exists

    return render(request, 'profile.html', {'profile': profile})


# Update Profile View - Handles profile updates (both user details and profile details)
@login_required
def update_profile(request):
    # Check if the method is POST to handle form submission
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)  # User update form
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)  # Profile update form

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # Save user details
            profile_form.save()  # Save profile details
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')  # Redirect to the profile page after update
    else:
        user_form = UserUpdateForm(instance=request.user)  # Create the form with current user data
        profile_form = ProfileUpdateForm(instance=request.user.profile)  # Create the form with current profile data

    # Render the profile update page with the forms
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'updateprofile.html', context)


# Delete Account View - Handles account deletion
@login_required
def delete_account(request):
    # Check if the method is POST to handle form submission for account deletion
    if request.method == 'POST':
        request.user.delete()  # Delete the user account
        messages.success(request, 'Your account has been deleted.')
        return redirect('login')  # Redirect to login after account deletion
    return render(request, 'delete_account.html')  # Render the account deletion page


# Signup Page View - Handles user registration and profile creation
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')  # Get the username from the form
        email = request.POST.get('email')  # Get the email from the form
        pass1 = request.POST.get('password')  # Get the password from the form
        pass2 = request.POST.get('confirm_password')  # Get the confirm password from the form

        # Check if the passwords match
        if pass1 != pass2:
            return HttpResponse("Your password and confirm password do not match!!")
        else:
            # Create user if passwords match
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()

            # Create Profile for the user
            profile = Profile(user=my_user)  # Create a Profile instance for the newly registered user
            profile.save()

            messages.success(request, "Your account has been created successfully!")
            return redirect('login')  # Redirect to login after successful registration
        
    return render(request, 'signup.html')  # Render the signup page


# Login Page View - Handles user login
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Get the username from the form
        pass1 = request.POST.get('password')  # Get the password from the form
        user = authenticate(request, username=username, password=pass1)  # Authenticate the user

        if user is not None:
            login(request, user)  # Log the user in if authentication is successful
            return redirect('profile')  # Redirect to profile page after login
        else:
            return HttpResponse("Username or password is incorrect!!!...")  # Return error if authentication fails

    return render(request, 'login.html')  # Render the login page
