import json

from homeworks_7_8_9_10_demo_qa.demo_qa_pages.radio_button_page import PageRadioButton


class TestRadioButtons:

    def test_radio_buttons(self, chrome):
        page = PageRadioButton(driver=chrome)
        page.open()
        # page.select_yes_button()
        # page.select_impressive_button()
        page.enable_no_button()
        page.select_no_button()

        # Перевірка, чи обрана (клікнута) кнопка "Yes"
        is_yes_button_selected = page.is_yes_button_selected()
        is_yes_button_enabled = page.is_yes_button_enabled()

        # Перевірка, чи обрана (клікнута) кнопка "Impressive"
        is_impressive_button_selected = page.is_impressive_button_selected()
        is_impressive_button_enabled = page.is_impressive_button_enabled()

        # Перевірка, чи обрана (клікнута) кнопка "No"
        is_no_button_selected = page.is_no_button_selected()
        is_no_button_enabled = page.is_no_button_enabled()

        dct = {
            'Yes': {
                'is_selected': is_yes_button_selected,
                'is_enabled': is_yes_button_enabled
            },
            'Impressive': {
                'is_selected': is_impressive_button_selected,
                'is_enabled': is_impressive_button_enabled
            },
            'No': {
                'is_selected': is_no_button_selected,
                'is_enabled': is_no_button_enabled
            }
        }

        # Запис результату у файл
        with open('../demo_qa_pages/result_radio_button.json', 'w') as file:
            json.dump(dct, file, indent=4)
