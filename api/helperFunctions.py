from vendinghandler.models import Drinks
import json




def getAllStock():
    drinksModel = Drinks.objects.all();
    table = {}
    for i in drinksModel:
        table[i.name] = i.inStock;
    return json.dumps(table);