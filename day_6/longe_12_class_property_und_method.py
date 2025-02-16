#  author: crislashgz1900
#  2025/02/05 15:22:16
#  1851195747@qq.com

class Tool:
    count = 0  # class property

    def __init__(self, name):
        self.name = name
        Tool.count += 1  # increment class property count

    def func(self):
        print(f"Es ist ein {self.name} tool")

    @classmethod
    def show_count(cls):
        print(cls.count)

    @staticmethod  # 静态方法，后面基本上用不着
    def help():
        print("This is a static method")


if __name__ == '__main__':
    tool1 = Tool('ax')
    print(Tool.count)
    tool1.func()
    Tool.show_count()
    Tool.help()
