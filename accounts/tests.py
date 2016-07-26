# -*- coding: utf-8 -*-

from django.test import TestCase
from accounts.models import Client, Employee, Account
from django.contrib.auth.models import User

TELEPHONE = "123456789"

class AccountsTestCase(TestCase):

    def create_user(self, model, login, mail, password, l_name, 
            f_name, active):
        user = User.objects.create_user(login, mail, password)
        user.last_name = l_name
        user.first_name = f_name
        user.is_active = active
        user.save()
        if model == "employee":
            Employee.objects.create(account=user, telephone=TELEPHONE,
                    address="Null", contract_begin="3020-12-12")
        else:
            Client.objects.create(account=user, telephone=TELEPHONE,
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

    def test_create_employee(self):
        user = User.objects.create_user("charlie", "charlie@nassau.com",
                "Eleonora")
        employee_count = Employee.objects.count()
        employee = Employee.objects.create(account=user, telephone=TELEPHONE,
                address="Null", contract_begin="2020-12-12")
        self.assertEqual("charlie", employee.account.username)
        self.assertEqual(employee_count + 1, Employee.objects.count())

    def test_create_client(self):
        user = User.objects.create_user("james", "james@flint.uk", "miranda")
        client_count = Client.objects.count()
        client = Client.objects.create(account=user, telephone=TELEPHONE,
                address="Sea")

        self.assertEqual("james", client.account.username)
        self.assertEqual(client_count + 1, Client.objects.count())

    def test_edit_employee(self):
        employee = Employee.objects.first()
        contract = employee.contract_begin
        employee.telephone = "987654321"
        employee.save()
        self.assertEqual(contract, employee.contract_begin)
        self.assertEqual("987654321", employee.telephone)

    def test_edit_client(self):
        client = Client.objects.first()
        telephone = client.telephone
        client.address = "Nassau"
        client.save()

        self.assertEqual("Nassau", client.address)
        self.assertEqual(telephone, client.telephone)

    def test_user_is_employee(self):
        user = User.objects.filter(first_name="Jessica").first()
        account = Account.objects.get_from_user(user)
        self.assertTrue(account.is_employee())

    def test_user_is_client(self):
        user = User.objects.filter(first_name="Diana").first()
        account = Account.objects.get_from_user(user)
        self.assertTrue(account.is_client())

    def test_unicode(self):
        client = Client.objects.get(account__first_name="Diana")
        employee = Employee.objects.get(account__first_name="Jessica")

        self.assertEqual(unicode(client), unicode(client.account))
        self.assertEqual(unicode(employee), unicode(employee.account))
