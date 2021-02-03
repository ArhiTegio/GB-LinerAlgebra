import numpy as np
from lineAlg import LinerAlg

if __name__ == '__main__':
    alg = LinerAlg()
    print('Задача 2.1')
    for vector in [[[0, -3, 6], [-4, 7, 9]], [[7, -4, 0, 1], [-3, 1, 11, 2]]]:
        print(f'Скалярное произведение [{",".join([str(e) for e in vector[0]])}] и [{",".join([str(e) for e in vector[1]])}]:\n{np.dot(vector[0], vector[1])}')

    print('Задача 2.2')
    ans = alg.Task2_2(np.array([4, 2, 4]), np.array([12, 3, 4]))
    print('Манхэттенская норма а = {0}, b = {1}'.format(ans[0][0], ans[0][1]))
    print('Евклидова норма а = {0}, b = {1}'.format(ans[1][0], ans[1][1]))
    print('Угол между a и b: {0}'.format(ans[2][0]))

    print('Задача 2.4')
    print('2.4.1. Базисом не является')
    for isBasis in [["2.4.2.", np.array([[1/(2**(1/2)), -1/(2**(1/2)), 0], [0, 1, 0], [0, 0, 1]])],
                    ["2.4.3", np.array([[1/2, -1/2, 0], [0, 1/2, 1/2], [0, 0, 1]])],
                    ["2.4.4", np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])]]:
        print("{0} Является ортонормированным базисом".format(isBasis[0]) if alg.Task2_4(isBasis[1]) else "{0} Базисом не является".format(isBasis[0]))



