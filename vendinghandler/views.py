from django.shortcuts import render, redirect
from .models import Drinks
from login.models import Users
from django.http import HttpResponse
import json
# Create your views here.


def vendingpage(request):
    context = {};
    
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8');
        body = json.loads(body_unicode);
        drinkName = body['name'];
        purchase(request, drinkName, context); 
        print(context);
        print('error' in context);
        if not 'error' in context: 
            return HttpResponse("1")
        else: 
            return HttpResponse("0")
    else: 
        context['rows'] = getherDrinks();
    return render(request, 'vending.html', context);

def purchase(request,name,context):
    if not request.session.has_key('userID'):
        return redirect('homepage');
    person = None;
    try:
        person = Users.objects.get(userID=request.session['userID']);
    except: 
        context['error'] = 'There was an error accessing your account. You will not be charged at this time';
        return 
    drink = None;
    try:
        drink = Drinks.objects.get(name = name);
    except: 
        context['error'] = 'Could not find drink. You will not be charged at this time';
        return
    if person.userCash - drink.price < 0:
        print(person.userCash - drink.price, drink.price);
        context['error'] = 'You have insufficient funds to purchase this drink.';
        return
    if drink.inStock - 1 < 0: 
        context['error'] = "We are currently out of " + drink.name + ". Check back later";
        return;
    context['success'] = 'Success, your download will start shortly.';
    person.userCash = person.userCash - drink.price;
    person.save();
    drink.inStock = drink.inStock - 1;
    drink.save();
    request.session['money'] = str(person.userCash);


def getherDrinks():
    drinkTable = Drinks.objects.all();
    counter = 1;
    letter = 0;
    rows = [];
    drinkRow = [];
    for drink in drinkTable.iterator(): 
        code = str(chr(letter + 65)) + str(counter);
        drinkTable = {
            'name' : drink.name, 
            'price' : drink.price, 
            'description' : drink.description, 
            'stock' : drink.inStock,
            'image' : drink.imageName,
            'code' : code
        }
        drinkRow.append(drinkTable);
        if letter > 2:
            rows.append(drinkRow);
            drinkRow = [];
            letter = 0;
            counter += 1;
        else: 
            letter += 1;
    rows.append(drinkRow);
    return rows;

