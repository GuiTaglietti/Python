#Teste pandas e numpy para a semana do conhecimento e apresentação ao Eder
#Melhorar coisas a serem discutidas na reunião e dados a serem usados
#A base de dados foi criada por mim e é apenas um teste para ser apresentada em análise

#Importar bibliotecas

import numpy as np
import pandas as pd

#Faz o computador ler os dados a serem analisados

dataFrame = pd.read_excel("C:/Users/Gui/Downloads/TestePandas.xlsx") #dataFrame é o nome escolhido para a base de dados
                                                                     #a ser usada, pode ser qualquer outro nome de preferência
#Usa a função "print(ALGO A SER MOSTRADO)" para
#exibir o que queremos na tela para o usuário
    
print(dataFrame)
print(dataFrame.plot(kind = "bar", x = "Nome-do-aluno", figsize = (10, 10)))

#Após tudo isso, o resultado é o que conferimos abaixo:
