dictLado ={
    "S":0,
    "L":-1,
    "R":1,
}

def verificasaida(cadeia,Estados,SimbolosTerminais,Simbolos,estadoAceitacao,transicoes):
    if cadeia[0] == "-":
        if estadoAceitacao == 0:
            return "aceito"
        else:
            return "rejeitado"
    
    else:
        dictTrans = {}
        for trans in transicoes:
            dictTrans.update({
               trans[0]+trans[1] : {
                   "proximoEstado":trans[2],
                   "escreve":trans[3],
                   "direcao":trans[4],
               } 
            })
        cadeiaUsada = ["B"]
        cadeia = cadeia[0]
        for x in cadeia:
            cadeiaUsada.append(x)
            
        cadeiaUsada.append("B")
        estadoAtual = "0"
        index = 1
        contador = 0
        
        try:
            while True:
                leituraAtual =  str(estadoAtual) + cadeiaUsada[index]
                transicaAtual = dictTrans.get(leituraAtual)
                cadeiaUsada[index] = transicaAtual.get("escreve")
                index += dictLado.get(transicaAtual.get("direcao"))
                estadoAtual = transicaAtual.get("proximoEstado")
                if estadoAtual == str(estadoAceitacao):
                    return "aceito"
                elif contador == 1000000:
                    return "rejeitado"
                contador += 1
                # break
        except:
            return "rejeitado"
    

def leEntrada():
    path = "./"
    arquivo = "entrada.txt"

    f = open(path+arquivo,"r")
    loaded = f.read()
    f.close()

    loadedSplit = loaded.split("\n")
    Estado = int(loadedSplit[0])
    Estados = [str(x) for x in range(0,Estado)]
    nSimbolosTerminais = int(loadedSplit[1][0])
    SimbolosTerminais = loadedSplit[1].split(" ")[1:]
    nSimbolos = int(loadedSplit[2][0])
    Simbolos = loadedSplit[2].split(" ")[1:]
    estadoAceitacao = int(loadedSplit[3])
    nTransicoes = int(loadedSplit[4])
    transicoes = []
    for index in range(0,nTransicoes):
        transicoes.append(loadedSplit[5+index].split(" "))
    indexAtual = index+5+1
    nCadeias = int(loadedSplit[indexAtual])
    cadeias = []
    for index in range(0,nCadeias):
            cadeias.append(loadedSplit[indexAtual+1+index].split(" "))
    resultados = []
    for cadeia in cadeias:
        resultados.append(verificasaida(cadeia,Estados,SimbolosTerminais,Simbolos,estadoAceitacao,transicoes))
    
    for x in resultados:
        print(x)
    path = "./"
    arquivo = "saida.txt"
    result = "\n".join(resultados)
    f = open(path+arquivo,"w")
    f.writelines(result)
    f.close()


if __name__ == '__main__':
    leEntrada()
    