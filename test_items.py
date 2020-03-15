import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_search_button_add_to_basket(browser):
        browser.get(link)
        assert browser.find_element_by_css_selector("button.btn-add-to-basket"), "Нет кнопки: Добавить в корзину"