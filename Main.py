import Apresentação as f
 
f.limparTela()
 
catalogo = f.carregarCatalogo()
 
while True:
    f.exibirMenu()
 
    try:
        menu = int(input("Digite sua opção: "))
 
        match menu:
            case 1:
                f.cadastrarVeiculo(catalogo)
            case 2:
                f.atualizarStatusVeiculo(catalogo)
            case 3:
                f.simularPreAprovacao(catalogo)
            case 4:
                print("SAINDO...")
                break
            case _:
                f.limparTela()
                print("Opção inválida, tente novamente.")
                f.enterParaContinuar()
 
    except ValueError:
        print("Só aceitamos número.")
        f.enterParaContinuar()
 
catalogo = f.carregarCatalogo()
 
while True:
    f.exibirMenu()
 
    try:
        menu = int(input("Digite sua opção: "))
 
        match menu:
            case 1:
                f.cadastrarVeiculo(catalogo)
            case 2:
                f.atualizarStatusVeiculo(catalogo)
            case 3:
                f.simularPreAprovacao(catalogo)
            case 4:
                print("SAINDO...")
                break
            case _:
                f.limparTela()
                print("Opção inválida, tente novamente.")
                f.enterParaContinuar()
 
    except ValueError:
        print("Só aceitamos número.")
        f.enterParaContinuar()