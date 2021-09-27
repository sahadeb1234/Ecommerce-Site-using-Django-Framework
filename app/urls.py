from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # path('', views.index, name="index"),
    path("", indexView.as_view(), name="index"),


    path('seller_account_intro/', views.selleraccountintr, name="seller_account_intro"),
    path('your_seller_account/', views.yourselleraccount, name="your_seller_account"),
    path('your_addresses/', views.youraddress, name="your_addresses"),
    path('add_new_address/', views.addnewaddress, name="add_new_address"),
    path("allproducts/", AllproductsView.as_view(), name="allproducts"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="product"),
    path("addtocart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    path("my-cart/", MyCartView.as_view(), name="myCart")
   

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)