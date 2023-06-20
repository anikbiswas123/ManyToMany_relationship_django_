from django.shortcuts import render,redirect
from .models import Customer, Products
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')


def AboutUs(request):
    return render(request,'about.html')

#add to customer

def add_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        if name and email and phone:
            Customer.objects.create(cus_name=name,cus_email=email,cus_mobile=phone)
            msg=name+'Record is successfully add'
            messages.success(request,msg)
            return redirect(add_customer)
    return render(request,'Add_and_Edit/add_customer.html')


def edit_customer(request):
    edit_info = ""
    edit_id = ""
    if request.method == 'POST' and 'edit' in request.POST:
        edit_id = request.POST.get('edit_id')
        if Customer.objects.filter(id = edit_id).exists():
            edit_info = Customer.objects.get(id = edit_id)
    
    if request.method == 'POST' and 'edit_info' in request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        e_id = request.POST.get('id')

        edit_info = Customer.objects.get(id = e_id)
        edit_info.cus_name = name
        edit_info.cus_email = email
        edit_info.cus_mobile = phone
        edit_info.save()
        msg = name + "'s record is successfully Update."
        messages.success(request, msg)
        return redirect('display_customer')

    data = {
        'edit': 'edit',
        'edit_info': edit_info,
    }
    return render(request, "Add_and_Edit/add_customer.html", data)

def display_customer(request):
    customers = Customer.objects.all()
    if request.method == "POST":
        delete_id = request.POST.get('delete_id')
        if Customer.objects.filter(id = delete_id).exists():
            cus = Customer.objects.get(id = delete_id)
            cus.delete()
            msg = cus.cus_name + "'s record is successfully Delete."
            messages.warning(request, msg)
            return redirect('display_customer')

    data = {
        'customers':customers,
        'total':customers.count(),
    }
    return render(request, 'Customer.html', data)

#products 


def add_product(request):
    cus = Customer.objects.all()

    if request.method == "POST":
        customer_id = request.POST.getlist('customer')    #getlist('category[]')
        c_id = [int(id) for id in customer_id]
        p_name = request.POST.get('p_name')
        quantity = request.POST.get('quantity')


        if customer_id and p_name and quantity:
            product = Products.objects.create(pro_name = p_name, pro_qty = quantity)
            product.cus.set(c_id)  # Assigning the many-to-many relationship using set()
            messages.success(request, "Product is successfully added.")
            return redirect(add_product)

    data = {
        'cus':cus,
    }
    return render(request, "Add_and_Edit/add_product.html", data)



def display_product(request):
    products = Products.objects.all()

    if request.method == "POST" and 'delete' in request.POST:
        delete_id = request.POST.get('delete_id')

        print(delete_id)
        if Products.objects.filter(id = delete_id).exists():
            pro = Products.objects.get(id = delete_id)
            pro.delete()
            msg = pro.pro_name + " record is successfully Delete."
            messages.warning(request, msg)
            return redirect('display_product')

    data = {
        'products': products,
        'total':products.count(),
    }
    return render(request, 'Product.html', data)


def edit_product(request):
    cus = Customer.objects.all()
    edit_info = None
    selected_customers = []

    if request.method == 'POST' and 'edit' in request.POST:
        edit_id = request.POST.get('edit_id')
        try:
            edit_info = Products.objects.get(id=edit_id)
            selected_customers = edit_info.cus.all()

        except Products.DoesNotExist:
            edit_info = None
    if request.method == 'POST' and 'edit_info' in request.POST:
        edit_id = request.POST.get('id')
        p_name = request.POST.get('p_name')
        quantity = request.POST.get('quantity')
        customer_ids = request.POST.getlist('customer')
        c_id = [int(id) for id in customer_ids]

        try:
            edit_info = Products.objects.get(id=edit_id)
            edit_info.pro_name = p_name
            edit_info.pro_qty = quantity
            edit_info.cus.set(c_id)
            edit_info.save()
            messages.success(request, "Product is successfully updated.")
            return redirect('display_product')
        except Products.DoesNotExist:
            edit_info = None

    data = {
        'pro': edit_info,
        'cus': cus,
        'selected_customers': selected_customers,
    }
    return render(request, 'Add_and_Edit/edit_product.html', data)

# from django.views import View
# # Class View
# class EditProductView(View):
#     def get(self, request):
#         cus = Customer.objects.all()
#         edit_info = None
#         selected_customers = []

#         data = {
#             'pro': edit_info,
#             'cus': cus,
#             'selected_customers': selected_customers,
#         }
#         return render(request, 'Add_and_Edit/edit_product.html', data)

#     def post(self, request):
#         cus = Customer.objects.all()
#         edit_info = None
#         selected_customers = []

#         if 'edit' in request.POST:
#             edit_id = request.POST.get('edit_id')
#             try:
#                 edit_info = Products.objects.get(id=edit_id)
#                 selected_customers = edit_info.cus.all()
#             except Products.DoesNotExist:
#                 edit_info = None

#         if 'edit_info' in request.POST:
#             edit_id = request.POST.get('id')
#             p_name = request.POST.get('p_name')
#             quantity = request.POST.get('quantity')
#             customer_ids = request.POST.getlist('customer')
#             c_id = [int(id) for id in customer_ids]

#             try:
#                 edit_info = Products.objects.get(id=edit_id)
#                 edit_info.pro_name = p_name
#                 edit_info.pro_qty = quantity
#                 edit_info.cus.set(c_id)
#                 edit_info.save()
#                 messages.success(request, "Product is successfully updated.")
#                 return redirect('display_product')
#             except Products.DoesNotExist:
#                 edit_info = None

#         data = {
#             'pro': edit_info,
#             'cus': cus,
#             'selected_customers': selected_customers,
#         }
#         return render(request, 'Add_and_Edit/edit_product.html', data)
