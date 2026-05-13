import os
import platform

ARQUIVO = "consultas.txt"

def limpar_tela():
    """Limpa a tela conforme o sistema operacional."""
    os.system("cls" if platform.system() == "Windows" else "clear")

def pausar():
    """Espera o usuário apertar ENTER para continuar."""
    input("\nPressione ENTER para voltar ao menu...")

def carregar_consultas():
    """Carrega todas as consultas do arquivo"""
    consultas = []
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                partes = [p.strip() for p in linha.strip().split(",")]
                if len(partes) == 5:
                    consultas.append({
                        "cpf": partes[0],
                        "medico": partes[1],
                        "especialidade": partes[2],
                        "data": partes[3],
                        "hora": partes[4]
                    })
    return consultas

def salvar_consultas(consultas):
    """Salva todas as consultas no arquivo"""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for c in consultas:
            f.write(f"{c['cpf']}, {c['medico']}, {c['especialidade']}, {c['data']}, {c['hora']}\n")

def listar_consultas(consultas):
    """Lista todas as consultas"""
    limpar_tela()
    if not consultas:
        print("\nNenhuma consulta cadastrada.\n")
        pausar()
        return
    print("=== LISTA DE CONSULTAS ===\n")
    for i, c in enumerate(consultas, 1):
        print(f"{i}. CPF: {c['cpf']} | {c['medico']} ({c['especialidade']}) | "
              f"{c['data']} às {c['hora']}")
    pausar()

def marcar_consulta(consultas):
    """Adiciona nova consulta"""
    limpar_tela()
    print("=== MARCAR NOVA CONSULTA ===\n")
    cpf = input("CPF do paciente: ").strip()
    medico = input("Nome do médico: ").strip()
    especialidade = input("Especialidade: ").strip()
    data = input("Data (dd/mm/aaaa): ").strip()
    hora = input("Hora (hh:mm): ").strip()

    nova = {"cpf": cpf, "medico": medico, "especialidade": especialidade, "data": data, "hora": hora}
    consultas.append(nova)
    salvar_consultas(consultas)
    print("\n Consulta marcada com sucesso!")
    pausar()

def alterar_consulta(consultas):
    """Altera uma consulta existente"""
    limpar_tela()
    listar_consultas(consultas)
    if not consultas:
        return
    try:
        indice = int(input("\nDigite o número da consulta que deseja alterar: ")) - 1
        if 0 <= indice < len(consultas):
            c = consultas[indice]
            print(f"\nEditando consulta de {c['medico']} ({c['especialidade']}) em {c['data']} às {c['hora']}")
            c["data"] = input(f"Nova data (atual {c['data']}): ").strip() or c["data"]
            c["hora"] = input(f"Nova hora (atual {c['hora']}): ").strip() or c["hora"]
            salvar_consultas(consultas)
            print("\n Consulta alterada com sucesso!")
        else:
            print(" Consulta não encontrada.")
    except ValueError:
        print(" Entrada inválida.")
    pausar()

def excluir_consulta(consultas):
    """Remove uma consulta"""
    limpar_tela()
    listar_consultas(consultas)
    if not consultas:
        return
    try:
        indice = int(input("\nDigite o número da consulta que deseja excluir: ")) - 1
        if 0 <= indice < len(consultas):
            removida = consultas.pop(indice)
            salvar_consultas(consultas)
            print(f"\n Consulta de {removida['medico']} removida com sucesso.")
        else:
            print(" Consulta não encontrada.")
    except ValueError:
        print(" Entrada inválida.")
    pausar()

def consultar_por_paciente(consultas):
    """Mostra as consultas de um paciente específico"""
    limpar_tela()
    cpf = input("Digite o CPF do paciente: ").strip()
    filtradas = [c for c in consultas if c["cpf"] == cpf]
    if filtradas:
        print(f"\nConsultas do paciente {cpf}:")
        for c in filtradas:
            print(f"- {c['medico']} ({c['especialidade']}) em {c['data']} às {c['hora']}")
    else:
        print("\n Nenhuma consulta encontrada para este CPF.")
    pausar()

def menu():
    consultas = carregar_consultas()
    while True:
        limpar_tela()
        print("=== MENU DE CONSULTAS ===")
        print("1. Listar todas as consultas")
        print("2. Marcar nova consulta")
        print("3. Alterar uma consulta")
        print("4. Excluir uma consulta")
        print("5. Consultar por paciente (CPF)")
        print("0. Sair")
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            listar_consultas(consultas)
        elif opcao == "2":
            marcar_consulta(consultas)
        elif opcao == "3":
            alterar_consulta(consultas)
        elif opcao == "4":
            excluir_consulta(consultas)
        elif opcao == "5":
            consultar_por_paciente(consultas)
        elif opcao == "0":
            limpar_tela()
            print("Saindo... ")
            break
        else:
            print("\nOpção inválida, tente novamente.")
            pausar()

if __name__ == "__main__":
    menu()