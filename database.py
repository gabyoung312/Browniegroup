products = {
     100: {"name":"Americano","price":125},
     200: {"name":"Brewed Coffee","price":100},
     300: {"name":"Cappuccino","price":120},
     400: {"name":"Espresso","price":120},
     500: {"name":"Latte","price":140},
     600: {"name":"Cold Brew","price":200},
     1000: {"name":"Tiramisu","price":150},
     1100: {"name":"Red Velvet","price":130},
     1200: {"name":"Tiramisu","price":150}
}
def get_product(code):
     return products[code]
def get_products():
     product_list = []
     for i,v in products.items():
          product = v
          product.setdefault("code",i)
          product_list.append(product)
     return product_list
