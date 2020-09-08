import os 
from os import path as p
import petpy 
import pandas
import json

key = os.getenv('API_KEY')
secret = os.getenv('SECRET')


pf = petpy.Petfinder(key=key, secret=secret)

def breeds(): 
    if p.exists("cats/cat_breeds.json") and p.exists("dogs/dog_breeds.json"):
        print("json already generated")
        return

    else: 
        cat_breeds = open("cats/cat_breeds.json","w+")
        cats = pf.breeds('cat') 
        cat_breeds.write(json.dumps(cats))
        cat_breeds.close() 
        dog_breeds = open("dogs/dog_breeds.json","w+")
        dogs = pf.breeds('dog') 
        dog_breeds.write(json.dumps(dogs))
        dog_breeds.close() 
        return 
    

def catnames(): 
    if p.exists("cats/cat_names.txt"): 
        print("cat names already generated")
        return 
    else:
        cats = pf.animals(animal_type='cat',pages=100, return_df=True)
        with open("cats/cat_names.txt","w+") as cat_names: 
            cat_names.write(cats['name'].str.cat(sep='\n'))
        cat_names.close()
        return 
    

def dognames(): 
    if p.exists("dogs/dog_names.txt"): 
        print("dog names already generated")
        return 
    else: 
        dog = pf.animals(animal_type='dog',pages=100, return_df=True)
        with open("dogs/dog_names.txt","w+") as dog_names: 
            dog_names.write(dog['name'].str.cat(sep='\n'))
        dog_names.close()
        return 
    


if __name__ == "__main__":
    breeds() 
    catnames()
    dognames()
    pass