#  author: crislashgz1900
#  2025/02/05 14:15:46
#  1851195747@qq.com


class Sonn1:
    def __init__(self, age, *args):
        self.age = age
        super().__init__(*args)


class Sonn2:
    def __init__(self, score):
        pass
        # self.age = age
        self.score = score


class GrandSonn(Sonn1, Sonn2):
    def __init__(self, name, *args):  # 可能会被传入多个参数
        self.name = name
        super().__init__(*args)


if __name__ == '__main__':
    Wolfgang = GrandSonn('Wolfgang', 18, 98.5)  # 姓名, 年龄, 分数

    print(Wolfgang.name)
    print(Wolfgang.age)
    print(Wolfgang.score)