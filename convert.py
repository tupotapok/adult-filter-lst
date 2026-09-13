import json
import os

# Проверяем, существует ли файл
if not os.path.exists('adult.lst'):
    print("Файл adult.lst не найден!")
    exit(1)

# Читаем домены
with open('adult.lst', 'r') as f:
    domains = [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Формируем структуру правила для sing-box
rule_set = {
    "version": 1,
    "rules": [
        {
            "domain_suffix": domains
        }
    ]
}

# Сохраняем в JSON
with open('adult.json', 'w') as f:
    json.dump(rule_set, f, indent=2)
