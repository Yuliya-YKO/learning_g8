from datetime import time

from selenium_lecture.pages.page_text_box import PageTextBox


def test_text_box_set_fullname(chrome):
    page = PageTextBox(driver=chrome)
    for y in range(301, 700):
        page.open()
        chrome.implicitly_wait(10)
        page.set_email(f'surko{y}@gmail.com')
        page.set_full_name(fullname='hgghh')
        page.set_current_address('dhfgk')
        page.select_button_by_locator()
        page.select_button_by_locator2()
        page.submit()
        chrome.implicitly_wait(10)

    # page.click_button_by_name('Submit')


# def test_text_1(chrome):
#     expected_result = 'pupkin@mail.com'
#     page = PageTextBox(driver=chrome)
#     page.open()
#     page.set_email('pupkin@mail.com')
#     page.submit()
#     result_email = page.get_result_email()
#     assert result_email == expected_result
