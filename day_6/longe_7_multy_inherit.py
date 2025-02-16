#  author: crislashgz1900
#  2025/02/03 14:11:36
#  1851195747@qq.com
class A:
    def test(self):
        print('A test')

    def demo(self):
        print("A demo")


class B:
    def test(self):
        print('B test')

    def demo(self):
        print('B demo')


class C(A, B):
    pass


if __name__ == '__main__':
    c = C()
    c.test()
    print(C.__mro__)  # 查找顺序


# 梯子链接: https://jsir5.no-mad-world.club/link/sLA6NBhT3WQufxvL?clash=3&extend=1
# 购买链接1: https://01081141.99iepl.com/#/register?code=vbE6Z4tr  # 泡泡狗
# 购买链接2: https://977168.xyz/#/register?code=I6YKDqAk  # bucd
