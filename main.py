filename = 'dump.json'  # Укажите правильный путь к вашему файлу

# Загрузка данных из файла
with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Ввод номера квалификации
qualification_number = input("Введите номер квалификации: ")

# Поиск квалификации
results = []
for item in data:
    if item['model'] == 'data.skill' and qualification_number in item['fields']['code']:
        results.append(item)

# Вывод результатов
if results:
    print("=============== Найдено ===============")
    for result in results:
        print(f"{result['fields']['code']} >> {result['fields']['title']}")
else:
    print("=============== Не найдено ===============")

