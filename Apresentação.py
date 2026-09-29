from rich import print
import os
import json
 
def limparTela():
    os.system('cls')
 
def enterParaContinuar():
    input("Digite ENTER para continuar...")
 
def carregarCatalogo():
    try:
        with open("catalogo.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
 
def salvarCatalogo(catalogo):
    with open("catalogo.json", "w", encoding="utf-8") as arquivo:
        json.dump(catalogo, arquivo, ensure_ascii=False, indent=4)
 
def pedeTexto(mensagem):
    texto = input(mensagem).strip()
    while texto == "":
        print("Esse campo não pode ficar vazio.")
        texto = input(mensagem).strip()
    return texto
 
def pedeInteiro(mensagem, minimo, maximo):
    while True:
        try:
            numero = int(input(mensagem))
            while numero < minimo or numero > maximo:
                print(f"Digite um valor entre {minimo} e {maximo}.")
                numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Só aceitamos números.")
 
def limpaPlaca(texto):
    placa = texto.replace(" ", "").replace("-", "").upper()
    return placa
 
def buscarVeiculoPorPlaca(catalogo, placa):
    for i in range(len(catalogo)):
        if catalogo[i]["placa"] == placa:
            return catalogo[i]
 
def pedePlaca(catalogo):
    while True:
        placa = limpaPlaca(input("DIGITE A PLACA DO VEÍCULO (ex: ABC1D23): "))
        if len(placa) != 7:
            print("Placa inválida, ela precisa ter 7 caracteres.")
        elif buscarVeiculoPorPlaca(catalogo, placa):
            print("Já existe um veículo cadastrado com essa placa.")
        else:
            return placa
 
def cadastrarVeiculo(catalogo):
    limparTela()
    print("[bold green]-=@ CADASTRO DO VEÍCULO @=-[/bold green]\n")
    placa = pedePlaca(catalogo)
    marca = pedeTexto("DIGITE A MARCA DO VEÍCULO: ").title()
    modelo = pedeTexto("DIGITE O MODELO DO VEÍCULO: ").title()
    ano = pedeInteiro("DIGITE O ANO DO VEÍCULO: ", 1950, 2027)
    cor = pedeTexto("DIGITE A COR DO VEÍCULO: ").capitalize()
    preco = pedeInteiro("DIGITE O PREÇO DO VEÍCULO (em reais, sem centavos): ", 1, 10000000)
    km = pedeInteiro("DIGITE A QUILOMETRAGEM (KM): ", 0, 1000000)
    novo_veiculo = {"placa": placa,
                    "marca": marca,
                    "modelo": modelo,
                    "ano": ano,
                    "cor": cor,
                    "preco": preco,
                    "km": km,
                    "status": "Disponível"}
 
    catalogo.append(novo_veiculo)
    salvarCatalogo(catalogo)
   
    print("\n[bold green]Veículo cadastrado com sucesso![/bold green]")
    print(f"PLACA: [bold red]{placa}[/bold red]")
    enterParaContinuar()
 
def atualizarStatusVeiculo(catalogo):
    limparTela()
    print("[bold green]-=@ ATUALIZAR STATUS DO VEÍCULO @=-[/bold green]\n")
 
    if len(catalogo) == 0:
        print("Nenhum veículo cadastrado até o momento.")
    else:
        placa = limpaPlaca(input("Digite a placa do veículo: "))
        veiculo = buscarVeiculoPorPlaca(catalogo, placa)
        if veiculo:
            print(f"\n{veiculo['placa']} - {veiculo['marca']} {veiculo['modelo']} {veiculo['ano']}")
            print(f"STATUS ATUAL: {veiculo['status']}")
            print("""
Escolha o novo status:
 
    1-Disponível
    2-Reservado
    3-Vendido
    """)
 
            opcao = pedeInteiro("Digite sua opção: ", 1, 3)
 
            match opcao:
                case 1:
                    novo_status = "Disponível"
                case 2:
                    novo_status = "Reservado"
                case 3:
                    novo_status = "Vendido"
 
            status_antigo = veiculo["status"]
            veiculo["status"] = novo_status
            salvarCatalogo(catalogo)
 
            print(f"\n[bold green]Status atualizado:[/bold green] {status_antigo} --> {novo_status}")
        else:
            print("Veículo não encontrado.")
 
    enterParaContinuar()
 
def classificarPreAprovacao(comprometimento):
    if comprometimento <= 0.30:
        resultado = "APROVADO"
    elif comprometimento <= 0.40:
        resultado = "EM ANÁLISE"
    else:
        resultado = "REPROVADO"
    return resultado
 
def simularPreAprovacao(catalogo):
 
    limparTela()
 
    print("[bold green]-=@ SIMULAÇÃO DE FINANCIAMENTO @=-[/bold green]\n")
 
    if len(catalogo) == 0:
        print("Nenhum veículo cadastrado até o momento.")
    else:
        placa = limpaPlaca(input("Digite a placa do veículo: "))
        veiculo = buscarVeiculoPorPlaca(catalogo, placa)
 
        if veiculo:
            print(f"\n{veiculo['marca']} {veiculo['modelo']} {veiculo['ano']} --> R$ {veiculo['preco']}\n")
 
            renda = pedeInteiro("DIGITE A RENDA MENSAL DO CLIENTE (R$): ", 1, 1000000)
            entrada = pedeInteiro("DIGITE O VALOR DA ENTRADA (R$): ", 0, 10000000)
 
            while entrada >= veiculo["preco"]:
                print("A entrada precisa ser menor que o preço do veículo.")
                entrada = pedeInteiro("DIGITE O VALOR DA ENTRADA (R$): ", 0, 10000000)
 
            prazo = pedeInteiro("DIGITE O PRAZO EM MESES (12 a 60): ", 12, 60)
 
            taxa = 0.015
            valor_financiado = veiculo["preco"] - entrada
            total = valor_financiado * (1 + taxa * prazo)
            parcela = total / prazo
            comprometimento = parcela / renda
 
            resultado = classificarPreAprovacao(comprometimento)
            print("\n" + "=" * 40)
            print(f"VALOR FINANCIADO: R$ {valor_financiado}")
            print(f"PARCELA ESTIMADA: R$ {parcela} x {prazo} meses")
            print(f"COMPROMETIMENTO DA RENDA: {comprometimento * 100}%")
             
            match resultado:
                case "APROVADO":
                    print("RESULTADO: [bold green]APROVADO[/bold green]")
                case "EM ANÁLISE":
                    print("RESULTADO: [bold yellow]EM ANÁLISE[/bold yellow]")
                case _:
                    print("RESULTADO: [bold red]REPROVADO[/bold red]")
             
            print("=" * 40)
            print("Simulação com juros simples de 1,5% ao mês, sem valor contratual.")
        else:
            print("Veículo não encontrado.")
             
    enterParaContinuar()
             
           
def exibirMenu():
    limparTela()
    print("=" * 40)
    print("""      
    [bold green]-=@ BEM VINDO À TECHCAR @=-[/bold green]
             
    Escolha uma opção para continuar:
             
    1-Cadastrar veículo
    2-Atualizar status do veículo
    3-Simular financiamento
    4-Sair
                """)
    print("=" * 40)