from django.shortcuts import render
from .models import Product
from product_management.firebase_utils import upload_image_to_firebase

def product_list(request):
    item_products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': item_products})

def product_create(request):
    if request.method == 'POST':
        product_name = request.POST.get('name')
        price_purchase = float(request.POST.get('price_purchase'))
        price_sale = float(request.POST.get('price_sale'))
        quantity = int(request.POST.get('quantity'))
        image = request.FILES['file']

        # Format the filename using the product name
        formatted_filename = product_name.replace(" ", "_").lower()
        file_url = upload_image_to_firebase(image, 'products', formatted_filename)

        product = Product(
            name=product_name,
            price_purchase=price_purchase,
            price_sale=price_sale,
            quantity=quantity,
            image=file_url
        )
        product.save()

    return render(request, 'products/add_product.html')