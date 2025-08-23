import os
import time

balance = 0
withdrawal = 0
deposit_day = 0
withdrawal_limit = 500
statement = ""
withdrawal_count = 0
MAX_WITHDRAWALS = 3

# ANSI code for colors
LIGHT_GREEN = "\033[92m"
DARK_GREEN = "\033[32m"
LIGHT_RED = "\033[91m"
DARK_RED = "\033[31m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def clear_console() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def deposit() -> None:
    global balance
    global deposit_day

    print(f"{LIGHT_GREEN}✓ Operação de depósito selecionada{RESET}")
    print(f"{BLUE}Seu saldo atual é de: R$ {balance:.2f} {RESET}")
    
    deposit_value = input("Digite o valor do depósito que deseja realizar: ")
    deposit_value = int(deposit_value)

    if deposit_value <= 0:
        print(f"{DARK_RED} Operação invalida, o valor deve ser maior que R$ 0.00{RESET}")
        return
    
    balance += deposit_value
    deposit_day += deposit_value
    print(f"{LIGHT_GREEN}Depósito de R$ {deposit_value:.2f} realizado com sucesso!{RESET}")
    return

def withdraw() -> None:
    global balance
    global withdrawal
    global withdrawal_count
    global withdrawal_limit

    print(f"{LIGHT_GREEN}✓ Operação de saque selecionada{RESET}")

    if balance <= 0:
        print(f"{YELLOW}Operação de saque cancelada por saldo insuficiente R$ {balance:.2f} {RESET}")
        return
    
    local_withdrawal = input("Informe o valor que deseja sacar: ")
    local_withdrawal = int(local_withdrawal)

    if withdrawal_count >= MAX_WITHDRAWALS:
        print(f"{LIGHT_RED}X Você ultrapassou a quantidade de saques diarios permitido{RESET}")
        return
    elif local_withdrawal > withdrawal_limit:
        print(f"{LIGHT_RED}X Você ultrapassou o limite máximo de R$ 500.00 por saque{RESET}")
        return
    elif local_withdrawal > balance:
        print(f"{LIGHT_RED}X O valor de saque é maior do que o seu saldo{RESET}")
        return
    
    print(f"{LIGHT_GREEN}✓ Saque no valor de R$ {local_withdrawal} realizado com sucesso {RESET}")
    balance -= local_withdrawal
    withdrawal += local_withdrawal
    withdrawal_count += 1
    print(f"{BLUE}Novo saldo total R$ {balance} {RESET}")

def statement_history() -> None:
    global balance
    global withdrawal
    global statement
    global deposit_day

    statement = f"""
    Total de depositos do dia R$ {deposit_day:.2f}
    Total de saques do dia R$ {withdrawal:.2f}
    Total de saldo da conta R$ {balance:.2f}
    """

    print(f"{BLUE} {statement} {RESET}")

title = " Bem vindo ao banco Pybank "
title = title.center(len(title) + 10, "#")

menu = f"""
    {title}
    d: depositar
    s: sacar
    e: extrato
    q: sair
===> """

while True:
    response = input(menu)

    clear_console()
    if response == "d":
        deposit()
    elif response == "s":
        withdraw()
    elif response == "e":
        statement_history()
    elif response == "q":
        clear_console()
        print(f"{LIGHT_GREEN}✓ Obrigado por utilizar o Pybank, volte sempre =D{RESET}")
        break
    else:
        print(f"{LIGHT_RED}X Operação inválida, favor selecionar uma das opções do menu{RESET}")
    
    time.sleep(1)

print(menu)