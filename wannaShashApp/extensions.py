from .models import ShashlikNaUgliach, Assorti, MiasnoiAssorti, Shawerma, Emails
from django.core.mail import send_mail

def retrieve_token(item):
    return item.partition("itemId")[2]

def get_name(list_of_lists, item_id):
    name = "None"
    for i in list_of_lists:
        if int(item_id) == i["itemId"]:
            name = i["itemName"]
    return name

def send_email_without_delivery(request, items, total_price):
    emails = Emails.objects.all()[0]
    username = request.POST.get("userName2")
    user_phone = request.POST.get("usePhone2")
    send_mail(
        "Новый заказ!",
        f"Заказ без доставки от '{username}'"
        f"\n\nТелефон: {user_phone}"
        f"\n\n{beautify(items)}"
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
        f"\n\n{beautify(items)}"
        f"\n\nВсего: "
        f"\nЗа продукты: {total_price} руб",
        emails.Sender, [emails.Receiver], fail_silently=True
    )

def retrieve_list_item_id_and_item_name_of_each_item():
    return [{"itemName": x.Name, "itemId": x.itemId } for x in Shawerma.objects.all()]\
           + [{"itemName": x.Name, "itemId": x.itemId } for x in MiasnoiAssorti.objects.all()]\
           + [{"itemName": x.Name, "itemId": x.itemId } for x in Assorti.objects.all()]\
           + [{"itemName": x.Name, "itemId": x.itemId } for x in ShashlikNaUgliach.objects.all()]

def set_dictionary_with_order(items):
    list_of_items = list()
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
        list_of_items.append(set_of_items)
        if counter == 3: counter = 0
    return list_of_items

def beautify(items):
    initial = ""
    for i in items:
        initial += f'-------' \
                   f'\nПродукт: {i["name"]}' \
                   f'\nЦена: {i["price"]} руб' \
                   f'\nКоличество: {i["amount"]}' \
                   f'\n-------'
    return initial