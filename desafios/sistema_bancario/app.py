import os
import time
import getpass

balance = 0
withdrawal = 0
deposit_day = 0
withdrawal_limit = 500
statement = ""
withdrawal_count = 0
MAX_WITHDRAWALS = 3

database = {"users": [], "addresses": [], "bank_accounts": []}

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

def deposit(deposit_value: int, /) -> None:
    global balance
    global deposit_day

    print(f"{LIGHT_GREEN}✓ Operação de depósito selecionada{RESET}")
    print(f"{BLUE}Seu saldo atual é de: R$ {balance:.2f} {RESET}")

    if deposit_value <= 0:
        print(f"{DARK_RED} Operação invalida, o valor deve ser maior que R$ 0.00{RESET}")
        return
    
    balance += deposit_value
    deposit_day += deposit_value
    print(f"{LIGHT_GREEN}Depósito de R$ {deposit_value:.2f} realizado com sucesso!{RESET}")
    return

def withdraw(*, local_withdrawal: int) -> None:
    global balance
    global withdrawal
    global withdrawal_count
    global withdrawal_limit

    print(f"{LIGHT_GREEN}✓ Operação de saque selecionada{RESET}")

    if balance <= 0:
        print(f"{YELLOW}Operação de saque cancelada por saldo insuficiente R$ {balance:.2f} {RESET}")
        return
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

def statement_history(cpf: int, /, *, account_number: int) -> None:
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

def cpf_processor(cpf: str) -> int:
    int_cpf = cpf.replace(".", "").replace("-", "").replace("/", "")
    return int(int_cpf)

def user_already_exists(cpf: int) -> bool:
    global database

    if not database.get("users"):
        return False
    for user in database.get("users"):
        if cpf in user.get("cpf", set()):
            return True
    return False

def get_user_by_cpf(cpf: int) -> list:
    global database

    if not database.get("users"):
        return None
    
    for user in database.get("users"):
        if cpf in user.get("cpf", set()):
            return user

    return None

def create_user(
        *, 
        name: str, 
        last_name: str, 
        birthday: str, 
        cpf: int, 
        address: str,
        password: str
    ) -> None:
    global database

    user_exists = user_already_exists(cpf)

    if not user_exists:
        new_user = {"cpf": {cpf},"password": {password},"name": {name},"last_name": {last_name},"birthday": {birthday},"address": {address}}
        database["users"].append(new_user)
        clear_console()
        print(f"{LIGHT_GREEN}✓ Usuário cadastrado com sucesso!!{RESET}")
        return
    else:
        clear_console()
        print(f"{LIGHT_RED}X O CPF informado já esta existe{RESET}")
    return

def login(*, cpf: int, password: str) -> bool:
    global database

    if not database.get("users"):
        return False
    
    user_credentials = get_user_by_cpf(cpf)

    if not user_credentials:
        return False
    
    if cpf in user_credentials.get("cpf", set()) and password in user_credentials.get("password", set()):
        return True

title = " Bem vindo ao banco Pybank "
title = title.center(len(title) + 10, "#")

menu_login = f"""
    {title}
    c: cadastrar uma conta
    e: entrar
    s: sair
===> """

def bank_main_screen(last_name, name) -> None:
    menu = f"""
        {BLUE}Bem vindo ao Pybank {name} em que posso ajudar?{RESET}
        d: depositar
        s: sacar
        e: extrato
        q: sair
    ===> """
    while True:
        response = input(menu)

        clear_console()
        if response == "d":
            deposit_value = input("Digite o valor do depósito que deseja realizar: ")
            deposit_value = int(deposit_value)
            deposit(deposit_value)
        elif response == "s":
            local_withdrawal = input("Informe o valor que deseja sacar: ")
            local_withdrawal = int(local_withdrawal)
            withdraw(local_withdrawal=local_withdrawal)
        elif response == "e":
            statement_history(1, account_number=2)
        elif response == "q":
            clear_console()
            print(f"{LIGHT_GREEN}✓ Obrigado por utilizar o Pybank, volte sempre =D{RESET}")
            break
        else:
            print(f"{LIGHT_RED}X Operação inválida, favor selecionar uma das opções do menu{RESET}")
        
        time.sleep(1)

def login_screen():
    while True:
        response = input(menu_login)

        clear_console()
        if response == "c":
            name = input("Digite seu nome: ")
            last_name = input("Digite seu sobrenome: ")
            birthday = input("Digite seu ano de nascimento: ")
            cpf = input("Digite seu CPF: ")
            cpf = cpf_processor(cpf)
            street = input("Qual a rua que você mora? ")
            number = input("Qual o número da rua? ")
            district = input("Qual o seu Bairro? ")
            city = input("Qual a sua cidade? ")
            state = input("Qual o seu estado? ")
            full_address = f"""{street}, {number} - {district} - {city}/{state}."""
            password = getpass.getpass("Crie uma senha: ")

            create_user(name=name, last_name=last_name, birthday=birthday, cpf=cpf, address=full_address, password=password)
        elif response == "e":
            cpf = input("Digite seu CPF, somente os números: ")
            cpf = int(cpf)

            password = getpass.getpass("Digite sua senha: ")
            is_logged = login(password=password, cpf=cpf)

            if is_logged:
                clear_console()
                bank_main_screen(last_name, name)
            else:
                clear_console()
                print(f"{LIGHT_RED}X Login ou senha incorretos, favor tentar mais tarde{RESET}")
        elif response == "s":
            clear_console()
            print(f"{LIGHT_GREEN}✓ Obrigado por utilizar o Pybank, volte sempre =D{RESET}")
            break
        else:
            print(f"{LIGHT_RED}X Operação inválida, favor selecionar uma das opções do menu{RESET}")
        
        time.sleep(1)

login_screen()