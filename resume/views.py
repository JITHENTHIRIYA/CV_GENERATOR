from django.shortcuts import render
from .models import Profile

# Create your views here.


def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        phone = request.POST.get("phone", "")
        email = request.POST.get("email", "")
        school = request.POST.get("school", "")
        degree= request.POST.get("degree", "")
        university = request.POST.get("university", "")
        about_you = request.POST.get("about_you", "")
        skill = request.POST.get("skill", "")
        previous_work = request.POST.get("previous_work", "")


        profile = Profile(name = name,phone=phone,email=email,school=school,degree = degree,university = university,about_you = about_you,skill = skill,previous_work = previous_work)
        profile.save()
    return render(request,"accept.html")

def rsme(request,id):
    user_profile = Profile.objects.get(pk = id)
    return render(request,"resume.html",{'user_profile':user_profile})




