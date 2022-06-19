(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

const buttons = document.querySelectorAll(".keypad-button");
const textSpace = document.querySelector("#text-space");
const errorMessage = document.querySelector("#error-message");
var textSpaceChanged = false;

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
            if (cash - price < 0){
                errorMessage.textContent = "You don't have enough funds to purchase this item!"
                textSpace.textContent = "Item Code:";
                textSpaceChanged = false;
                return;
            }
            errorMessage.textContent = "";
            textSpace.textContent = "Item Code:";
            textSpaceChanged = false;
        }
    }
}
