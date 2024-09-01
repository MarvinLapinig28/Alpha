from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import  Staff
from django.contrib import messages
from app.models import  CustomUser



@login_required(login_url='/')
def HOME(request):
    staff = Staff.objects.all()
    staff_count = Staff.objects.all().count()

    context = {
        'staff': staff,
        'staff_count': staff_count,
    }
    return render(request,'Hod/home.html',context)


def ADD_STAFF(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is Already Taken!')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username is Already Taken!')
            return redirect('add_staff')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                user_type = 2,
            )
            user.set_password(password)
            user.save()

            staff = Staff (
                admin = user,
                address = address,
                gender = gender,
            )
            staff.save()
            messages.success(request,'Staff are Successfully Added !')
            return redirect('add_staff')
    return render(request,'Hod/add_staff.html')


def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context = {
        'staff':staff,
    }
    return render(request,'Hod/view_staff.html',context)


def EDIT_STAFF(request,id):
    staff = Staff.objects.get(id = id)

    context = {
        'staff':staff,
    }
    return render(request,'Hod/edit_staff.html',context)


def UPDATE_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')


        user = CustomUser.objects.get(id=staff_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.gender = gender
        staff.address = address

        staff.save()
        messages.success(request, 'Record Are Successfully Updated !')
        return redirect('view_staff')
    return render(request, 'Hod/edit_staff.html')


def DELETE_STAFF(request,admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request, 'Staff Are Successfully Deleted !')
    return redirect('view_staff')
