from xml.etree.ElementTree import indent
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .helperFunctions import *
from rest_framework.exceptions import ParseError, NotFound, AuthenticationFailed



# Create your views here.




@api_view(['GET'])
def getAllStock(request):
    drinksModel = Drinks.objects.all();
    table = {}
    for i in drinksModel:
        table[i.name] = i.inStock;
    return Response(table);



@api_view(['GET'])
def getDrinkStock(request,drinkname):
    drink = None;
    try:
        drink = Drinks.objects.get(name = drinkname);
    except:
        raise NotFound("Drink: '" + drinkname + "' is not in the database")
    return Response(str(drink.inStock));


@api_view(['POST'])
def addDrinkStock(request,drinkname):
    drink = None;
    print(request.data)
    try:
        drink = Drinks.objects.get(name = drinkname);
    except:
        raise NotFound("Drink: '" + drinkname + "' is not in the database");
    try:
        if not 'amount' in request.data: 
            raise;
        if not 'password' in request.data:
            raise
    except :
        raise ParseError("Data is malformed")

    try: 
        if request.data['password'] != "secretpassword":
            raise;
    except: 
        raise AuthenticationFailed("Password is incorrect");
    
    try:
        drink.inStock = max(0,min(request.data['amount'] + drink.inStock, drink.maxStock));
    except :
        raise ParseError("Data is malformed")
    drink.save()
    return Response(str(drink.inStock) + " is the new amount");

@api_view(['POST'])
def changedrinkprice(request,drinkname):
    drink = None;
    print(request.data)
    try:
        drink = Drinks.objects.get(name = drinkname);
    except:
        raise NotFound("Drink: '" + drinkname + "' is not in the database");
    try:
        if not 'price' in request.data: 
            raise;
        if not 'password' in request.data:
            raise
    except :
        raise ParseError("Data is malformed: missing data")
    try: 
        if request.data['password'] != "secretpassword":
            raise;
    except: 
        raise AuthenticationFailed("Password is incorrect");
    
    try:
        drink.price = max(0, request.data['price']);
    except :
        raise ParseError("Data is malformed: failed to change price")
    drink.save()
    return Response(str(drink.price) + " is the new price");