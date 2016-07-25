# -*- coding: utf-8 -*-

from django.test import TestCase
from accounts.models import Client, Employee
from django.contrib.auth.models import User

class AccountsTestCase(TestCase):
    def create_user(self, model, login, mail, password, l_name, 
            f_name, active):
        user = User.objects.create_user(login, mail, password)
        user.last_name = l_name
        user.first_name = f_name
        user.is_active = active
        user.save()
        if model == "employee":
            Employee.objects.create(account=user, telephone="123456789",
                    address="Null", contract_begin="3020-12-12")
        else:
            Client.objects.create(account=user, telephone="123456789",
                    address="Null")
    
    def setUp(self):
        # wonder woman is client
        self.create_user("client", "wonder", "wonder@woman.wo", "gotham",
                "Prince", "Diana", True)
        # Jessica Jones is worker
        self.create_user("employee", "jess", "jessie@detecti.ve", "kilgrave",
                "Jones", "Jessica", True)

    def test_get_user_by_name(self):
        user = User.objects.get(username="jess")
        self.assertEqual(user.last_name, "Jones")

    def test_get_client_from_user(self):
        user = User.objects.get(username="wonder")
        client = Client.objects.get(address="Null")
        self.assertEqual(user.client, client)
        self.assertEqual(user, client.account)

    def test_get_employee_from_user(self):
        user = User.objects.get(username="jess")
        employee = Employee.objects.get(address="Null")
        self.assertEqual(user.employee, employee)
        self.assertEqual(user, employee.account)
