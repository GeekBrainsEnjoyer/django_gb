from django.shortcuts import redirect, render

from .forms import ProductForm


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        return redirect('hwapp:index')

    else:
        form = ProductForm()

    return render(request, 'hwapp4/product_form.html', {'form': form})
