from django.shortcuts import render


# Create your views here.

def index(request):
    meetups = [
        {'title': "MyFirstMeetup"},
        {'title': "MySecondMeetup"}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })
