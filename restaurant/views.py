from django.shortcuts import render, redirect
from restaurant.forms import UserForm


from restaurant.models import User,food_item, drink_item, table, Order
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'restaurant/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'restaurant/registration.html',{'user_form':user_form,'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request,'restaurant/index.html',{'username':username})
                # return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("Invalid Login Details Supllied")
    else:
        return render(request,'restaurant/login.html',{})

def order(request):
    if request.method == "GET":
        return render(request,'restaurant/order.html',{"food_items":food_item.objects.all(),"drink_items":drink_item.objects.all(),"seats_2":table.objects.filter(seats=2),"seats_4":table.objects.filter(seats=4),"seats_10":table.objects.filter(seats=10)})
    elif request.method == "POST":
        Pizza_qty = int(request.POST["Pizza_qnty"])
        Burger_qty = int(request.POST["Burger_qnty"])
        Noodles_qty = int(request.POST["Noodles_qnty"])
        Coffee_qty = int(request.POST["Coffee_qnty"])
        Tea_qty = int(request.POST["Tea_qnty"])
        Juice_qty = int(request.POST["Juice_qnty"])
        Pizza_price = int(food_item.objects.filter(name="Pizza")[0].price)
        Burger_price = int(food_item.objects.filter(name="Burger")[0].price)
        Noodles_price = int(food_item.objects.filter(name="Noodles")[0].price)
        Coffee_price = int(drink_item.objects.filter(name="Coffee")[0].price)
        Tea_price = int(drink_item.objects.filter(name="Tea")[0].price)
        Juice_price = int(drink_item.objects.filter(name="Juice")[0].price)
        total_bill = (Pizza_qty*Pizza_price) + (Burger_qty*Burger_price) + (Noodles_qty*Noodles_price) + (Coffee_qty*Coffee_price) + (Tea_qty*Tea_price) + (Juice_qty*Juice_price)
        table_num = request.POST["table_number"]
        tbl = table.objects.filter(table_num=table_num)[0]
        if tbl.is_occupied == False:
            print("success")
            tbl.is_occupied = True
            tbl.save()
            billy = Order(Table_num=table_num,Pizza_qty=Pizza_qty,Burger_qty=Burger_qty,Noodles_qty=Noodles_qty,Coffee_qty=Coffee_qty,Tea_qty=Tea_qty,Juice_qty=Juice_qty,total_bill=total_bill)
            billy.save()
            return redirect('bill',billy.id)
        else:
            return render(request,'restaurant/order.html',{"food_items":food_item.objects.all(),"drink_items":drink_item.objects.all(),"seats_2":table.objects.filter(seats=2),"seats_4":table.objects.filter(seats=4),"seats_10":table.objects.filter(seats=10)})



def bill(request,orderId):
    return render(request,"restaurant/bill.html")










# --------------
