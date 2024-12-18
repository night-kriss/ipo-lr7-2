import json

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def find_qualification(data, qualification_number):
    results = []
    for item in data:
        if item['model'] == 'data.skill' and qualification_number in item['fields']['code']:
            results.append(item)
    return results

def main():
    filename = 'dump.json'  # Укажите правильный путь к вашему файлу
    data = load_data(filename)
    
    qualification_number = input("Введите номер квалификации: ")
    results = find_qualification(data, qualification_number)
    
    if results:
        print("=============== Найдено ===============")
        for result in results:
            print(f"{result['fields']['code']} >> {result['fields']['title']}")
    else:
        print("=============== Не найдено ===============")

if __name__ == "__main__":
    main()
