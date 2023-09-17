
# Завдання 1: Збереження словника у форматі XML: Конвертуйте словник у формат XML та збережіть його у файл з розширенням ".xml".

from lxml import etree

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


root = etree.Element('users')


for username, user_data in test_dict.items():
    user_element = etree.SubElement(root, 'user', username=username)
    for key, value in user_data.items():
        etree.SubElement(user_element, key).text = str(value)


tree = etree.ElementTree(root)
tree.write('users.xml', pretty_print=True, encoding='utf-8')

#  Завдання 2: Читання XML-файлу: Відкрийте XML-файл та розпарсіть його, щоб отримати знову словник Python як оригінал.

import xml.etree.ElementTree as ET


tree = ET.parse('users.xml')
root = tree.getroot()


parsed_dict = {}


for user_element in root.findall('user'):
    username = user_element.get('username')
    user_data = {}

    for element in user_element:
        user_data[element.tag] = element.text

    parsed_dict[username] = user_data

print(parsed_dict)

# Завдання 3: Збереження словника у форматі JSON: Конвертуйте словник у формат JSON та збережіть його у файл з розширенням ".json".

import json

with open('users.json', 'w') as json_file:
    json.dump(test_dict, json_file, indent=4)

# Завдання 4: Читання JSON-файлу: Відкрийте JSON-файл та завантажте його дані у Python як словник.

import json

with open('users.json', 'r') as json_file:
    _json_dict = json.load(json_file)

print(_json_dict)

# Завдання 5: Конвертація з XML до JSON: Завантажте XML-файл, розпарсіть його та конвертуйте у формат JSON. Потім збережіть в файл.

tree = ET.parse('users.xml')
root = tree.getroot()

parsed_dict = {}

for user_element in root.findall('user'):
    username = user_element.get('username')
    user_data = {}

    for element in user_element:
        user_data[element.tag] = element.text

    parsed_dict[username] = user_data

with open('users_converted.json', 'w') as json_file:
    json.dump(parsed_dict, json_file, indent=4)


