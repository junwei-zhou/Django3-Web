from django.test import TestCase
from .models import PersonInfo
from django.contrib.auth.models import User
from django.test import Client


class PersonInfoTest(TestCase):
    # 添加数据
    def setUp(self):
        PersonInfo.objects.create(name='Lucy', age=10)
        PersonInfo.objects.create(name='May', age=12)

    # 编写测试用例
    def test_personInfo_age(self):
        # 编写用例
        name1 = PersonInfo.objects.get(name='Lucy')
        name2 = PersonInfo.objects.get(name='May')
        # 判断测试用例的执行结果
        self.assertEqual(name1.age, 10)
        self.assertEqual(name2.age, 12)

    # 编写测试用例
    def test_api(self):
        # 编写用例
        c = Client()
        response = c.get('/api/')
        # 判断测试用例的执行结果
        self.assertIsInstance(response.json(), dict)

    # 编写测试用例
    def test_html(self):
        # 编写用例
        c = Client()
        response = c.get('/?id=2')
        name = response.context['person'].name
        # 判断测试用例的执行结果
        self.assertEqual(name, 'May')
        self.assertTemplateUsed(response, 'index.html')


class UserTest(TestCase):
    # 添加数据
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='test', password='test', email='1@1.com')

    # 编写测试用例
    def test_user(self):
        # 编写用例
        r = User.objects.get(username='test')
        # 判断测试用例的执行结果
        self.assertEquals(r.email, '123@456.com')
        self.assertTrue(r.password)

    # 编写测试用例
    def test_login(self):
        # 编写用例
        c = Client()
        r = c.login(username='test', password='test')
        # 判断测试用例的执行结果
        self.assertTrue(r)
