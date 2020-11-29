from django.shortcuts import render

def home(request):
	return render(request, 'home.html')


def revers(request):
	user_text = request.GET['usertext']
	word_text = user_text.split()
	count_word_text = len(word_text)
	reversed_text = user_text[::-1]
	return render(request, 'revers.html', {'user_text':user_text,
		'reversedtext':reversed_text, 'count_word_text':count_word_text})