from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get("bag", {})
    # prevents direct access from the page top bar
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse("products"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51Mzh6nK0F9yAasNPCBArpbuga6LTECX18E4nSeOeB6WWNJhzs8LMIO3aGxh05LKAvgMMEGtdLpaQAmkahrcVjTWk00Q0eanRkr",
        "client_secret": "sk_test_51Mzh6nK0F9yAasNP481YBBKypenfQmWg0QvKmAYCzbfFBkPAr9S0fty4E2VAeadPjsN0RYAZi6DmZGa5pctOUgGo00Qd6CRkqA",
    }

    return render(request, template, context)
