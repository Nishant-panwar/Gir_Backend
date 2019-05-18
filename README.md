# Gir_Backend
Gir is a market place, which connects different product vendors to consumers, using an online platform.Task here is to design and implement a backend system for Gir


### List all products
**Definition**

`GET /products`

**Response**

- `200 OK` on success

```json
[
    {
        "name": "OnePlus 6T (Mirror Black, 6GB RAM, 128GB Storage)",
        "type": "Electronics",
        "price": "37,999",
        "specs": "Camera, Display, Memory....",
        "quantity": "1"
    },
    {
        "name": "OnePlus 6T (Midnight Black, 8GB RAM, 128GB Storage)",
        "type": "Electronics",
        "price": "41,999",
        "specs": "Camera, Display, Memory....",
        "quantity": "1"
    }
]
```
### Add a product

**Definition**

`POST /products`

**Arguments**

- `"name"`:string a unique name for this product
- `"type"`:string a name of the product type from the pre decided type
- `"price"`:decimal the current price/cost of the product individually in Indian currency 
- `"specs"`:string the specifications of the product 
- `"quantity"`:integer the count of the product

**Response**

- `201 Created` on success
```json
    {
        "name": "OnePlus 6T (Mirror Black, 6GB RAM, 128GB Storage)",
        "type": "Electronics",
        "price": "37,999",
        "specs": "Camera, Display, Memory....",
        "quantity": "1"
    }
```
