import os 
import petpy 
import pandas
import json

key = os.getenv('API_KEY')
secret = os.getenv('SECRET')


pf = petpy.Petfinder(key=key, secret=secret)

def breeds(): 
    cat_breeds = open("cats/cat_breeds.json","w+")
    cats = pf.breeds('cat') 
    cat_breeds.write(json.dumps(cats))
    cat_breeds.close() 
    dog_breeds = open("dogs/dog_breeds.json","w+")
    dogs = pf.breeds('dog') 
    dog_breeds.write(json.dumps(dogs))
    dog_breeds.close() 
    

if __name__ == "__main__":
    breeds()
    pass