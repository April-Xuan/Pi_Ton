#  author: crislashgz1900
#  2025/02/05 14:50:35
#  1851195747@qq.com

# 多态就是同一条指令, 产生的行为是不一样的

class Hund(object):
    def __init__(self, name):
        self.name = name

    def spiele(self):
        print("Ich spiele mit {}.".format(self.name))

class XiaoTianHund(Hund):
    def spiele(self):
        print("{} flies like a bird.".format(self.name))


class Person(object):
    def __init__(self, name):
        self.name = name

    def spiele(self, hund):
        print("{} spiele mit {}.".format(self.name, hund.name))
        hund.spiele()


if __name__ == '__main__':
    nina = Person("Nina")
    xiaotian = XiaoTianHund("Xiao Tian")
    nina.spiele(xiaotian)
