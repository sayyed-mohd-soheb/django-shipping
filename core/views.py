from django.shortcuts import render
from .models import Product
from .utils import find_best_box

# Create your views here.

def pg1(request):
    box = None

    if request.method == "POST":
        length = float(request.POST.get("length"))
        width = float(request.POST.get("width"))
        height = float(request.POST.get("height"))
        weight = float(request.POST.get("weight"))

        # temporary product object
        product = Product(
            length=length,
            width=width,
            height=height,
            weight=weight
        )

        box = find_best_box(product)

    return render(request, "index.html", {"box": box})