
print("\n\t***** Censo IBGE 2023 *****\n\n")
maior = float("-inf")
cidade_maior = ()
menor = float("-inf")
cidade_menor = ()
nun_veiculos = 0
acid = 0
num_media = 0

num_cidades = int(input("Digite quantidade de cidades, a ser verificada?\n"))
for censo in range(num_cidades):
    cidade = input(f"Digige o nome da cidade?{censo + 1}\n")
    num_acidentes = float(input(f"Informe, o número de acidentes?#{censo + 1}\n"))
    veiculo = float(input(f"Informe, o número de veiculos?\n"))

    if num_acidentes > maior:
        maior = num_acidentes
        cidade_maior = cidade

    if num_acidentes < maior:
        menor = num_acidentes
        cidade_menor = cidade

    nun_veiculos = nun_veiculos + veiculo
    media = nun_veiculos/num_cidades

    num_media += 1

    if num_acidentes < 2000:
        acid = acid + num_acidentes
        med_acident = acid/num_media




print("{} é a cidade com maior índice, {} acidentes com vítimas.\n".format(cidade_maior,maior))
print("{} é a cidade com menor índice, {} acidentes com vítimas.\n".format(cidade_menor, menor))
print("A média de veiculos é nas cidades juntas é {}.\n".format(media))
print("A média de acidentes nas cidades com menos de 2000 veículos é {}".format(med_acident))