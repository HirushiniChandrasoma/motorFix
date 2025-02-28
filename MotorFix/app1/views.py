from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import CarParts

# Signup Page View
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')  # Redirect back to signup page
        
        # Create user
        User.objects.create_user(username=uname, email=email, password=pass1)

        messages.success(request, "Your account has been created successfully!")
        return redirect('login')  # Redirect to login page
    
    return render(request, 'signup.html')

# Login Page View
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('view-items')  # Redirect to items view after login
        else:
            messages.error(request, "Username or password is incorrect!")
            return redirect('login')

    return render(request, 'login.html')

# Create CarParts
def add_items(request):
    if request.method == "POST":
        itemId = request.POST['itemId']
        itemName = request.POST['itemName']
        itemType = request.POST['itemType']
        itemDescription = request.POST['itemDescription']
        itemPrice = request.POST['itemPrice']
        itemImage = request.FILES.get('itemImage')  # Handling image uploads

        data = CarParts(
            itemId=itemId, 
            itemName=itemName, 
            itemType=itemType, 
            itemDescription=itemDescription, 
            itemPrice=itemPrice,
            itemImage=itemImage  # Storing image
        )
        data.save()
  
        return redirect('view-items')

    return render(request, 'adddetails.html')

# Retrieve CarParts
def view_items(request):
    carparts = CarParts.objects.all()
    return render(request, 'view.html', {'carparts': carparts})

# Update CarParts
def update_items(request, pk):
    carparts = get_object_or_404(CarParts, id=pk)

    if request.method == 'POST':
        carparts.itemName = request.POST['itemName']
        carparts.itemType = request.POST['itemType']
        carparts.itemPrice = request.POST['itemPrice']
        carparts.itemDescription = request.POST['itemDescription']
        carparts.itemImage = request.FILES.get('itemImage', carparts.itemImage)  # Keep old image if no new one
        carparts.save()

        return redirect('view-items')

    return render(request, 'update.html', {'carparts': carparts})

# Delete CarParts
def delete_items(request, pk):
    carparts = get_object_or_404(CarParts, id=pk)

    if request.method == 'POST':
        carparts.delete()
        return redirect('view-items')

    return render(request, 'delete_account.html', {'carparts': carparts})
