from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	data = {
		'first_name': request.user.first_name,
		'last_name': request.user.last_name,
		'username': request.user.username
	}
	return render(request, 'accounts/home.html', data)
