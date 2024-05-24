from random import randint


def jogar_dado(lados):
    return randint(0, lados)


print(jogar_dado(6))
