from django.shortcuts import render,redirect
from .models import Users
from cryptography.fernet import Fernet

file = open("encryption.key", "rb");
secret = file.read();
file.close();
encrpytion = Fernet(secret);

# Create your views here.
def signup(request): 
    if request.session.has_key('userID'):
        return redirect('homepage');
    context = {}

    if request.method == "POST":
        password = request.POST["password"];
        username = request.POST["username"];
        if len(password) < 6: 
            context["error"] = "Malformed password";
        if Users.objects.filter(username=username).exists():
            obj = Users.objects.get(username=username);
            context["error"] = "Username is taken. Try a different username.";
        else:
            password = encrpytion.encrypt(str.encode(password));
            obj = Users(
                username = username,
                userPassword = password
            )
            obj.save();
            request.session['money'] = obj.userCash;
            request.session['userID'] = obj.userID;
            return redirect('homepage');
    return render(request,"signup.html", context);

def logout(request):
    if not request.session.has_key('userID'):
        return redirect('homepage');
    del request.session['userID'];
    del request.session['money'];
    return redirect('homepage');
    

def login(request): 
    context = {};
    if request.session.has_key('userID'):
        return redirect('homepage');
    if request.method == "POST":
        password = request.POST["password"];
        username = request.POST["username"];
        if not Users.objects.filter(username=username).exists():
            context['error'] = "No account exists with that username & password combination";
            return render(request, "login.html", context);
        plr = Users.objects.get(username=username);
        if password != str(encrpytion.decrypt(plr.userPassword).decode()):
            context['error'] = "There is not an account with that username & password combination";
            #context['error'] = str(password) + "\n" + str(encrpytion.decrypt(plr.userPassword).decode());
            return render(request, "login.html", context);
        request.session['money'] = str(plr.userCash);
        request.session['userID'] = plr.userID;
        return redirect('homepage');
    return render(request, "login.html", context);

        
    