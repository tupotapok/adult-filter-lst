import json

# Чтение итогового списка доменов
with open('adult.lst', 'r', encoding='utf-8') as f:
    domains = [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Формирование структуры JSON для sing-box
rule_set = {
    "version": 1,
    "rules": [
        {
            "domain_suffix": domains
        }
    ]
}

# Сохранение в adult.json
with open('adult.json', 'w', encoding='utf-8') as f:
    json.dump(rule_set, f, indent=2)
