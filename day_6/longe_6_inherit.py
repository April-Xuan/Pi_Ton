#  author: crislashgz1900
#  2025/01/16 14:47:19
#  1851195747@qq.com


class Animal:

    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} ist eating --")

    def drink(self):
        print(f"{self.name} ist drinking --")

    def run(self):
        print(f"{self.name} ist running --")

    def sleep(self):
        """
        老师您好，我叫郭怿璇，一志愿报考复旦大学电子信息专业
        报考代码085400，初试分数约340分
        本科武大数学专业，六级514分雅思6.5
        参加过华数杯和华中杯建模比赛负责全部代码
        请问我有调剂的机会吗？

        请问贵校往年控制工程专业或者相近专业是否开放过调剂呢
        一般什么时候可以有比较确定的消息
        学院一般什么时候可能发公告呢
        :return:
        """
        print(f"{self.name} ist sleeping")


class Hund(Animal):
    def __init__(self, name, color):  # 提示说是不要忘记父类的初始化方法
        super().__init__(name)  # super.() 是匿名的父类对象
        self.color = color

    def bark(self):
        print(f"{self.color} {self.name} ist barking --")

    def run(self):
        super().run()
        print(f"{self.name} ist running fast --")


class XiaoTianHund(Hund):
    def __init__(self, name, color, age):  # 不能隔代继承，也没有这个需求
        super().__init__(name, color)
        self.age = age

    def fly(self):
        print(f"{self.color} {self.name} ist flying --")


if __name__ == '__main__':
    tim = Hund("Tim", "red")
    tim.bark()
    tim.sleep()
    xtq = XiaoTianHund("Xiao Tian", 'yellow', 20)
    xtq.fly()
    xtq.eat()
    xtq.run()


