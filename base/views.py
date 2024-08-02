from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def bfhl(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            numbers = [item for item in data['data'] if item.isdigit()]
            alphabets = [item for item in data['data'] if item.isalpha()]
            highest_alphabet = max(alphabets, key=str.lower) if alphabets else []
            response_data = {
                "is_success": True,
                "user_id": "john_doe_17091999",
                "email": "john@xyz.com",
                "roll_number": "ABCD123",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": [highest_alphabet] if highest_alphabet else []
            }
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({"is_success": False, "error": str(e)}, status=400)
    else:
        return JsonResponse({"operation_code": 1})

def frontend(request):
    return render(request, 'base/frontend.html')
