from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from products.models import Product


# Create your views here.

class SearchProductView(ListView):
    template_name = 'search/view.html'

    def get_context_data(self, *args, **kwargs):
        request = self.request
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = request.GET.get('q')
        context['query'] = query
        return context
        # print("context", context)

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        # print(request.GET)
        query = method_dict.get('q', None)
        # print('query', query)
        if query is not None:
            # return Product.objects.filter(lookups).distinct()
            return Product.objects.search(query)
        return Product.objects.featured()

        # __icontains = fields contains this
        # __iexact = fields is exactly this
