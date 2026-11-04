print("\nBem-vindo(a) ao sistema de pedidos de Açaí! Meu nome é Gabriel Oliveira.")

print("---------------------------------Cardápio-------------------------------")
print("\n• Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;")
print("• Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;")
print("• Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;")

acumulador = 0  # Inicializa o acumulador para somar os valores dos pedidos

while True:
    sabor = str(input("\nDigite o sabor desejado (CP/AC): ")).upper()  # Solicita o sabor do açaí e converte para maiúsculo
    if sabor != "CP" and sabor != "AC":  
        print("Sabor inválido. Tente novamente")
        continue  # Retorna ao início do loop caso o sabor seja inválido
    elif sabor == "CP":  
        tamanho = str(input("Digite o tamanho desejado (P/M/G): ")).upper() 
        if tamanho != "P" and tamanho != "M" and tamanho != "G":
            print("Tamanho inválido. Tente novamente")
            continue  # Retorna ao início do loop caso o tamanho seja inválido
        if tamanho == "P":
            preco = 9
        elif tamanho == "M":
            preco = 14
        else:
            preco = 18

    elif sabor == "AC":  
          tamanho = str(input("Digite o tamanho desejado (P/M/G): ")).upper()
          if tamanho != "P" and tamanho != "M" and tamanho != "G":
                print("Tamanho inválido. Tente novamente")
                continue  
          if tamanho == "P":  
                preco = 11  
          elif tamanho == "M":  
                preco = 16  
          else:  
                preco = 20
                    
    acumulador += preco  # Adiciona o preço do pedido ao acumulador

    print(f"\nO preço do pedido é: R${preco:.2f}")  
    
    continuar = str(input("\nDeseja pedir mais alguma coisa? (S/N): ")).upper()
    if continuar == "S":
        continue  # Continua o loop para permitir novos pedidos
    elif continuar == "N":
        print("\nObrigado por utilizar nosso sistema de pedidos! O valor total dos seus pedidos é: R${:.2f}".format(acumulador))
        break  # Sai do loop caso o usuário não queira fazer mais pedidos
    else:
        print("Opção inválida. Encerrando o programa.")
        break   




