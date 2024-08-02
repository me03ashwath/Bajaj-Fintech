from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def bfhl(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            response = {
                "is_success": True,
                "user_id": "john_doe_17091999",
                "email": "john@xyz.com",
                "roll_number": "ABCD123",
                "numbers": [],
                "alphabets": [],
                "highest_alphabet": []
            }
            numbers = []
            alphabets = []
            for item in data.get("data", []):
                if item.isdigit():
                    numbers.append(item)
                elif item.isalpha():
                    alphabets.append(item)

            response["numbers"] = numbers
            response["alphabets"] = alphabets
            if alphabets:
                response["highest_alphabet"] = [max(alphabets, key=lambda x: x.upper())]
            
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"is_success": False, "error": str(e)}, status=400)
    elif request.method == 'GET':
        return JsonResponse({"operation_code": 1})
    else:
        return JsonResponse({"error": "Invalid HTTP method"}, status=405)
