from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa

# Create your views here.

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    user = request.user

    size = request.POST['size']

    cart, created = Cart.objects.get_or_create(user = user)
    cart_item, created = CartItem.objects.get_or_create(cart = cart, product = product, product_size = size)

    cart_item.product_name = product.name
    cart_item.product_img = product.img
    cart_item.quantity += 1
    cart_item.price += product.price
    cart_item.product_size = size

    cart.total_price += product.price

    cart_item.save()
    cart.save()

    messages.info(request, "Added to Cart!")

    return redirect("product_detail", product_id = product_id)

@login_required
def view_cart(request):
    user = request.user
    cart = Cart.objects.get(user = user)
    cart_items = CartItem.objects.filter(cart = cart)

    return render(request, 'cart.html', {"cart_items" : cart_items, "cart" : cart})

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id = item_id)
    user = request.user
    product = Product.objects.get(id = cart_item.product_id)
    cart = cart_item.cart

    if request.POST.get('qty-add'):
        cart_item.quantity += 1
    elif request.POST.get('qty-sub'):
        cart_item.quantity -= 1

        if cart_item.quantity <= 0:
            cart_item.delete()
            
            cart_items = CartItem.objects.filter(cart = cart)
            cart.total_price = sum(item.price for item in cart_items)
            
            cart.save()

            return redirect('view_cart')
    
    cart_item.price = (product.price * cart_item.quantity)

    cart_item.save()

    cart_items = CartItem.objects.filter(cart = cart)

    cart.total_price = sum(item.price for item in cart_items)
    cart.save()
    
    return redirect('view_cart')

def download_invoice(request):
    cart = Cart.objects.get(user=request.user)


    cart_items = CartItem.objects.filter(cart=cart)


    total_price = cart.total_price


    html = render_to_string('invoice_template.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'user': request.user,
    })


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'


    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), result)


    if not pdf.err:
        response.write(result.getvalue())
        return response
    else:
        return HttpResponse('Error generating PDF')