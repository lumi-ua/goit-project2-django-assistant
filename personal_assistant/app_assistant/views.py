from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'app_assistant/index.html', {"title": "Personal assistant"})
