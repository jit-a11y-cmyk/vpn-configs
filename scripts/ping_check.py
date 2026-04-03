import json
import socket

def check_host(ip, port=443):
    try:
        # Пробуем подключиться к порту за 3 секунды
        socket.create_connection((ip, port), timeout=3)
        return "online"
    except:
        return "offline"

# Читаем твой vpn.txt
try:
    with open('vpn.txt', 'r') as f:
        config_lines = f.readlines()
except:
    config_lines = []

status_results = []

for line in config_lines:
    if "@" in line and ":" in line:
        # Пытаемся достать IP из ссылки vless://... @1.2.3.4:443...
        parts = line.split('@')[1].split(':')
        ip = parts[0]
        # Проверяем и добавляем в список
        res = check_host(ip)
        status_results.append({"ip": ip, "status": res})

# Сохраняем результат в файл для сайта
with open('status.json', 'w') as f:
    json.dump(status_results, f, indent=2)
  
