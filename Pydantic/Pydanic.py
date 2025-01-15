from lib2to3.btm_matcher import type_repr


class ProductWithoutPydantic:
    def __init__(self,name : str ,price : float ,in_stock: bool):
        self.name = name
        self.price = price
        self.in_stock = in_stock

if __name__ == "__main__":
    example_prodcut = ProductWithoutPydantic("ornek",1000,20);
    print(example_prodcut.in_stock)
    external_data = {
        "name":"laptop",
        "price" : "999",
        "in_stock" : "true"
    }
    proudct =  ProductWithoutPydantic(
        name= external_data["name"],
        price= float(external_data["price"]),
        in_stock= bool(external_data["in_stock"])
    )
    print(type(proudct.name))
    print(type(proudct.in_stock))
    print(type(proudct.price))