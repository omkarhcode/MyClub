from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			# Redirect to a success page.
			return redirect('home')
		else:
			messages.success(request, ("There was an error Logging In, Please try again..."))
			# Return an 'invalid login' error message.
			return redirect('login')
	else:
		return render(request, 'authenticate/login.html', {})



def logout_user(request):
	logout(request)
	messages.success(request, ("You were logged out..."))
	return redirect('home')