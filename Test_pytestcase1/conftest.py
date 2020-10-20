import pytest
import yaml
import sys
sys.path.append('../')
from Cal_method.funcal import Calculator

@pytest.fixture(params=['user1', 'user2', 'user3'])
def login(request):
    print('登陆方法')
    print('传入的参数为：'+str(request.param))
    yield ['username', 'passwd']
    print('teardown')

@pytest.fixture(scope='module')
def get_calc():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")


