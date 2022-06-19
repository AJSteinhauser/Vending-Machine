(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

const buttons = document.querySelectorAll(".keypad-button");
const textSpace = document.querySelector("#text-space");
const errorMessage = document.querySelector("#error-message");
const successMessage = document.querySelector("#success-message");
var textSpaceChanged = false;


var currenyFormatter = new Intl.NumberFormat('en-US',
                        {style: 'currency', currency: 'USD',
                          minimumFractionDigits: 2});


function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}


for (let i = 0; i < buttons.length; i++){
    let but = buttons[i];
    if (but.textContent != "#"){
        but.onclick = function(){ 
            if (!textSpaceChanged){ 
                textSpace.textContent = "";
                textSpaceChanged = true;
            }
            textSpace.textContent = textSpace.textContent.concat(but.textContent);
        }
    }
    else{
        but.onclick = function(){ 
            successMessage.textContent = "";
            let code = document.getElementById(textSpace.textContent.concat("_title"));
            if (code == null){
                errorMessage.textContent = "This product does not exist"
                textSpace.textContent = "Item Code:";
                textSpaceChanged = false;
                return;
            }
            let stock = document.getElementById(textSpace.textContent.concat("_stock"));
            stock = parseInt(stock.textContent);
            if (stock - 1 < 0){
                errorMessage.textContent = "We're are out of this item at the moment. Please check back soon."
                textSpace.textContent = "Item Code:";
                textSpaceChanged = false;
                return;
            }
            let cash = document.getElementById("money");
            cash = parseInt(cash.textContent);
            let price = document.getElementById(textSpace.textContent.concat("_price"));
            price = parseFloat(price.textContent.substring(1));
            let description = document.getElementById(textSpace.textContent.concat("_description"));
            if (cash - price < 0){
                errorMessage.textContent = "You don't have enough funds to purchase this item!"
                textSpace.textContent = "Item Code:";
                textSpaceChanged = false;
                return;
            }
            let dict = {
                        "name" : code.textContent,
                        "price" : price,
                        "description" : description.textContent
            }
            let dictstring = JSON.stringify(dict);

            let url = window.location.href;
            let post = {
                        "name" : code.textContent, 
                        "csrfmiddlewaretoken" : document.getElementById("token").textContent
            }
            let xhr = new XMLHttpRequest();
            xhr.open("POST", url);
            xhr.setRequestHeader("X-CSRFToken", document.getElementById("token").textContent)
            xhr.setRequestHeader("Accept", "application/json");
            xhr.setRequestHeader("Content-Type", "application/json");

            xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.responseText == '1'){
                    download(code.textContent.concat(".json"), dictstring);
                    cash.textContent = cash-price
                    document.getElementById(textSpace.textContent.concat("_stock")).textContent = (stock -1).toString() + " in stock";
                    document.getElementById("payment").textContent = "💰 " + currenyFormatter.format(cash-price).toString() +" 💰"
                    document.getElementById("money").textContent = currenyFormatter.format(cash-price).toString().substring(1)
                    errorMessage.textContent = "";
                    textSpace.textContent = "Item Code:";
                    textSpaceChanged = false;
                    successMessage.textContent = "Your download will start shortly";
                }
                else{
                    location.reload();
                    errorMessage.textContent = "Mismatch between client and server, reloading page...";
                }
            }};

            xhr.send(JSON.stringify(post));
        }
    }
}
