
from pyscript import document


def generate_sku(event):
    category = document.getElementById("category").value
    product = document.getElementById("product").value
    stock = document.getElementById("stock").value

    sku = category + "-" + product + "-" + stock

    document.getElementById("sku").innerText = "SKU: " + sku