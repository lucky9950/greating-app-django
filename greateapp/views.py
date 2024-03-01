from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import datetime

def get_greeting(request):
    current_time = datetime.datetime.now().time()

    if current_time < datetime.time(12, 0):
        greeting = 'Good Morning'
    elif current_time < datetime.time(18, 0):
        greeting = 'Good Afternoon'
    else:
        greeting = 'Good Evening'

    context = {'greeting': greeting}
    return render(request, 'index.html', context)
