from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def product_list(request):
    """
    Fetches all products and recommendations from MongoDB Atlas.
    """
    # 1. Retrieve all items for the 'All Products' section
    all_products = Product.objects.all()
    
    # 2. Logic for recommendations (Currently showing all items)
    # This ensures your 'orange' appears in both lists as per the example
    recommendations = Product.objects.all() 

    # 3. Use clear keys that match your HTML loops
    context = {
        'products': all_products,
        'recommendations': recommendations,
    }

    return render(request, 'store/product_list.html', context)

def add_product(request):
    """
    Handles the creation of new products and saves them to MongoDB Atlas.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Directly inserts the new document into your Cluster0 collection
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
        
    return render(request, 'store/add_product.html', {'form': form})