from Cal_method.funcal import Calculator
import pytest


class Test_add:

    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    def teardow_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,c', [[1, 1, 2], [0, 0, 0], [100000000, 100000000, 200000000],
                                       [0.1, 0.1, 0.2], [-1, -2, -3], [-1, 1, 0], [3.2, 3.2, 6.4],
                                       [-100000, -100000, -200000]])
    def test_add_int(self, a, b, c):
        result_add1 = self.cal.add(a, b)
        assert result_add1 == c
        print("加法用例通过")
        if result_add1 != c:
            print("参数输入错误，请重新输入")

    # with pytest.raises(AssertionError):  raises异常情况捕获，说明用例正常通过！
    # self.cal.add(a,b)

    @pytest.mark.parametrize('a,b,c', [[10, 2, 5], [0.1, 2, 0.05], [10000, 10000, 1]])
    def test_div(self, a, b, c):
        result_div = self.cal.div(a, b)
        assert result_div == c
        print("除法用例通过")

