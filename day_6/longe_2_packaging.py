#  author: crislashgz1900
#  2025/01/10 15:52:57
#  1851195747@qq.com


class Person:
    """human"""

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print(f'{self.name} joggt, es weighs {self.weight}kg jetzt')

    def eat(self):
        self.weight += 1
        print(f'{self.name} ate, es weighs {self.weight}kg jetzt')

    def __str__(self):
        """因为该函数是别人调用的，所以返回值必须是字符串"""
        return f'Ich heiβe {self.name} und mein weight ist {self.weight}kg'  # 不要写成 print()


if __name__ == "__main__":
    elefant = Person('elefant', 80)
    elefant.run()
    elefant.eat()
    print(elefant)
