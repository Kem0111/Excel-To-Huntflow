import unittest
from src.xlsx_parser import pars_exel_file


class TestExcelParser(unittest.TestCase):
    def test_pars_exel_file(self):
        # Arrange
        expected_output = [
            {
                'last_name': 'Глибин',
                'first_name': 'Виталий',
                'middle_name': 'Николаевич',
                'money': '150000 рублей',
                'position': 'Frontend-разработчик',
                'status': 'Отправлено письмо',
                'comment': 'Нужно звать на собеседование'
            },
            {
                'last_name': 'Танский',
                'first_name': 'Михаил',
                'money': '120 000',
                'position': 'Frontend-разработчик',
                'status': 'Интервью с HR',
                'comment': 'Какой-то странный, но нужно поговорить'
            },
            {
                'last_name': 'Корниенко',
                'first_name': 'Максим',
                'money': 80000,
                'position': 'Менеджер по продажам',
                'status': 'Выставлен оффер',
                'comment': 'Классный'
            },
            {
                'last_name': 'Шорин',
                'first_name': 'Андрей',
                'money': 200000,
                'position': 'Менеджер по продажам',
                'status': 'Отказ',
                'comment': 'Очень дорогой'
            },
        ]

        # Act
        result = pars_exel_file('tests/fixtures/testdb.xlsx')

        # Assert
        self.assertEqual(result, expected_output)
