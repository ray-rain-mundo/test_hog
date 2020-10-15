"""写一个Bicycle(自行车)类,有run(骑行)方法,
调用时显示骑行里程km(骑行里程为传入的数字):再写一个电动自行车类EBicycle继承自Bicycle,
添加电池电量valume属性通过，参数传入, 同时有两个方法：
1）fill_charge(vol) 用来充电, vol 为电量
2）run(km) 方法用于骑行,每骑行10km消耗电量1度,当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果"""


class Bicycle():
    def run(self, km):
        print(f"该自行车骑行里程为{km}公里")


class Ebicycle(Bicycle):
    def __init__(self, valume):
        self.valume = valume

    def fill_charge(self, vol):
        self.valume += vol
        print(f"该车充了{vol}度电,电动车电量为{self.valume}度")

    def run(self, km):
        left_valume = self.valume - km / 10
        if left_valume == 0:
            super().run(km)
        elif left_valume < 0:
            print(f"当前电量不足以骑行完剩余路程{km}")
        elif left_valume > 0:
            print(f"可以骑行完路程{km},剩余电量为{left_valume}")


if __name__ == '__main__':
    e = Ebicycle(2)
    e.fill_charge(10)
    e.run(12)
