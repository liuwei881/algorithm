#coding=utf-8


def sum_def(lis):
    """模拟sum函数"""
    if len(lis) == 0:
        return 0
    else:
        return lis[0] + sum_def(lis[1:])


def list_contain(lis):
    """列表中包含的元素数"""
    if len(lis) == 0:
        return 0
    else:
        return 1 + list_contain(lis[1:])


def list_max(lis):
    """找出list中最大的数"""
    if len(lis) == 1:
        return lis[0]
    else:
        return lis[0] if lis[0] > list_max(lis[1:]) else list_max(lis[1:])


if __name__ == '__main__':
    print(list_max([4000, 5, 6, 10, 20, 500]))