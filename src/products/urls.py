from django.conf.urls import url

from .views import ProductListView, ProductDetailSlugView
    # product_list_view, product_detail_view, ProductDetailView, ProductFeaturedListView, ProductFeaturedDetailView

urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),

    # url(r'^products-fbv/', product_list_view),
    # url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    # url(r'^product-fbv/(?P<pk>\d+)/$', product_detail_view),
    # url(r'^featured/', ProductFeaturedListView.as_view()),
    # url(r'^featured-detail/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
]
