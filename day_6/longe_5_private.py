#  author: crislashgz1900
#  2025/01/16 11:32:18
#  1851195747@qq.com

# 私有属性和私有方法只能在类内部访问

class Woman:
    def __init__(self, name, age):
        self.__age = age  # 私有属性
        self.name = name
        # 一个下划线不是私有属性，只是在有的编译器里不会联想出来，超出命名规范

    def __secret(self):  # 私有方法
        print(f"{self.name} ist {self.__age}")  # 类的方法可以访问私有属性

    def bf(self):
        self.__secret()


if __name__ == "__main__":
    biying = Woman("Wu Biying", 18)
    print(biying.name)
    biying.bf()

