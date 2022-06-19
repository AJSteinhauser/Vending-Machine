from django.shortcuts import render
from .models import Drinks

# Create your views here.


def vendingpage(request):
    context = {};
    context['rows'] = getherDrinks();
    return render(request, 'vending.html', context);

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