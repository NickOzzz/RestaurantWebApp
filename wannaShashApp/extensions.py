from .models import ShashlikNaUgliach, Assorti, MiasnoiAssorti, Shawerma, Emails
from django.core.mail import send_mail

def retrieve_token(item):
    return item.partition("itemId")[2]

def get_item_name(items, item_id):
    item_name = "None"
    for item in items:
        if int(item_id) == item["itemId"]:
            item_name = item["itemName"]
    return item_name

def adjust_and_get_item_count(cookies, token, item_tracker, items_to_change):
    counter = 1
    if cookies["itemId" + token] in item_tracker:
        for item in items_to_change:
            if item["id"] == cookies["itemId" + token]:
                counter = item["counter"]
                del items_to_change[items_to_change.index(item)]
                counter += 1
                break
    return counter

def send_order_email(request, total_price, items):
    if request.POST.get("order-delivery"):
        send_email_with_delivery(request, items, total_price)
        return True
    elif request.POST.get("order-self"):
        send_email_without_delivery(request, items, total_price)
        return True
    return False

def send_email_without_delivery(request, items, total_price):
    emails = Emails.objects.all()[0]
    username = request.POST.get("userName2")
    user_phone = request.POST.get("usePhone2")
    send_mail(
        "Новый заказ!",
        f"Заказ без доставки от '{username}'"
        f"\n\nТелефон: {user_phone}"
        f"\n\n{beautify_items(items)}"
        f"\n\nВсего: {total_price} руб",
        emails.Sender, [emails.Receiver], fail_silently=True
    )

def send_email_with_delivery(request, items, total_price):
    emails = Emails.objects.all()[0]
    username = request.POST.get("userName")
    user_phone = request.POST.get("usePhone")
    user_place = request.POST.get("userPlace")
    send_mail(
        "Новый заказ!",
        f"Заказ c доставкой от '{username}'"
        f"\n\nТелефон: {user_phone}"
        f"\n\nДоставка до '{user_place}'"
        f"\n\n{beautify_items(items)}"
        f"\n\nВсего: "
        f"\nЗа продукты: {total_price} руб",
        emails.Sender, [emails.Receiver], fail_silently=True
    )

def retrieve_list_of_item_id_and_item_name_of_each_item():
    return [{"itemName": x.Name, "itemId": x.itemId } for x in Shawerma.objects.all()]\
           + [{"itemName": x.Name, "itemId": x.itemId } for x in MiasnoiAssorti.objects.all()]\
           + [{"itemName": x.Name, "itemId": x.itemId } for x in Assorti.objects.all()]\
           + [{"itemName": x.Name, "itemId": x.itemId } for x in ShashlikNaUgliach.objects.all()]

def set_list_of_item_dictionaries_with_order(items):
    dicts_of_items = list()
    counter = 0
    for item in items:
        set_of_items = {}
        counter+=1
        set_of_items.update({"order": counter})
        set_of_items.update({"Name": item.Name})
        set_of_items.update({"Description": item.Description})
        set_of_items.update({"Price": item.Price})
        set_of_items.update({"Price": item.Price})
        set_of_items.update({"image": item.image})
        dicts_of_items.append(set_of_items)
        if counter == 3: counter = 0
    return dicts_of_items

def beautify_items(items):
    initial = ""
    for item in items:
        initial += f'-------' \
                   f'\nПродукт: {item["name"]}' \
                   f'\nЦена: {item["price"]} руб' \
                   f'\nКоличество: {item["amount"]}' \
                   f'\n-------'
    return initial