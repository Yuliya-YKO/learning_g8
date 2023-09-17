# Імпортуємо бібліотеку etree з бібліотеки lxml для роботи з XML
from lxml import etree

# Створюємо словник test_dict з вмістом, який ми хочемо перетворити у формат XML
test_dict = {
    'user1': {'gender': 'm',
              'firstname': 'Vasya',
              'lastname': 'Pupkin',
              'age': 20},
    'user2': {'gender': 'f',
              'firstname': 'Vasilisa',
              'lastname': 'Pupkina',
              'age': 21}
}

# Створюємо кореневий елемент XML з іменем 'users'
root = etree.Element('users')

# Проходимося по словнику test_dict та додаємо елементи до XML
for username, user_data in test_dict.items():
    user_element = etree.SubElement(root, 'user', username=username)
    for key, value in user_data.items():
        etree.SubElement(user_element, key).text = str(value)

# Створюємо дерево XML з кореневим елементом
tree = etree.ElementTree(root)

# Зберігаємо дерево XML у файл 'users.xml', використовуючи красиве форматування (pretty_print)
tree.write('users.xml', pretty_print=True, encoding='utf-8')


# Імпортуємо бібліотеку ElementTree з xml.etree для роботи з XML
import xml.etree.ElementTree as ET

# Відкриваємо XML-файл 'users.xml' для читання та розпарсюємо його
tree = ET.parse('users.xml')
root = tree.getroot()

# Створюємо пустий словник parsed_dict
parsed_dict = {}

# Проходимося по елементах 'user' у XML і дістаємо дані
for user_element in root.findall('user'):
    username = user_element.get('username')
    user_data = {}

    for element in user_element:
        user_data[element.tag] = element.text

    parsed_dict[username] = user_data

# Виводимо отриманий словник parsed_dict
print(parsed_dict)


# Імпортуємо бібліотеку json для роботи з JSON
import json

# Зберігаємо словник test_dict у JSON-файл 'users.json'
with open('users.json', 'w') as json_file:
    json.dump(test_dict, json_file, indent=4)

# Відкриваємо JSON-файл 'users.json' для читання та завантажуємо його у словник _json_dict
with open('users.json', 'r') as json_file:
    _json_dict = json.load(json_file)

# Виводимо отриманий словник _json_dict
print(_json_dict)


# Знову відкриваємо XML-файл 'users.xml' для читання та розпарсюємо його
tree = ET.parse('users.xml')
root = tree.getroot()

# Створюємо пустий словник parsed_dict
parsed_dict = {}

# Проходимося по елементах 'user' у XML і дістаємо дані
for user_element in root.findall('user'):
    username = user_element.get('username')
    user_data = {}

    for element in user_element:
        user_data[element.tag] = element.text

    parsed_dict[username] = user_data

# Зберігаємо отриманий словник parsed_dict у JSON-файл 'users_converted.json'
with open('users_converted.json', 'w') as json_file:
    json.dump(parsed_dict, json_file, indent=4)
