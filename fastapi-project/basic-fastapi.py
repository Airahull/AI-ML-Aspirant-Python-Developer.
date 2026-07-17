from fastapi import FastAPI
# now creating a route in fastapi to get the data from the user and then we will use that data to predict the price of the product.
app = FastAPI()
# it is a simple get request for checking api is working or not .
# it is a static route (in which value doesnt change ).

@app.get("/") 
def home():
    return {"message ":"welcome to the ecomerce fastapi project"} # it is a simple get request for checking api is working or not.

#dynamic route is basically in which output change according to parameter .
@app.get("/product/{id}")
def getproduct(id :int):
    
    products=["iphone","redmi","oppo","vivo"]#list of products.
    return products[id] # id is basically a index number.

