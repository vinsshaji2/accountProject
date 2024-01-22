from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from acApp.forms import myNewForm, mynewFormTwo, userform, userforminfo
from .models import User_details
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('acApp:user_login'))


def home(request):
    form = mynewFormTwo()
    if request.method == "POST":
        form = mynewFormTwo(request.POST)

        if form.is_valid():
            print("form validation is successfully completed")
            print("portfolio: " + form.cleaned_data["protfolio"])
            print("EMAIL: " + form.cleaned_data["email"])

    return render(request, "acApp/index.html", {"form": form})


@login_required
def index(request):
    form = myNewForm()
    if request.method == "POST":
        form = myNewForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("home")
        else:
            print("FORM IS INVALID")
    con = {"text": "PRAVEEN , PRASANTH", "form": form}
    return render(request, "acApp/basic.html", con)


def userinfo(request):
    if request.method == "POST":
        user_form = userform(request.POST)
        profile_form = userforminfo(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "profile_img" in request.FILES:
                profile.profile_img = request.FILES["profile_img"]

            profile.save()

            return redirect("acApp:index")

        else:
            print("Your form is not valid!", user_form.errors, profile_form.errors)

    else:
        user_form = userform()
        profile_form = userforminfo()

    con = {'userform': user_form, 'userforminfo': profile_form}
    return render(request, "acApp/user_info.html", con)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('passw')
        user = authenticate(username=username, password=password)

        if user:
            print(user.is_active)
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('acApp:index'))

            else:
                print("ACCOUNT IS NOT ACTIVE")
        else:
            print("Someone tried to logging and Failed !")
            print(f"username: {username} password: {password}")
            return HttpResponse("INVALID CREDENTIALS")

    else:
        return render(request, "acApp/user_login.html", {})

@login_required
def Register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        country = request.POST.get('country')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        postal_code = request.POST.get('pcode')

        user = User_details.objects.create(name=name
                                    ,email=email,address1=address1,address2=address2,city=city, phone=phone, date_of_birth=dob,gender=gender, country=country, postal_code=postal_code)
        if user:
            user.save()
            return HttpResponse("USER DETAILS SAVED TO DB!")
        print("USER DETAILS SAVED TO DB!")
    else:
        return render(request, "acApp/register.html")

@login_required
def update_user(request):
    if request.method == "POST":
        user_email = request.user.email
        print(user_email)
        user = get_object_or_404(User_details, email=user_email)
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.date_of_birth = request.POST.get('dob')
        user.gender = request.POST.get('gender')
        user.city = request.POST.get('city')
        user.country = request.POST.get('country')
        user.address1 = request.POST.get('address1')
        user.address2 = request.POST.get('address2')
        user.postal_code = request.POST.get('pcode')

        user.save()
        return HttpResponse("USER DETAILS UPDATED IN DB!")

    else:
        user_email = request.user.email
        print(user_email)
        user = get_object_or_404(User_details, email=user_email)
        print(user.gender)
        return render(request, "acApp/update.html", {"det": user})

@login_required
def user_details(request):
    print(request.user.username)
    u_name = request.user.username
    user_det = get_object_or_404(User, username=u_name)
    return render(request, "acApp/user_details.html", {"det": user_det, "s": u_name})


def user_delete(request, email):
    if request.method == "POST":
        user = get_object_or_404(User, email=email)
        user.delete()
        return HttpResponse("User deleted Successfully!!")
    else:
        return None