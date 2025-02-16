#  author: crislashgz1900
#  2025/01/10 15:23:16
#  1851195747@qq.com

# 面向对象的三大特性：封装、（之前要学私有属性和私有方法）继承和多态

# 不要在类给对象增加属性


class Katze:
    """
    这是一个猫类
    """
    def __init__(self, name):
        print("Es ist ein method for initialization")
        self.name = name

    def eat(self):
        print(f"{self.name} eats fisch gern")

    def drink(self):
        print(f"{self.name} drinks wasser")

    def __del__(self):  # 重写销毁函数，对象被从内存中销毁前，会被自动调用
        print("Katze object is destroyed")


if __name__ == '__main__':
    print("indent")  # 练习缩进
    tom = Katze('tom')
    tom.eat()
    tom.drink()

    del tom  # 就算没有这一句，程序结束时也会销毁对象
    print("Process ends")

