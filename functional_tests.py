from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):
    ''' тест нового посетителя '''

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def checking_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        ''' тест: можно начать список и получить его позже '''
        self.browser.get('http://localhost:8000')
        # Чек шапки на страницу неотложных дел
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Купить павлиньи перья')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.checking_for_row_in_list_table('1: Купить павлиньи перья')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сфарганить чучело из перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.checking_for_row_in_list_table('1: Купить павлиньи перья')
        self.checking_for_row_in_list_table('2: Сфарганить чучело из перьев')

        # self.assertTrue(
        #     any(
        #         row.text == '1: Купить павлиньи перья' for row in rows),
        #     f'Не появился новый элемент списка в таблице. Содержимое:{table.text}',
        # )

        self.fail('Закончить тест!')



if __name__ == '__main__':
    unittest.main(warnings='ignore')
