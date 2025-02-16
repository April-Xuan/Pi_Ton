#  author: crislashgz1900
#  2025/02/13 14:47:53
#  1851195747@qq.com

class A:
    def __init__(self):
        self.__age = 18


class B(A):
    def get_age(self):
        print(self.__age)

