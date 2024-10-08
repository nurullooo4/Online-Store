from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from app_main.models import Product, Comment, Cart, Category
from app_users.models import Customer


def home_page(request):
    categories = Category.objects.all().order_by('id')
    query = request.GET.get('q')
    search = request.GET.get('search', '')
    products = Product.objects.all()

    category_filter = request.GET.get('category', '')
    if category_filter:
        products = products.filter(category__slug=category_filter)

    if search:
        products = products.filter(name__icontains=search)
    if query:
        if query == 'expensive':
            products = products.order_by('-new_price')
        elif query == 'cheap':
            products = products.order_by('new_price')
        elif query == 'rating':
            products = products.order_by('-rating')
        elif query == 'new-arrivals':
            products = products.order_by('-created')

    cart_products_quantity = 0
    if request.user.is_authenticated:
        cart_products_quantity = len(request.user.cart_set.all())

    context = {
        'products': products,
        'categories': categories,
        'search': search,
        'is_home_page': True,
        'cart_products_quantity': cart_products_quantity,
        'selected_category': category_filter,
    }

    return render(request, 'index.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    similar_products = Product.objects.all().exclude(id=product_id).order_by('-rating')[:4]

    if request.method == 'POST':
        comment = request.POST.get('comment')
        
        if len(comment.strip()) >= 10:
            new_comment = Comment.objects.create(
                owner=request.user,
                product=product,
                body=comment
            )
            new_comment.save()
            return redirect(f'/detail/{product_id}#comments-section')

    context = {
        'product': product,
        'last_3_comments': product.comment_set.all()[::-1][:3],
        'similar_products': similar_products,
    }

    return render(request, 'detail.html', context)


@login_required(login_url='login')
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        try:
            cart = Cart.objects.create(
                product=get_object_or_404(Product, id=product_id),
                user=get_object_or_404(Customer, id=request.user.id),
                quantity=quantity
            )
            cart.save()
        except:
            product = request.user.cart_set.all().get(product__id=product_id)
            product.quantity += int(quantity)
            product.save()


    return redirect('detail', product_id=product_id)
