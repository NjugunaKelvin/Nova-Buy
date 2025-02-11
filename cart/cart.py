from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        # get session key if it exists
        cart = self.session.get('session_key')

        # if the user is new, no session key   Create one
        if "session_key" not in request.session:
            cart = self.session['session_key'] = {}
        
        # make cart available on all pages of the site
        self.cart =cart

    def add(self, product):
        product_id = str(product.id)

        # logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] ={'price' : str(product.price)}
            self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # get ids from carts
        product_ids = self.cart.keys()

        # use ids to look up products in database models
        products = Product.objects.filter(id__in=product_ids)

        # return the looked up products
        return products

