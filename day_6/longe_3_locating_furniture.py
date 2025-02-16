#  author: crislashgz1900
#  2025/01/10 16:22:24
#  1851195747@qq.com


# 有限设计被依赖的类
class HouseItem:
    def __init__(self, name, area):
        """
        initialization
        :param name: name of the furniture
        :param area: the area the furniture occupies
        """
        self.name = name
        self.area = area

    def __str__(self):
        return '%s occupies %.2f' % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        """
        房子初始化方法
        :param house_type:
        :param area:
        """
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []  # 家具列表
        self.free_area = area

    def __str__(self):
        return ("Type: %s\nTotal Area: %.2f [%.2f remained]\n Furniture: %s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item:HouseItem):  # 注解没有任何意义，只是为了联想代码，冒号:对象类型：注解
        if item.area > self.free_area:
            print("No free area, failed to lay")
            return  # 没有任何返回值

        self.free_area -= item.area
        self.item_list.append(item.name)  # 实际的工作中肯定放的是对象


if __name__ == '__main__':
    bed = HouseItem('Simmons', 3)
    closet = HouseItem('Sushi', 2)
    table = HouseItem('Yadi', 1.5)
    print(bed)
    print(closet)
    print(table)

    print("-" * 14, "About the House", "-" * 15)

    house = House('3 rooms & 2 halls', 30)
    print(house)

    house.add_item(bed)
    house.add_item(closet)
    house.add_item(table)

    print("-" * 14, "After Putting the Furniture", "-" * 15)

    print(house)
