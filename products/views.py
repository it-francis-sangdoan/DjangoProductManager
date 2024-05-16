from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
from product_management.firebase_utils import upload_image_to_firebase

def product_list(request):
    item_products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': item_products})

def handle_product_fields(product, request):
    product.name = request.POST.get('name')
    product.price_purchase = float(request.POST.get('price_purchase'))
    product.price_sale = float(request.POST.get('price_sale'))
    product.quantity = int(request.POST.get('quantity'))
    if 'file' in request.FILES:
        image = request.FILES['file']
        formatted_filename = product.name.replace(" ", "_").lower()
        file_url = upload_image_to_firebase(image, 'products', formatted_filename)
        if not file_url:
            return None
        product.image = file_url
    return product

def product_create(request):
    if request.method == 'POST':
        product = Product()
        product = handle_product_fields(product, request)
        if product is None:
            messages.error(request, 'Failed to upload image. Please try again.')
            return render(request, 'products/product_add.html', request.POST)
        product.save()
        messages.success(request, 'Product has been created successfully!')
        return redirect('product_list')
    return render(request, 'products/product_add.html')


# def product_create(request):
#     if request.method == 'POST':
#         product_name = request.POST.get('name')
#         price_purchase = float(request.POST.get('price_purchase'))
#         price_sale = float(request.POST.get('price_sale'))
#         quantity = int(request.POST.get('quantity'))
#         image = request.FILES['file']

#         # Format the filename using the product name
#         formatted_filename = product_name.replace(" ", "_").lower()
#         file_url = upload_image_to_firebase(image, 'products', formatted_filename)

#         product = Product(
#             name=product_name,
#             price_purchase=price_purchase,
#             price_sale=price_sale,
#             quantity=quantity,
#             image=file_url
#         )
#         product.save()

#     return render(request, 'products/product_add.html')

def product_update(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price_purchase = float(request.POST.get('price_purchase'))
        product.price_sale = float(request.POST.get('price_sale'))
        product.quantity = int(request.POST.get('quantity'))

        image = request.FILES['file']
        formatted_filename = product.name.replace(" ", "_").lower()
        file_url = upload_image_to_firebase(image, 'products', formatted_filename)
        print(file_url)
        product.image = file_url
        product.save()

    return render(request, 'products/product_update.html', {'product': product})

def product_delete(request, product_id):
    item_product = Product.objects.get(id=product_id)
    item_product.delete()
    messages.success(request, 'Product has been deleted successfully!')
    return redirect("/products/")
