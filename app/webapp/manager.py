def if_number(a, b):
    response_data = {}
    try:
        float(a)
        float(b)
        return False, response_data
    except ValueError:
        response_data = {'error': "Введены некорректные значения. Введите числа"}
        return True, response_data


def get_numbers(request):
    if request.method == 'POST' and request.body:
        a = request.POST.get('A')
        b = request.POST.get('B')
        return a, b
