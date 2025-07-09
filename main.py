import requests
from random import randint
import time
import random
import sqlite3


conn = sqlite3.connect("cpfs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cpfs_encontrados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf TEXT UNIQUE
)
""")
conn.commit()



def gerar_cpf():
    while True:
        cpf = [randint(0, 9) for _ in range(9)]
        if cpf != cpf[::-1]:
            break
    for i in range(9, 11):
        soma = sum(cpf[j] * (i + 1 - j) for j in range(i))
        digito = ((soma * 10) % 11) % 10
        cpf.append(digito)
    return ''.join(map(str, cpf)) # 54.42 s

def gerar_cpf2():

    cpf = [randint(0, 9) for _ in range(9)]
    while len(set(cpf)) == 1:
        cpf = [randint(0, 9) for _ in range(9)]

    pesos = [10, 11]
    for p in pesos:
        soma = sum(x * (p - i) for i, x in enumerate(cpf))
        cpf.append(((soma * 10) % 11) % 10)

    return ''.join(map(str, cpf)) # 54.55 s

def gerar_cpf3():

    cpf = [randint(0, 9) for _ in range(9)]
    while len(set(cpf)) == 1:
        cpf = [randint(0, 9) for _ in range(9)]

    pesos_1 = list(range(10, 1, -1))
    pesos_2 = list(range(11, 1, -1))

    soma1 = sum(x * y for x, y in zip(cpf, pesos_1))
    digito1 = ((soma1 * 10) % 11) % 10
    cpf.append(digito1)

    soma2 = sum(x * y for x, y in zip(cpf, pesos_2))
    digito2 = ((soma2 * 10) % 11) % 10
    cpf.append(digito2)

    return ''.join(map(str, cpf)) # 55.04 s


def gerar_cpf4():
    while True:
        cpf = [random.randint(0, 9) for _ in range(9)]
        if cpf[0] != cpf[1] or cpf[0] != cpf[2]:
            break

    soma = 0
    for i in range(9):
        soma += cpf[i] * (10 - i)
    digito1 = (soma * 10 % 11) % 10
    cpf.append(digito1)

    soma = 0
    for i in range(10):
        soma += cpf[i] * (11 - i)
    digito2 = (soma * 10 % 11) % 10
    cpf.append(digito2)

    return ''.join(map(str, cpf)) #54.18 s

def gerar_cpf5():
    cpf = [randint(0, 9) for _ in range(8)]
    cpf.append(randint(0, 9))

    if cpf.count(cpf[0]) == 9:
        cpf[-1] = (cpf[-1] + 1) % 10
    for i in range(9, 11):
        soma = sum(cpf[j] * (i + 1 - j) for j in range(i))
        cpf.append(((soma * 10) % 11) % 10)

    return ''.join(map(str, cpf)) # 54.46

def gerar_cpf6():
    cpf = [randint(0, 9) for _ in range(9)]
    if cpf[1] == cpf[0] and cpf[2] == cpf[0] and cpf[3] == cpf[0]:
        cpf[3] = (cpf[3] + 1) % 10

    soma1 = cpf[0]*10 + cpf[1]*9 + cpf[2]*8 + cpf[3]*7 + cpf[4]*6 + cpf[5]*5 + cpf[6]*4 + cpf[7]*3 + cpf[8]*2
    digito1 = (soma1 * 10 % 11) % 10
    cpf.append(digito1)

    soma2 = cpf[0]*11 + cpf[1]*10 + cpf[2]*9 + cpf[3]*8 + cpf[4]*7 + cpf[5]*6 + cpf[6]*5 + cpf[7]*4 + cpf[8]*3 + cpf[9]*2
    digito2 = (soma2 * 10 % 11) % 10
    cpf.append(digito2)

    return ''.join(str(d) for d in cpf) #57.41 s

def gerar_cpf7():

    cpf = [random.randint(0, 9) for _ in range(9)]


    if cpf[0] == cpf[1] == cpf[2]:
        cpf[2] = (cpf[2] + 1) % 10

    soma1 = cpf[0] * 10 + cpf[1] * 9 + cpf[2] * 8 + cpf[3] * 7 + cpf[4] * 6 + \
            cpf[5] * 5 + cpf[6] * 4 + cpf[7] * 3 + cpf[8] * 2
    digito1 = (soma1 * 10 % 11) % 10
    cpf.append(digito1)

    soma2 = cpf[0] * 11 + cpf[1] * 10 + cpf[2] * 9 + cpf[3] * 8 + cpf[4] * 7 + \
            cpf[5] * 6 + cpf[6] * 5 + cpf[7] * 4 + cpf[8] * 3 + cpf[9] * 2
    digito2 = (soma2 * 10 % 11) % 10
    cpf.append(digito2)

    return f"{cpf[0]}{cpf[1]}{cpf[2]}{cpf[3]}{cpf[4]}{cpf[5]}{cpf[6]}{cpf[7]}{cpf[8]}{cpf[9]}{cpf[10]}" # 55.63 s

def gerar_cpf8():
    a = randint(0, 9)
    b = randint(0, 9)
    c = randint(0, 9)
    d = randint(0, 9)
    e = randint(0, 9)
    f = randint(0, 9)
    g = randint(0, 9)
    h = randint(0, 9)
    i = randint(0, 9)

    if a == b == c == d == e == f == g == h == i:
        i = (i + 1) % 10

    soma1 = a*10 + b*9 + c*8 + d*7 + e*6 + f*5 + g*4 + h*3 + i*2
    j = (soma1 * 10 % 11) % 10

    soma2 = a*11 + b*10 + c*9 + d*8 + e*7 + f*6 + g*5 + h*4 + i*3 + j*2
    k = (soma2 * 10 % 11) % 10

    return f"{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}" # 53.59 s


def gerar_cpf9():

    cpf = [random.randint(0, 9) for _ in range(9)]


    if cpf[0] == cpf[1] == cpf[2]:
        cpf[-1] = (cpf[-1] + 1) % 10
    d1 = (10 * cpf[0] + 9 * cpf[1] + 8 * cpf[2] + 7 * cpf[3] + 6 * cpf[4] +
          5 * cpf[5] + 4 * cpf[6] + 3 * cpf[7] + 2 * cpf[8]) * 10 % 11 % 10

    d2 = (11 * cpf[0] + 10 * cpf[1] + 9 * cpf[2] + 8 * cpf[3] + 7 * cpf[4] +
          6 * cpf[5] + 5 * cpf[6] + 4 * cpf[7] + 3 * cpf[8] + 2 * d1) * 10 % 11 % 10

    return f"{cpf[0]}{cpf[1]}{cpf[2]}{cpf[3]}{cpf[4]}{cpf[5]}{cpf[6]}{cpf[7]}{cpf[8]}{d1}{d2}" # 54.03


def gerar_cpf10():
    multiplicador1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    multiplicador2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    semente = str(randint(100000000, 999999999))  # Gera 9 dígitos

    soma = sum(int(semente[i]) * multiplicador1[i] for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    semente += str(digito1)

    soma = sum(int(semente[i]) * multiplicador2[i] for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    semente += str(digito2)

    return semente # 53.53


def gerar_cpf11():
    semente = f"{random.randint(0, 999999999):09d}"

    if semente[0] * 9 == semente:
        semente = semente[:-1] + str((int(semente[-1]) + 1) % 10)

    soma = (int(semente[0]) * 10 + int(semente[1]) * 9 + int(semente[2]) * 8 +
            int(semente[3]) * 7 + int(semente[4]) * 6 + int(semente[5]) * 5 +
            int(semente[6]) * 4 + int(semente[7]) * 3 + int(semente[8]) * 2)

    resto = soma % 11
    d1 = 0 if resto < 2 else 11 - resto

    soma = (int(semente[0]) * 11 + int(semente[1]) * 10 + int(semente[2]) * 9 +
            int(semente[3]) * 8 + int(semente[4]) * 7 + int(semente[5]) * 6 +
            int(semente[6]) * 5 + int(semente[7]) * 4 + int(semente[8]) * 3 + d1 * 2)

    resto = soma % 11
    d2 = 0 if resto < 2 else 11 - resto

    return f"{semente}{d1}{d2}" #53.84


def gerar_cpf12():
    n = random.randint(0, 999999999)
    semente = f"{n:09d}"

    soma = (int(semente[0]) * 10 + int(semente[1]) * 9 + int(semente[2]) * 8 +
            int(semente[3]) * 7 + int(semente[4]) * 6 + int(semente[5]) * 5 +
            int(semente[6]) * 4 + int(semente[7]) * 3 + int(semente[8]) * 2)
    d1 = 0 if (resto := soma % 11) < 2 else 11 - resto

    soma = (int(semente[0]) * 11 + int(semente[1]) * 10 + int(semente[2]) * 9 +
            int(semente[3]) * 8 + int(semente[4]) * 7 + int(semente[5]) * 6 +
            int(semente[6]) * 5 + int(semente[7]) * 4 + int(semente[8]) * 3 + d1 * 2)
    d2 = 0 if (resto := soma % 11) < 2 else 11 - resto

    return f"{semente}{d1}{d2}" #54.46

def gerar_cpf13():
    semente = f"{randint(100000000, 999999999)}"
    soma1 = (
        (ord(semente[0]) - 48) * 10 +
        (ord(semente[1]) - 48) * 9 +
        (ord(semente[2]) - 48) * 8 +
        (ord(semente[3]) - 48) * 7 +
        (ord(semente[4]) - 48) * 6 +
        (ord(semente[5]) - 48) * 5 +
        (ord(semente[6]) - 48) * 4 +
        (ord(semente[7]) - 48) * 3 +
        (ord(semente[8]) - 48) * 2
    )
    resto1 = soma1 % 11
    d1 = 0 if resto1 < 2 else 11 - resto1

    semente += str(d1)

    soma2 = (
        (ord(semente[0]) - 48) * 11 +
        (ord(semente[1]) - 48) * 10 +
        (ord(semente[2]) - 48) * 9 +
        (ord(semente[3]) - 48) * 8 +
        (ord(semente[4]) - 48) * 7 +
        (ord(semente[5]) - 48) * 6 +
        (ord(semente[6]) - 48) * 5 +
        (ord(semente[7]) - 48) * 4 +
        (ord(semente[8]) - 48) * 3 +
        (ord(semente[9]) - 48) * 2
    )
    resto2 = soma2 % 11
    d2 = 0 if resto2 < 2 else 11 - resto2

    return semente + str(d2) #53.49

func_id = 13

def cpf_existe(cpf):
    url = f"suaAPI{cpf}"
    try:
        r = requests.get(url, timeout=2)
        return r.json().get("mensagem") != "CPF não encontrado."
    except:
        return False

if __name__ == "__main__":
    total_inicio = time.perf_counter()

    for i in range(100):
        cpf = globals()[f"gerar_cpf{func_id}"]()
        existe = cpf_existe(cpf)

        if existe:
            print(f"CPF encontrado: {cpf}")
            cursor.execute("INSERT OR IGNORE INTO cpfs_encontrados (cpf) VALUES (?)", (cpf,))

    total_fim = time.perf_counter()
    print(f"{total_fim - total_inicio:.2f} s")

    conn.commit()
    conn.close()


