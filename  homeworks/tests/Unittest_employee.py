import unittest
from unittest.mock import Mock,patch
from employee import Employee

Human1 = Employee("Ruslan", "Ihnatenko", 1000)
Human2 = Employee("Petro", "Romanenko", 50000)


class EmployeeTest(unittest.TestCase):
    def test_email_func(self):
        self.assertEqual(Human1.email, "Ruslan.Ihnatenko@email.com")
        self.assertEqual(Human2.email, "Petro.Romanenko@email.com")

    def test_fullname_func(self):
        self.assertEqual(Human1.fullname, "Ruslan Ihnatenko")
        self.assertEqual(Human2.fullname, "Petro Romanenko")

    def test_apply_raise_func(self):
        Human1.apply_raise()
        self.assertEqual(Human1.pay, 1050)
        Human2.apply_raise()
        self.assertEqual(Human2.pay, 52500)

    def test_monthly_schedule_func(self):
        human3 = Employee("Denys", "Gordon", 9000)
        with patch('employee.requests.get') as mock_requests:
            mock_requests.return_value.ok = True
            self.assertNotEqual(human3.monthly_schedule('May'), 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
