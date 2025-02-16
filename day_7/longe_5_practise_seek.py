#  author: crislashgz1900
#  2025/02/16 16:48:07
#  1851195747@qq.com
import os


def seek_start():
    """
    相对于开头(文件起始位置)进行偏移
    :return:
    """
    file = open('longe_file_1', mode='r+', encoding='utf-8')

    file.seek(5, os.SEEK_SET)  # 相对于开头偏移 5 个字节
    text = file.read(5)  # 一个字母占一个字节, 一个汉字占三个字节
    print(text)
    file.close()


def seek_end():
    """
    相对于结尾(文件末尾位置)进行偏移
    :return:
    """
    file = open('longe_file_1', mode='r+', encoding='utf-8')
    file.seek(0, os.SEEK_END)
    text = file.read(5)
    print(text)
    file.close()


def seek_cur():
    """
    相对于当前位置不动
    :return:
    """
    file = open('longe_file_1', mode='r+', encoding='utf-8')
    file.seek(0, os.SEEK_CUR)
    text = file.read(5)  # 一个字母占一个字节, 一个汉字占三个字节
    print(text)  # 读不到内容, 是空字符串
    file.close()


def seek_b_cur():
    """
    在 b 模式下, 读取到的是字节流, 读取图片, 音频, 视频
    :return:
    """
    file = open('longe_file_1', mode='rb+')  # 不需要指定编码格式
    file.seek(5, os.SEEK_CUR)
    zjl = file.read()  # zi jie liu, 得到的是字节流
    print(zjl)
    file.close()


if __name__ == '__main__':
    # seek_start()
    # seek_end()
    # seek_cur()
    seek_b_cur()
