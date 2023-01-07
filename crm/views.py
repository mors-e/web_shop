from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import send_telegram


# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()

    price_card_1 = PriceCard.objects.get(pk=1)
    price_card_2 = PriceCard.objects.get(pk=2)
    price_card_3 = PriceCard.objects.get(pk=3)

    price_table = PriceTable.objects.all()

    form = OrderForm()

    dict_objects = {'slider_list': slider_list,
                    'price_card_1': price_card_1,
                    'price_card_2': price_card_2,
                    'price_card_3': price_card_3,
                    'price_table': price_table,
                    'form': form
                    }
    return render(request, './index.html', dict_objects)


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    send_telegram(telegram_name=name, telegram_phone=phone)
    return render(request, './thanks.html', {'name': name,
                                             'phone': phone
                                             })
