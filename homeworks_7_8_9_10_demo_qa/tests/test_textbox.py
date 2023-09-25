from homeworks_7_8_9_10_demo_qa.demo_qa_pages.demo_text_box_page import PageObjectTextBox


def test_textbox_set_name(chrome):
    page = PageObjectTextBox(driver=chrome)
    page.open()
    page.set_full_name("Yuliya")
    page.set_email("yko.koty7@gmail.com")
    page.set_curr_addr("Ukrainka sity")
    page.set_perm_addr("Stroiteley")
    page.submit_button()

def test_textbox(chrome):
    expected_result = 'Yuliya'
    page = PageObjectTextBox(driver=chrome)
    page.open()
    page.set_full_name('Yuliya')
    page.submit_button()
    result_name = page.get_result_name()
    assert result_name == expected_result