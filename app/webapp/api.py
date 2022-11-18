from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse

from webapp.manager import if_number, get_numbers


def add(request: WSGIRequest, *args, **kwargs):
    a, b = get_numbers(request)
    wrong_request, response_data = if_number(a, b)

    if wrong_request:
        response = JsonResponse(response_data)
    else:
        response_data = {
            'answer': round((float(a) + float(b)), 2)
        }
        response = JsonResponse(response_data)
        response.status_code = 201
    return response


def subtract(request: WSGIRequest, *args, **kwargs):
    a, b = get_numbers(request)
    wrong_request, response_data = if_number(a, b)

    if wrong_request:
        response = JsonResponse(response_data)
        response.status_code = 400
    else:
        response_data = {
            'answer': round((float(a) - float(b)), 2)
        }
        response = JsonResponse(response_data)
        response.status_code = 201
    return response


def multiply(request: WSGIRequest, *args, **kwargs):
    a, b = get_numbers(request)
    wrong_request, response_data = if_number(a, b)

    if wrong_request:
        response = JsonResponse(response_data)
        response.status_code = 400
    else:
        response_data = {
            'answer': round((float(a) * float(b)), 2)
        }
        response = JsonResponse(response_data)
        response.status_code = 201
    return response


def divide(request: WSGIRequest, *args, **kwargs):
    a, b = get_numbers(request)
    wrong_request, response_data = if_number(a, b)

    if wrong_request:
        response = JsonResponse(response_data)
    elif b == 0:
        response_data = {
            'error': "Division by zero!"
        }
        response = JsonResponse(response_data)
        response.status_code = 400
    else:
        response_data = {
            'answer': round((float(a) / float(b)), 2)
        }
        response = JsonResponse(response_data)
        response.status_code = 201
    return response
