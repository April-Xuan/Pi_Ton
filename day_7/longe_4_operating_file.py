#  author: crislashgz1900
#  2025/02/13 15:36:54
#  1851195747@qq.com


def open_r():
    """
    读取文件
    :return:
    """
    file = open('longe_file_2.txt', mode='r', encoding='utf-8')
    text = file.read()  # 读出来的都是字符串
    print(text)
    file.close()


def open_rw():
    """
    读取文件, 写入文件
    :return:
    """
    file = open('longe_file_2.txt', mode='r+', encoding='utf-8')
    text = file.read()  # 读出来的都是字符串
    print(text)
    file.write(' Ich mochte wandern gehen!')  # 写到末尾了
    file.close()


def open_w():
    """
    练习 w 模式写入文件
    :return:
    """
    file = open('longe_file_3.txt', mode='w', encoding='utf-8')  # 文件不存在就会创建，存在就会清空
    # file.write('Ich bin ein kleines blumelein.')
    file.close()


def open_a():
    """
    练习 a 模式, 每次写到文件末尾
    :return:
    """
    file = open('longe_file_1', mode='a', encoding='utf-8')
    file.write('how')
    file.close()


def use_readline():
    # 打开文件
    file = open("longe_file_2.txt", encoding="utf-8")

    while True:
        # 读取一行内容
        text = file.readline()

        # 判断是否读到内容, 读取到文件末尾拿到的是一个空字符串
        if not text:
            break

        # 每读取一行的末尾已经有了一个 '\n'
        print(text, end='')


if __name__ == '__main__':
    # open_r()
    # open_rw()
    # open_w()
    # open_a()
    use_readline()