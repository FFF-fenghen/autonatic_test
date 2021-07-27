from time import sleep
import threading

def test_1():
    sleep(2)


def test_2():
    sleep(3)


def test_3():
    sleep(4)

#
# if __name__ == '__main__':
#     pytest.main(['-s', __file__, '--tests-per-worker=4'])
