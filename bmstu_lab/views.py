from django.shortcuts import render
from django.http import HttpResponse

from datetime import date 


ORDERS = {'data' : {
        'current_date': date.today(),
        'orders': [
            {'id': 1, 'name': 'Заказ 1', 'price': 5000},
            {'id': 2, 'name': 'Заказ 2', 'price': 10000},
            {'id': 3, 'name': 'Заказ 3', 'price': 20000},
            {'id': 4, 'name': 'Заказ 4', 'price': 40000},
            {'id': 5, 'name': 'Заказ 5', 'price': 60000},
        ]
    }}
data_vmachines = {
        'vmachines': [
    {'id': 1, 'name': 'HP C1-M1-D10', 'price': 480, 'description': 'Для выполнения кода сервисов и приложений, размещения интернет-магазинов и развертывания тестовых сред.', 'vCPU': '1 ядро', 'RAM': '1 ГБ', 'SSD': '10 ГБ', 'url': 'http://127.0.0.1:9000/vmachines/1.jpg', 'description_tech': 'Компактный виртуальный сервер с 1 ядром vCPU (2.5 ГГц), 1 ГБ DDR4, 10 ГБ SSD, подходит для тестовых сред и небольших приложений.'},
    {'id': 2, 'name': 'HP C2-M4-D80', 'price': 2260, 'description': 'Для выполнения кода сервисов и приложений, размещения интернет-магазинов и развертывания тестовых сред.', 'vCPU': '2 ядра', 'RAM': '4 ГБ', 'SSD': '80 ГБ', 'url': 'http://127.0.0.1:9000/vmachines/2.jpg', 'description_tech': 'Сбалансированный сервер с 2 ядрами vCPU (2.5 ГГц), 4 ГБ DDR4, 80 ГБ SSD, отлично подходит для средних приложений и тестов.'},
    {'id': 3, 'name': 'HP C4-M32-D200', 'price': 10245, 'description': 'Для выполнения кода сервисов и приложений, размещения интернет-магазинов и развертывания тестовых сред.', 'vCPU': '4 ядра', 'RAM': '32 ГБ', 'SSD': '200 ГБ', 'url': 'http://127.0.0.1:9000/vmachines/3.jpg', 'description_tech': 'Мощный сервер с 4 ядрами vCPU (2.5 ГГц), 32 ГБ DDR4, 200 ГБ SSD, предназначен для крупных приложений и сервисов.'},
    {'id': 4, 'name': 'HP C1-M0.5-D5', 'price': 248, 'description': 'Для хостинга сайтов, запуска стейджинга и мониторинга.', 'vCPU': '1 ядро', 'RAM': '0.5 ГБ', 'SSD': '5 ГБ', 'url': 'http://127.0.0.1:9000/vmachines/4.jpg', 'description_tech': 'Экономичный сервер с 1 ядром vCPU (2.5 ГГц), 0.5 ГБ DDR4, 5 ГБ SSD, идеально подходит для небольших сайтов и тестов.'},
    {'id': 5, 'name': 'HP C2-M2-D40', 'price': 738, 'description': 'Для хостинга сайтов, запуска стейджинга и мониторинга.', 'vCPU': '2 ядра', 'RAM': '2 ГБ', 'SSD': '40 ГБ', 'url': 'http://127.0.0.1:9000/vmachines/5.jpg', 'description_tech': 'Универсальный сервер с 2 ядрами vCPU (2.5 ГГц), 2 ГБ DDR4, 40 ГБ SSD, подходит для веб-приложений и хостинга сайтов.'},
    {'id': 6, 'name': 'HP C4-M8-D80', 'price': 2439, 'description': 'Для хостинга сайтов, запуска стейджинга и мониторинга.', 'vCPU': '4 ядра', 'RAM': '8 ГБ', 'SSD': '80 ГБ', 'url': 'http://127.0.0.1:9000/vmachines/6.jpg', 'description_tech': 'Надежный сервер с 4 ядрами vCPU (2.5 ГГц), 8 ГБ DDR4, 80 ГБ SSD, подходит для многозадачных приложений и веб-проектов.'},
    {'id': 7, 'name': 'HP C8-M32-D256', 'price': 18901, 'description': 'Для 3D-моделирования, рендеринга, ML и аналитики.', 'vCPU': '8 ядер', 'RAM': '32 ГБ', 'SSD': '256 ГБ', 'url': 'http://127.0.0.1:9000/vmachines/7.jpg', 'description_tech': 'Высокопроизводительный сервер с 8 ядрами vCPU (2.5 ГГц), 32 ГБ DDR4, 256 ГБ SSD, подходит для задач требующих больших вычислительных ресурсов.'},
    {'id': 8, 'name': 'HP C12-M64-D512', 'price': 28317, 'description': 'Для 3D-моделирования, рендеринга, ML и аналитики.', 'vCPU': '12 ядер', 'RAM': '64 ГБ', 'SSD': '512 ГБ', 'url': 'http://127.0.0.1:9000/vmachines/8.jpg', 'description_tech': 'Мощнейший сервер с 12 ядрами vCPU (2.5 ГГц), 64 ГБ DDR4, 512 ГБ SSD, идеально подходит для рендеринга и вычислительных задач.'},
    {'id': 9, 'name': 'HP C32-M180-D1024', 'price': 89315, 'description': 'Для 3D-моделирования, рендеринга, ML и аналитики.', 'vCPU': '32 ядра', 'RAM': '180 ГБ', 'SSD': '1024 ГБ', 'url': 'http://127.0.0.1:9000/vmachines/9.jpg', 'description_tech': 'Флагманский сервер с 32 ядрами vCPU (2.5 ГГц), 180 ГБ DDR4, 1024 ГБ SSD, подходит для масштабных вычислительных и аналитических задач.'},
]

    }

