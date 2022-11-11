import pandas as pd;
import numpy as np

with open('species_PdNiO.out') as f:
    content = f.readlines()
content = [x.strip('\n') for x in content]
content = [x.strip('#') for x in content]
matriz = []

def criar_tabela():
    colunas = "Timestep No_Moles No_Specs O O2"

    colunas = colunas.split()

    tabela = pd.DataFrame(matriz, columns=colunas)
    cont = 1
    list_colunas = []

    for line in content:
        list_linha = []
        if (cont % 2 != 0):
            linha = line.split()
            Time = linha.index("Timestep")
            space = linha.index("No_Specs")
            if "No_Moles" in linha:

                Nmoles = linha.index('No_Moles')
            else:
                Nmoles = 'null'
            if "O" in linha:
                O = linha.index('O')
            else:
                O = 'null'
            if "O2" in linha:
                OD = linha.index('O2')
            else:
                OD = 'null'

        if (cont % 2 == 0):
            linha = line.split()
            list_linha.append(linha[Time])
            if Nmoles == 'null':
                list_linha.append('null')

            else:
                list_linha.append(linha[Nmoles])


            list_linha.append(linha[space])
            if O == 'null':
                list_linha.append('null')
            else:
                list_linha.append(linha[O])

            if OD == 'null':
                list_linha.append('null')
            else:
                list_linha.append(linha[OD])
            df_new_row = pd.DataFrame({'Timestep': [list_linha[0]], 'No_Moles': [list_linha[1]],'No_Specs':list_linha[2],'O':list_linha[3],'O2':list_linha[4]})
            tabela = pd.concat([tabela, df_new_row])

        cont += 1
    print(tabela)

    tabela.to_excel('Species_formatado.xlsx')




criar_tabela()

