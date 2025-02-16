#  author: crislashgz1900
#  2025/02/05 15:48:01
#  1851195747@qq.com

class MusicPlayer:
    instance = None  # 用来保存对象

    def __new__(cls, *args, **kwargs):  # 里面的*args和**kwargs是为了让类的构造函数可以接收参数
        if cls.instance is None:
            cls.instance = super().__new__(cls)  # 调用父类的构造函数, 类似于C语言中的malloc()
        return cls.instance  # 返回单例对象

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    player1 = MusicPlayer('Erika')
    player2 = MusicPlayer('Schnappi')
    print(id(player1))
    print(id(player2))
    print(player1.name)
    print(player2.name)
