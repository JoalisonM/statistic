# verificar a existência de correlação entre a idade da mãe quando
# adolescente (entre 13 e 19 anos) e o peso do recém nascido

# quebrar o algoritmo em dois de 2021 até 2014 e de 2103 até 2005

import os
from estatistica.correlacao import correlacao

def anoArquivo(nomeArquivo):
  caminhoArquivo = nomeArquivo.split('/')
  anoDoArquivo = caminhoArquivo[2].split('.')
  anoDoArquivo = int(anoDoArquivo[0])

  return anoDoArquivo

def antesDe2013(nomeArquivo) -> bool:
  if(anoArquivo(nomeArquivo) > 2013):
    return True

  return False

def escreverNoArquivo(nomeArquivo, correlacao):
  with open("resultado.txt", "a") as file:
    text = str(anoArquivo(nomeArquivo)) + " --> " + str(correlacao) + "\n\r"
    file.write(text)
    file.close()

def correlacaoIdadeMaexPesoFilho(nomeArquivo, idadeMae, pesoFilho):
  idade = []
  peso = []

  with open(nomeArquivo, "r") as file:
    rows = file.readlines()

  for i in range(len(rows)):
    idadeMin = int(rows[i][idadeMae['posicaoInicial']:idadeMae['posicaoFinal']]) >= 13
    idadeMax = int(rows[i][idadeMae['posicaoInicial']:idadeMae['posicaoFinal']]) <= 19
    if(idadeMin and idadeMax):
      idade.append(float(rows[i][idadeMae['posicaoInicial']:idadeMae['posicaoFinal']]))
      peso.append(float(rows[i][pesoFilho['posicaoInicial']:pesoFilho['posicaoFinal']]))

  resultado = correlacao(idade, peso)

  escreverNoArquivo(nomeArquivo, resultado)

def analiseArquivo(nomeArquivo, antesDe2013):
  if (antesDe2013): # de 2021 à 2014
    posicaoIdadeMae = {'posicaoInicial': 74, 'posicaoFinal': 76}
    posicaoPesoFilho = {'posicaoInicial': 503, 'posicaoFinal': 507}
    correlacaoIdadeMaexPesoFilho(nomeArquivo, posicaoIdadeMae, posicaoPesoFilho)
  else:# de 2013 à 2006
    posicaoIdadeMae = {'posicaoInicial': 88, 'posicaoFinal': 90}
    posicaoPesoFilho = {'posicaoInicial': 462, 'posicaoFinal': 466}
    correlacaoIdadeMaexPesoFilho(nomeArquivo, posicaoIdadeMae, posicaoPesoFilho)

def processoFilho(numeroProcesso, maxProcessosParalelos, pastas, pastaRaiz):
  print("Processo %i criado!"%(numeroProcesso+1))

  for i in range(numeroProcesso, len(pastas), maxProcessosParalelos):
    caminhoAtehArquivo = os.path.join(pastaRaiz, pastas[i])
    for j in os.listdir(caminhoAtehArquivo):
      nomeArquivo = os.path.join(caminhoAtehArquivo, j)
      print("Processo %i --> %s"%(numeroProcesso+1, nomeArquivo))
      analiseArquivo(nomeArquivo, antesDe2013(nomeArquivo))

pastaRaiz = "database"
maxProcessosParalelos = 2
pastas = os.listdir(pastaRaiz)

for numeroProcesso in range(0, maxProcessosParalelos):
  if(os.fork() == 0):
    processoFilho(numeroProcesso, maxProcessosParalelos, pastas, pastaRaiz)
    exit(0)

for numero in range(0, maxProcessosParalelos):
    os.wait()

print("\n====================================================")
print("Análise concluída com sucesso!!!")
print("Abrir o arquivo resultado.txt para ver os resultados")
print("====================================================")