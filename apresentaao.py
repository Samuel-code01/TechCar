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
            
def buscarVeiculoPorPlaca(catalogo,placa):
    for i in range(len(catalogo)):
        if catalogo[i] ["Placa"] == placa:
            return catalogo[i]
        
        
def pedePlaca(catalogo):
    while True:
        placa = limpaPlaca(input("Digite a Placa do Veiculo (ex: exx4A22): "))
        if len(placa) != 7:
            print("Placa invalida,ela precisa ter 7 caracteries ")
        elif buscarVeiculoPorPlaca(catalogo,placa):
            print("Ja existe um veiculo Cadastrado nessa placa")
        else:
            return placa
        
        
def cadastrarVeiculo(catalogo):
    limparTela ()
    print("Cadastro do Veiculo")
    
    
    placa = pedePlaca(catalogo)
    marca = pedeTexto("Digite a Marca do Veiculo")
    modelo = pedeTexto("DIGITE O MODELO DO VEÍCULO: ").title()
    ano = pedeInteiro("DIGITE O ANO DO VEÍCULO: ", 1950, 2027)
    cor = pedeTexto("DIGITE A COR DO VEÍCULO: ").capitalize()
    preco = pedeInteiro("Digite o preco do veiculo em (reais, sem centavos): ", 40000 , 3000000)
    km = pedeInteiro("Digite a Quilometragem (km) ", 0, 2500000  )
    
    
    novo_veiculo = {"Placa": placa
                    
                    
                    
                    
                    
                    
                    
                    
                    }
    
    
    
        
        
        
        
    
            
           
    