a=1
n=1
e=1
#DIREITA
def paraDireita(passos, erro):
    motor1i.off()
    motor2.off()
    motor3.off()
    motor4i.off()
#ESQUERDA
def paraEsquerda(passos, erro):
    motor1.off()
    motor2i.off()
    motor3i.off()
    motor4.off()
#BAIXO
def paraBaixo(passos, erro):
    motor1i.off()
    motor2i.off()
    motor3i.off()
    motor4i.off()
#CIMA
def paraCima(passos, erro):
    motor1.off()
    motor2.off()
    motor3.off()
    motor4.off()
#90º Horário
def noventaGrausHorario(passos, erro):
    motor1.off()
    motor2i.off()
    motor3.off()
    motor4i.off()
#90º Anti-horário
def noventaGrausAntiHorario(passos, erro):
    motor1i.off()
    motor2.off()
    motor3i.off()
    motor4.off()


#CHAMANDO FUNÇÕES

#INICIO(SAÍDA COM ELEVADOR PARA ESQUERDA)

paraDireita(passos,erro)
#ALINHA COM LINHA VERDE
paraBaixo(passos,erro)
#DESCE ATÉ ENCONTRAR QUINA
noventaGrausHorario(passos,erro)
#ANDA ATÉ OS 3 INFRA ENCONTRAREM ALGUM CONTEINER
paraCima(passos,erro)
#ABAIXA ELEVADOR E LÊ COR 
#BUSCA VARIÁVEIS  'a' e 'v'

if e>0:
    #PEGA CONTEINER
    paraBaixo(passos, erros)
    paraEsquerda(passos,erros)
    noventaAntiHorario(passos,erros)
    paraCima(passos,erros)
    paraEsquerda(passos,erros)
    if n>0:
        #ALINHA COM OUTROS CONTEINER
    elif n==0:
        #NÃO FAZ NADA
        #DESCE O ELEVADOR E DEPOSITA
#VOLTA PARA "SEGUE PARA DIREITA ATÉ A LINHA VERDE (PRIMEIRO PASSO)"

elif e==0:
    paraBaixo(passos,erros)
    paraDireita(passos,erros)
    #ANDA ATÉ OS 3 INFRA ENCONTRAREM ALGUM CONTEINER
    paraCima(passos,erros)
    #ABAIXA O ELEVADOR E LÊ A COR
    paraBaixo(passos,erros)
    paraDireita(passos,erros)
    noventaGrausHorario(passos,erros)
    paraCima(passos,erros)
    paraDireita(passos,erros)
    paraEsquerda(passos,erros)
    paraBaixo(passos,erros)
    noventaAntiHorario(passos,erros)
    paraEsquerda(passos,erros)
#VOLTA PARA "ANDA ATÉ OS INFRA ENCONTRAREM ALGUM CONTEINER"
