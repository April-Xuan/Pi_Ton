#  author: crislashgz1900
#  2025/01/13 15:46:50
#  1851195747@qq.com


class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count = count

    def shoot(self):
        if 0 >= self.bullet_count:
            print("No bullet")
            return

        self.bullet_count -= 1
        print(f'{self.model} fired, {self.bullet_count} bullets remained')


class Soldier:
    def __init__(self, name, gun: Gun = None):  # 要让别人知道这个对象有多少属性
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun is None:  # 判断两个对象是否是同一个
            print(f"{self.name} has kein guns")
            return

        print(f'{self.name} rushes')

        self.gun.add_bullet(40)

        self.gun.shoot()


if __name__ == '__main__':
    ak47 = Gun('AKM')
    # ak47.add_bullet(40)
    # ak47.shoot()

    alice = Soldier('Alice')
    alice.fire()
    alice.gun = ak47
    alice.fire()

