from django.shortcuts import render

def home(request):
	return render(request, 'home.html')


def revers(request):
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	return render(request, 'revers.html', {'user_text':user_text,
		'reversedtext':reversed_text})