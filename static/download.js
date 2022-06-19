
let price  = document.getElementById("price");
let name = document.getElementById("name");
let description = document.getElementById("description");
let dict = {
    "name" : name.textContent,
    "price" : price.textContent,
    "description" : description.textContent
}


function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}



let dictstring = JSON.stringify(dict);
download(name.textContent.concat(".json"), dictstring);

window.location.href = "/";
