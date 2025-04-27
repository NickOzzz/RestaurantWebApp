from django.shortcuts import render, redirect
from .models import ShashlikNaUgliach, Assorti, MiasnoiAssorti, Shawerma, SpacingMainPage, Costs
from wannaShashApp import extensions

#MainPage
def mainView(request):
    foods1 = MiasnoiAssorti.objects.all()
    foods2 = ShashlikNaUgliach.objects.all()
    foods3 = Assorti.objects.all()
    foods4 = Shawerma.objects.all()
    spacings = SpacingMainPage.objects.all()[0]
    costs = Costs.objects.all()[0]
    foods1count = len(foods1)
    foods2count = len(foods2)
    foods3count = len(foods3)
    foods4count = len(foods4)
    return render(request, "main/mainPage.html", {"foods1": foods1,
                                                  "foods2": foods2,
                                                  "foods3": foods3,
                                                  "foods4": foods4,
                                                  "spacings": spacings,
                                                  "costs": costs,
                                                  "foods1count": str(foods1count),
                                                  "foods2count": str(foods2count),
                                                  "foods3count": str(foods3count),
                                                  "foods4count": str(foods4count)})

#CartPage
def cartView(request):
    #List of each item's id and name
    list_of_lists = extensions.retrieve_list_item_id_and_item_name_of_each_item()
    #List of items to be rendered
    list_of_items = list()
    #List to track repeating items to merge them into one
    tracker = list()

    items = request.COOKIES
    total_price = 0

    #Setting list of items
    for item in items:

        #Set total price based on all of the items
        if "itemPrice" in item:
            token = item.partition("itemPrice")[2]
            total_price += int(request.COOKIES["itemPrice" + token])

        #Merge repeating items into one and retrieve token
        counter = 1
        if "itemId" in item:
            temporary_token = extensions.retrieve_token(item)
            if request.COOKIES["itemId" + temporary_token] in tracker:
                for ite in list_of_items:
                    if ite["id"] == request.COOKIES["itemId" + temporary_token]:
                        counter = ite["counter"]
                        del list_of_items[list_of_items.index(ite)]
                        counter += 1
                        break

            #Retrieve item id and add it to tracker
            item_id = request.COOKIES["itemId" + temporary_token]
            tracker.append(item_id)

            name = extensions.get_name(list_of_lists, item_id)

            #Set list of items from all
            list_of_items.append({"itemName": name,
                                  "itemDescription": request.COOKIES["itemDescription" + temporary_token],
                                  "itemPrice": request.COOKIES["itemPrice" + temporary_token],
                                  "imageUrl": request.COOKIES["imageUrl" + temporary_token],
                                  "counter": counter,
                                  "id": item_id,
                                  "token": temporary_token})

    #If button is pressed in form with post method, send an email and redirect to success page
    if request.method == "POST":
        items = []
        for item in list_of_items:
            items.append({"name": item["itemName"], "price": item["itemPrice"], "amount": item["counter"]})
        if request.POST.get("order-delivery"):
            extensions.send_email_with_delivery(request, items, total_price)
            return redirect("/success/")
        elif request.POST.get("order-self"):
            extensions.send_email_without_delivery(request, items, total_price)
            return redirect("/success/")

    return render(request, "main/cartPage.html", {"list_of_items": list_of_items,
                                                  "total_price": total_price})

#SuccessPage
def success(request):
    return render(request, "main/successPage.html")
