from django.db.models.enums import TextChoices
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.


# def index(request):
#   return render(request, 'authentication/index.html')


class MyCartView(TemplateView):
    template_name =  "authentication/mycart.html"

class indexView(TemplateView):
    template_name = "authentication/index.html"
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['myname'] = "Sahadeb Rokaya"
      context['product_list'] = Product.objects.all().order_by("-id")
 
      return context



class AllproductsView(TemplateView):
    template_name = "authentication/all.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['myname'] = "Sahadeb Rokaya"
      context['Allproducts'] =  Category.objects.all()
      return context
class ProductDetailView(TemplateView):
    template_name = "authentication/product.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      url_slug = self.kwargs['slug']
      product = Product.objects.get(slug=url_slug)
      context['product'] =  product
      return context

class AddToCartView(TemplateView):
    template_name =  "authentication/addtocart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get product id from requested url
        productid = self.kwargs['pro_id']
        # get product
        productobj = Product.objects.get(id=productid)

        # check if cart exists
        cartid = self.request.session.get("cartid", None)
        if cartid:
            cart_obj = Cart.objects.get(id=cartid)
            this_product_in_cart = cart_obj.cartproduct_set.filter(
                product=productobj)

            # item already exists in cart
            if this_product_in_cart.exists():
                cartproduct = this_product_in_cart.last()
                cartproduct.quantity += 1
                cartproduct.subtotal += productobj.selling_price
                cartproduct.save()
                cart_obj.total += productobj.selling_price
                cart_obj.save()
            # new item is added in cart
            else:
                cartproduct = CartProduct.objects.create(
                    cart=cart_obj, Product=productobj, rate=productobj.selling_price, quantity=1, subtotal=productobj.selling_price)
                cart_obj.total += productobj.selling_price
                cart_obj.save()

        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            cartproduct = CartProduct.objects.create(
                cart=cart_obj, Product=productobj, rate=productobj.selling_price, quantity=1, subtotal=productobj.selling_price)
            cart_obj.total += productobj.selling_price
            cart_obj.save()

        return context


   




def selleraccountintr(request):

    return render(request, 'authentication/seller_account_intro.html')

def yourselleraccount(request):
    return render(request, 'authentication/your_seller_account.html' )

def youraddress(request):
    return render(request, 'authentication/your_addresses.html' )

def addnewaddress(request):
    return render(request, 'authentication/add_new_address.html')
