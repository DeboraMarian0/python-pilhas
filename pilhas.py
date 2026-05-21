
from collections import deque


def menu():
    print("\n\033[0;30;45m=== Gerenciador de Processos ===\033[0m\n")
    print("1 - Inserir processo")
    print("2 - Executar processo")
    print("3 - Mostrar pilha de processos")
    print("4 - Sair")


def opcao_invalida():
    print("\n\033[0;31mOpção inválida. Tente novamente.\033[0m\n")
    opcoes()


def inserir_processo(nome_processo):
    pilha_processos.append(nome_processo)
    print(
        f"Processo \033[0;35m'{nome_processo}'\033[0m inserido na pilha de processos.\n")
    opcoes()


def listar_pilha():
    if pilha_processos:  # Se a pilha de processos não estiver vazia
        print("\n\033[1;32mPilha de Processos: \033[0m[", end=" ")

        for i in range(len(pilha_processos)):
            # se não for o último da lista
            if i == len(pilha_processos) - 1:
                print(f"{pilha_processos[i]}", end=" ")
            else:
                print(f"{pilha_processos[i]}", end=", ")
        print("]\n")
    else:
        print("\n\033[0;31mA pilha de processos está vazia.\033[0m\n")
    opcoes()


def executar_processos():
    if pilha_processos:
        # pop sempre exclui o último dado inserido
        processo_executado = pilha_processos.pop()
        print(
            f"\nProcesso \033[0;31m'{processo_executado}'\033[0m finalizado.\n")
    else:
        print("\n\033[0;31mNenhum processo para executar.\033[0m\n")
    opcoes()


def opcoes():
    try:
        menu()
        escolha_usuario = int(input("\nInsira a opção desejada (1-4): "))
        print(f"\nOpção escolhida: {escolha_usuario}")

        match escolha_usuario:
            case 1:
                nome_processo = input("\nNome do processo: ")
                inserir_processo(nome_processo)
            case 2:
                executar_processos()
            case 3:
                listar_pilha()
            case 4:
                print("\nFinalizando...\n")
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    global pilha_processos  # tem que ser global para poder ser acessada dentro das funções
    pilha_processos = deque()
    opcoes()


if __name__ == '__main__':
    main()
