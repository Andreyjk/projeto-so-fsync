
import os
import time

def medir_gravacao(usar_fsync):
    inicio = time.perf_counter()

    with open("teste_gravacao.txt", "w") as arquivo:
        for i in range(100):
            arquivo.write(f"Registro {i}\n")

            if usar_fsync:
                arquivo.flush()
                os.fsync(arquivo.fileno())

    fim = time.perf_counter()
    tempo_total = (fim - inicio) * 1000

    return tempo_total


os.makedirs("dados", exist_ok=True)

for rodada in range(5):
    tempo_sem = medir_gravacao(False)
    tempo_com = medir_gravacao(True)

    print(f"Rodada {rodada + 1}")
    print(f"Sem fsync: {tempo_sem:.3f} ms")
    print(f"Com fsync: {tempo_com:.3f} ms")
    print("---------------------------")

    with open("dados/tempo_sem_fsync.txt", "a") as arquivo:
        arquivo.write(f"{tempo_sem:.3f}\n")

    with open("dados/tempo_com_fsync.txt", "a") as arquivo:
        arquivo.write(f"{tempo_com:.3f}\n")
