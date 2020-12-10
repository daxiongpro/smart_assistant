def t1():
    global g_b
    g_b = 2
    g_l1 = []
    g_l2.append(7)


if __name__ == '__main__':
    g_b = 3
    g_l1 = [1, 2]
    g_l2 = [1, 2, 3]

    t1()
    print(g_b, g_l1, g_l2)
