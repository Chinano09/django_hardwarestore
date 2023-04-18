from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductCategory
from .forms import ProductForm, CategoryForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_protect

# Product
PRODUCT_LIST_PATH = '/product_list'


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def create_product(request):
    if 'user_id' not in request.session:
        return redirect(PRODUCT_LIST_PATH)
    if not request.user.is_authenticated:
        return redirect(PRODUCT_LIST_PATH)
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect(PRODUCT_LIST_PATH)
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def edit_product(request, pk):
    if 'user_id' not in request.session:
        return redirect(PRODUCT_LIST_PATH)
    if not request.user.is_authenticated:
        return redirect(PRODUCT_LIST_PATH)
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect(PRODUCT_LIST_PATH)
    return render(request, 'edit_product.html', {'form': form, 'product': product})


def delete_product(request, pk):
    if 'user_id' not in request.session:
        return redirect(PRODUCT_LIST_PATH)
    if not request.user.is_authenticated:
        return redirect(PRODUCT_LIST_PATH)
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect(PRODUCT_LIST_PATH)


# Category
CATEGORY_LIST_PATH = '/category_list'


def category_list(request):
    category = ProductCategory.objects.all()
    return render(request, 'category_list.html', {'category': category})


def create_category(request):
    if 'user_id' not in request.session:
        return redirect(CATEGORY_LIST_PATH)
    if not request.user.is_authenticated:
        return redirect(CATEGORY_LIST_PATH)
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect(CATEGORY_LIST_PATH)
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})


def edit_category(request, pk):
    if 'user_id' not in request.session:
        return redirect(CATEGORY_LIST_PATH)
    if not request.user.is_authenticated:
        return redirect(CATEGORY_LIST_PATH)
    category = get_object_or_404(ProductCategory, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        category = form.save(commit=False)
        category.save()
        return redirect(CATEGORY_LIST_PATH)

    return render(request, 'edit_category.html', {'form': form})


def delete_category(request, pk):
    if 'user_id' not in request.session:
        return redirect(CATEGORY_LIST_PATH)
    if not request.user.is_authenticated:
        return redirect(CATEGORY_LIST_PATH)
    category = get_object_or_404(ProductCategory, pk=pk)
    category.delete()
    return redirect(CATEGORY_LIST_PATH)


def category_products(request, pk):
    category = ProductCategory.objects.get(pk=pk)
    products = Product.objects.filter(category_id=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'product_list.html', context)

# Home


def home(request):
    return render(request, 'home.html')

# Register

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('CATEGORY_LIST_PATH')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login


# TODO: Fix redirection to homepage
@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['user_id'] =  user.id
                return redirect(CATEGORY_LIST_PATH)
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid user'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    logout(request)
    return redirect('home')