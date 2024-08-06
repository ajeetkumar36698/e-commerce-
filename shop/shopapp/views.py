from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Customer,Product,OrderPlaced,Cart
from .forms import CustomerRegistionForm,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def base(request):
    return render(request,"shop/base.html")

def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,"shop/address.html",{'add':add})
# def index(request):
#     return render(request,"shop/index.html")
@login_required(login_url='/account/login/')
def add_to_cart(request):
    user=request.user
    Product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=Product_id)
    
    Cart(user=user,product=product).save()
    return redirect('/show_cart')
@login_required(login_url='/account/login/')
def show_cart(request):
    if(request.user.is_authenticated):
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        totalamount=0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount+shipping_amount
        
        return render(request,"shop/addtocart.html",{'cart':cart,'totalamount':totalamount,'amount':amount})




class indexView(View):
    def get(self,request):
        topwears=Product.objects.filter(category='TW')
        bottomwears=Product.objects.filter(category='BW')
        mobiles=Product.objects.filter(category='M')
        laptop=Product.objects.filter(category='L')

        return render(request,'shop/index.html',{'topwears':topwears,'bottomwears':bottomwears,'mobiles':mobiles,'laptop':laptop})



# def user_login(request):
#     return render(request,"shop/login.html")

# def profile(request):
#     return render(request,"shop/profile.html")
# @login_required(login_url='/account/login/')
class profile(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,"shop/profile.html",{'form':form})
    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if(form.is_valid()):
            usr = request.user
            name= form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulations!! Profile Update Successfull')

        return render(request,"shop/profile.html",{'form':form})
        


# def sign(request):
#     return render(request,"shop/sign.html")

class sign(View):
    def get(self,request):
        form=CustomerRegistionForm()
        return render(request,"shop/sign.html",{'form':form})
    def post(self,request):
        form=CustomerRegistionForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request,'Congratulations!! Registered Successfull')
        return render(request,"shop/sign.html",{'form':form})



    

# def product_details(request):
#     return render(request,"shop/product_details.html")
class product_details(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"shop/product_details.html",{'product':product})


def mobile(request,data=None):
	if data==None :
			mobiles = Product.objects.filter(category='M')
	elif data == 'Redmi' or data == 'Samsung':
			mobiles = Product.objects.filter(category='M').filter(brand=data)
	elif data == 'below':
			mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
	elif data == 'above':
			mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
	return render(request, 'shop/mobile.html', {'mobiles':mobiles})

@login_required(login_url='/account/login/')
def remove_from_cart(request, item_id):
    if request.method == 'POST':
        # Get the item from the cart
        item = get_object_or_404(Cart, id=item_id)
        # Remove the item from the cart
        item.delete()
    return redirect('/show_cart')


def laptopView(request,data=None):
	if data==None :
			laptops = Product.objects.filter(category='L')
	elif data == 'HP' or data == 'Dell':
			laptops = Product.objects.filter(category='L').filter(brand=data)
	elif data == 'below':
			laptops = Product.objects.filter(category='L').filter(discounted_price__lt=10000)
	elif data == 'above':
			laptops = Product.objects.filter(category='L').filter(discounted_price__gt=10000)
	return render(request, 'shop/laptop.html', {'laptops':laptops})

def topWearView(request,data=None):
	if data==None :
			topwears = Product.objects.filter(category='TW')
	elif data == 'Shirt' or data == 'TShirt':
			topwears = Product.objects.filter(category='TW').filter(brand=data)
	elif data == 'below':
			topwears = Product.objects.filter(category='TW').filter(discounted_price__lt=10000)
	elif data == 'above':
			topwears = Product.objects.filter(category='TW').filter(discounted_price__gt=10000)
	return render(request, 'shop/topwear.html', {'topwears':topwears})

def bottomWearView(request,data=None):
	if data==None :
			bottomWears = Product.objects.filter(category='BW')
	elif data == 'Jeans' or data == 'Lower':
			bottomWears = Product.objects.filter(category='BW').filter(brand=data)
	elif data == 'below':
			bottomWears = Product.objects.filter(category='BW').filter(discounted_price__lt=10000)
	elif data == 'above':
			bottomWears = Product.objects.filter(category='BW').filter(discounted_price__gt=10000)
	return render(request, 'shop/bottomwear.html', {'bottomWears':bottomWears})




def product_list(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(brand__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})