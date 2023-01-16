from django.shortcuts import render

# Create your views here.
def design(request):
    return render(request, "designapp/bookdesign.html")