CARTS = {
    1: {'items': {1: 2, 8: 1}, 'total':3,'id':1},
    2: {'items': {2: 1, 4: 3},'total':4,'id':2},
    
}

def GetVmachines(request):
    max_price_str = request.GET.get('max_price', '100000')  # Значение по умолчанию 100000

    try:
        max_price = int(max_price_str)
    except ValueError:
        max_price = 100000  # Если значение не удалось преобразовать, используем значение по умолчанию

    # Функция для получения цены из строки или числа
    def parse_price(price):
        if isinstance(price, str):
            try:
                # Если цена строка, попробуем удалить возможные символы и преобразовать в число
                return int(price.replace(' ', '').replace('₽/мес', '').replace(',', ''))
            except ValueError:
                return 0
        elif isinstance(price, int):
            return price
        return 0

    # Фильтрация виртуальных машин по цене
    filtered_vmachines = [vmachine for vmachine in data_vmachines['vmachines'] if parse_price(vmachine['price']) <= max_price]

    context = {
        'vmachines': filtered_vmachines,
        'max_price': max_price,
        'cart_url': CARTS[1]
    }
    return render(request, 'vmachines.html', context)
def GetVmachine(request, id):
    
    vmachine = next((vmachine for vmachine in data_vmachines['vmachines'] if vmachine['id'] == id), None)
    
    if vmachine is None:
        return HttpResponse('Заказ не найден', status=404)
    context = {
        'vmachine': vmachine,  
        'data': {
            'vmachine': {'id': id},  
        },
        'cart_url': CARTS[1]
    }
    
    return render(request, 'vmachine.html', context
    )
def GetCart(request, id):
    
    cart = CARTS.get(id)
    
    if not cart:
        return HttpResponse('Корзина не найдена', status=404)
    
    
    items = []
    total_price = 0
    for vm_id, quantity in cart['items'].items():
        vmachine = next((vm for vm in data_vmachines['vmachines'] if vm['id'] == vm_id), None)
        if vmachine:
            vmachine_info = {
                'id': vmachine['id'],
                'name': vmachine['name'],
                'price': vmachine['price'],
                'quantity': quantity,
                'total': vmachine['price'] * quantity,
                'url': vmachine['url'],
            }
            items.append(vmachine_info)
            total_price += vmachine_info['total']
    
    # Контекст для отображения на странице
    context = {
        'vmachine_id': id,
        'items': items,
        'total_price': total_price
    }
    
    # Рендерим страницу с корзиной
    return render(request, 'vmachine-cart.html', context)