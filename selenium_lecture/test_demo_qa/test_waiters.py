from homeworks_7_8_9_10_demo_qa.conftest import chrome
from homeworks_7_8_9_10_demo_qa.demo_qa_pages.Dynamic_page_waiters import DynamicProperties


class TestDynamicProperties:

    def test_1dp(self, chrome):
        page = DynamicProperties(driver=chrome)
        page.open()

    def test_2dp(self, chrome):
        page = DynamicProperties(driver=chrome)
        page.open()
        _id = page.get_enable_after_button_attribute('id')
        print(_id)
        pass


    def test_3dp(chrome):
        page = DynamicProperties(driver=chrome)
        page.open()
        element = page.get_enable_after_button_element()
        is_element_enabled = element.is_enabled()
        assert is_element_enabled
        pass

