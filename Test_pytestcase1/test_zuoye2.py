import pytest
import yaml


def get_datas():
    with open("D:/mundo/Hogwarts/test/hogwarts_learn/testdata/calc.yml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas['Calculator']

class TestCalculator:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', get_datas()['ADD']['parametrize'], ids=get_datas()['ADD']['ids'])
    def test_add(self, get_calc,a, b, expect):
        result = get_calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect', get_datas()['SUB']['parametrize'], ids=get_datas()['SUB']['ids'])
    def test_sub(self,get_calc, a, b, expect):
        result = get_calc.sub(a, b)
        assert round(result, 2) == expect

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect', get_datas()['MUL']['parametrize'], ids=get_datas()['MUL']['ids'])
    def test_mul(self,get_calc, a, b, expect):
        result = get_calc.mul(a, b)
        assert round(result, 2) == expect

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expect',get_datas()['DIV']['parametrize'], ids=get_datas()['DIV']['ids'])
    def test_div(self,get_calc, a, b, expect):
        result = get_calc.div(a, b)
        assert result == expect

    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('a,b',get_datas()['DIV_ZERO']['parametrize'], ids=get_datas()['DIV_ZERO']['ids'])
    def test_div_zero(self,get_calc, a, b):
        with pytest.raises(ZeroDivisionError):
            get_calc.div(a, b)