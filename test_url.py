# ============================================================
# PASO 5: Verificar la API desplegada
# ============================================================

import requests
import json

# TODO 13: Cambia esta URL por la URL de TU API desplegada
BASE_URL = 'https://nubank-deploy-ml.onrender.com'

print(f'Probando API en: {BASE_URL}')
print('=' * 50)

# --- Verificar que la API responde ---
try:
    response = requests.get(f'{BASE_URL}/health', timeout=60)
    print(f'Health check: {response.status_code}')
    print(json.dumps(response.json(), indent=2))
except requests.exceptions.Timeout:
    print('⚠️  Timeout: El servicio puede estar en cold start. Espera 30 segundos y vuelve a intentarlo.')
except Exception as e:
    print(f'❌ Error: {e}')

print()



test_cases = [
    {
        'description': 'Iris setosa',
        'data': {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2}
    },
    {
        'description': 'Iris versicolor',
        'data': {'sepal_length': 7.0, 'sepal_width': 3.2, 'petal_length': 4.7, 'petal_width': 1.4}
    },
    {
        'description': 'Iris virginica',
        'data': {'sepal_length': 6.3, 'sepal_width': 3.3, 'petal_length': 6.0, 'petal_width': 2.5}
    },
]

print(f'Probando predicciones en: {BASE_URL}/predict')
print('=' * 50)

for test in test_cases:
    print(f"\n--- {test['description']} ---")
    try:
        response = requests.post(
            f'{BASE_URL}/predict',
            json=test['data'],
            timeout=60
        )
        print(f'Status: {response.status_code}')
        result = response.json()
        print(json.dumps(result, indent=2))
        # Verificar que la predicción es correcta
        expected = test['description'].split()[-1].lower()  # 'setosa', 'versicolor' o 'virginica'
        predicted = result.get('prediction', '').lower()
        ok = '✅' if predicted == expected else '❌'
        print(f'{ok} Esperado: {expected} | Predicho: {predicted}')
    except Exception as e:
        print(f'❌ Error: {e}')

# --- Verificar el endpoint raíz ---
try:
    response = requests.get(f'{BASE_URL}/', timeout=60)
    print(f'Endpoint raíz: {response.status_code}')
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f'❌ Error: {e}')