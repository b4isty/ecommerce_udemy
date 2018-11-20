from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView, DetailView
from .models import Product


# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        # print(context)
        return context


def product_list_view(request):
    queryset = Product.objects.all()
    context = {"qs": queryset}
    return render(request, "products/product_list_view.html", context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        # print(context)
        return context


def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)
  ############
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print("No product here")
    #     raise Http404("Product Doesn't Exist")
    # except:
    #     print("huuh")

###########
    instance = Product.objects.get_by_id(id=pk)
    if instance is None:
        raise Http404("Product Doesn't Exist")
    # print(qs)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product Doesn't Exist")

    # print(args, kwargs)
    context = {"object": instance}
    return render(request, "products/detail.html", context)
