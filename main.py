import os
from estatistica.correlacao import correlacao
import json

def anoArquivo(nomeArquivo):
  caminhoArquivo = nomeArquivo.split('/')
  anoDoArquivo = caminhoArquivo[2].split('.')[0]

  return int(anoDoArquivo)

def escreverNoArquivo(dicionario):
  with open("resultado.json", "w") as file:
    text = json.dumps(dicionario)
    file.write(text)
    file.close()

def lerArquivoDict(caminho):
  with open(caminho, "r") as file:
    dictString = file.read()

  return json.loads(dictString)

def antesDe2013(nomeArquivo) -> bool:
  if(anoArquivo(nomeArquivo) > 2013):
    return True

  return False

def pesoTotalFilho(nomeArquivo, idadeMae, pesoFilho):
  pesos = {
    "13": [0, 0], "14": [0, 0], "15": [0, 0],
    "16": [0, 0], "17": [0, 0], "18": [0, 0],
    "19": [0, 0]
  }

  with open(nomeArquivo, "r") as file:
    rows = file.readlines()

  for i in range(len(rows)):
    idade = rows[i][idadeMae['posicaoInicial']:idadeMae['posicaoFinal']]
    peso = float(rows[i][pesoFilho['posicaoInicial']:pesoFilho['posicaoFinal']])

    idadeMin = int(idade) >= 13
    idadeMax = int(idade) <= 19

    if(idadeMin and idadeMax):
        if (idade in pesos):
          pesos[idade][0] += peso
          pesos[idade][1] += 1

  dictAntigo = lerArquivoDict("resultado.json")

  for i in range(13, 20):
    dictAntigo[str(i)][0] += pesos[str(i)][0]
    dictAntigo[str(i)][1] += pesos[str(i)][1]

  escreverNoArquivo(dictAntigo)

def analiseArquivo(nomeArquivo, antesDe2013):
  if (antesDe2013): # de 2021 à 2014
    posicaoIdadeMae = {'posicaoInicial': 74, 'posicaoFinal': 76}
    posicaoPesoFilho = {'posicaoInicial': 503, 'posicaoFinal': 507}
    pesoTotalFilho(nomeArquivo, posicaoIdadeMae, posicaoPesoFilho)
  else:# de 2013 à 2006
    posicaoIdadeMae = {'posicaoInicial': 88, 'posicaoFinal': 90}
    posicaoPesoFilho = {'posicaoInicial': 462, 'posicaoFinal': 466}
    pesoTotalFilho(nomeArquivo, posicaoIdadeMae, posicaoPesoFilho)

def processoFilho(numeroProcesso, maxProcessosParalelos, pastas, pastaRaiz) -> dict[int, list[int]]:
  print("Processo %i criado!"%(numeroProcesso+1))

  for i in range(numeroProcesso, len(pastas), maxProcessosParalelos):
    caminhoAtehArquivo = os.path.join(pastaRaiz, pastas[i])
    for j in os.listdir(caminhoAtehArquivo):
      nomeArquivo = os.path.join(caminhoAtehArquivo, j)
      print("Processo %i --> %s"%(numeroProcesso+1, nomeArquivo))
      analiseArquivo(nomeArquivo, antesDe2013(nomeArquivo))

def medias(pesosDict):
  medias = {"13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0}
  for i in range(13, 20):
    medias[str(i)] = pesosDict[str(i)][0] / pesosDict[str(i)][1]

  return medias

def calcularCorrelacao(mediasDict):
  idades = [13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
  mediasPesos = []
  for i in range(13, 20):
    mediasPesos.append(float(mediasDict[str(i)]))

  return correlacao(idades, mediasPesos)


pastaRaiz = input("Digite o nome da pasta raíz: ")
maxProcessosParalelos = int(input("Digite o número de processos: "))
pastas = os.listdir(pastaRaiz)

escreverNoArquivo({
  "13": [0, 0], "14": [0, 0], "15": [0, 0],
  "16": [0, 0], "17": [0, 0], "18": [0, 0],
  "19": [0, 0]
})

for numeroProcesso in range(0, maxProcessosParalelos):
  if(os.fork() == 0):
    processoFilho(numeroProcesso, maxProcessosParalelos, pastas, pastaRaiz)
    exit(0)

for numero in range(0, maxProcessosParalelos):
  os.wait()

dictPesos = lerArquivoDict("resultado.json")
mediasPesos = medias(dictPesos)
correlacaoIdadePeso = calcularCorrelacao(mediasPesos)

print("\n=====================================================")
print("Análise concluída com sucesso!!!\n")
for i in range(13, 20):
  print("Idade %i; Peso total: %.2fg; Peso médio: %.2fg; N: %i"%(
    i, dictPesos[str(i)][0], mediasPesos[str(i)], dictPesos[str(i)][1]
  ))
print("\nCorrelação: %.2f"%(correlacaoIdadePeso))
print("\n=====================================================")