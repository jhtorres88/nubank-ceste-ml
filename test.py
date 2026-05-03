import requests
import json

BASE_URL = 'http://localhost:8000'

print('=== GET / ===')
try:
    response_root = requests.get(f'{BASE_URL}/')
    print(f"Status: {response_root.status_code}")
    print(json.dumps(response_root.json(), indent=2))
except Exception as e:
    print(f"Error en Prueba 1: {e}")

print('=== GET /health ===')
try:
    response_health = requests.get(f'{BASE_URL}/health')
    print(f"Status: {response_health.status_code}")
    print(json.dumps(response_health.json(), indent=2))
except Exception as e:
    print(f"Error en Prueba 2: {e}")

print('\n=== POST /predict (setosa) ===')
test_data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

try:
    response_predict = requests.post(f'{BASE_URL}/predict', json=test_data)
    print(f"Status: {response_predict.status_code}")
    print(json.dumps(response_predict.json(), indent=2))
except Exception as e:
    print(f"Error en Prueba 3: {e}")