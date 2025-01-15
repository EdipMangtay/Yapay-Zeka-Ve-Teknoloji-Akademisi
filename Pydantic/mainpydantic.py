from pydantic import BaseModel
class ProductPydantic(BaseModel):
    nane: str;
    price: float;
    in_stock: bool;

if __name__ == "__main__":
    external_data = {
        "name":"laptop",
        "price" : "999",
        "in_stock" : "true"
    }
    proudct =  ProductPydantic(
        name= external_data["name"],
        price= (external_data["price"]),
        in_stock= (external_data["in_stock"])
    )
    print(type(proudct.name))
    print(type(proudct.in_stock))
    print(type(proudct.price))
