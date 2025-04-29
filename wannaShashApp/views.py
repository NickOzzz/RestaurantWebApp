from django.shortcuts import render, redirect
from .models import ShashlikNaUgliach, Assorti, MiasnoiAssorti, Shawerma, SpacingMainPage, Costs
from wannaShashApp import extensions

#MainPage
def main_view(request):
    meat_assortments = MiasnoiAssorti.objects.all()
    shashlik_on_coal = ShashlikNaUgliach.objects.all()
    assortments = Assorti.objects.all()
    shawerma = Shawerma.objects.all()

    spacings = SpacingMainPage.objects.all()[0]
    costs = Costs.objects.all()[0]

    meat_assortments_count = len(meat_assortments)
    shashlik_on_coal_count = len(shashlik_on_coal)
    assortments_count = len(assortments)
    shawerma_count = len(shawerma)
    return render(request, "main/mainPage.html", {"meat_assortments": meat_assortments,
                                                  "shashlik_on_coal": shashlik_on_coal,
                                                  "assortments": assortments,
                                                  "shawerma": shawerma,
                                                  "spacings": spacings,
                                                  "costs": costs,
                                                  "meat_assortments_count": str(meat_assortments_count),
                                                  "shashlik_on_coal_count": str(shashlik_on_coal_count),
                                                  "assortments_count": str(assortments_count),
                                                  "shawerma_count": str(shawerma_count)})

#CartPage
def cart_view(request):
    #List of each item's id and name
    item_ids_and_names = extensions.retrieve_list_of_item_id_and_item_name_of_each_item()
    #List of items to be rendered
    final_items = list()
    #List to track repeating items to merge them into one
    item_tracker = list()

    cookie_items = request.COOKIES
    total_price = 0

    #Setting list of items
    for cookie_item in cookie_items:

        #Set total price based on all of the items
        if "itemPrice" in cookie_item:
            token = cookie_item.partition("itemPrice")[2]
            total_price += int(cookie_items["itemPrice" + token])

        #Merge repeating items into one and retrieve token
        if "itemId" in cookie_item:
            token = extensions.retrieve_token(cookie_item)
            counter = extensions.adjust_and_get_item_count(cookie_items, token, item_tracker, final_items)

            #Retrieve item id and add it to tracker
            item_id = cookie_items["itemId" + token]
            item_tracker.append(item_id)

            name = extensions.get_item_name(item_ids_and_names, item_id)

            #Set list of items from all
            final_items.append({"itemName": name,
                                  "itemDescription": cookie_items["itemDescription" + token],
                                  "itemPrice": cookie_items["itemPrice" + token],
                                  "imageUrl": cookie_items["imageUrl" + token],
                                  "counter": counter,
                                  "id": item_id,
                                  "token": token})

    order_sent = False
    #If button is pressed in form with post method, send a delivery email and redirect to success page
    if request.method == "POST":
        items_to_send = []
        for item in final_items:
            items_to_send.append({"name": item["itemName"], "price": item["itemPrice"], "amount": item["counter"]})
        order_sent = extensions.send_order_email(request, total_price, items_to_send)

    if order_sent:
        return redirect("/success/")

    return render(request, "main/cartPage.html", {"list_of_items": final_items,
                                                  "total_price": total_price})

#SuccessPage
def success(request):
    return render(request, "main/successPage.html")
