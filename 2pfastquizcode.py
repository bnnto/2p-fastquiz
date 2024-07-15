import RPi.GPIO as GPIO
from time import sleep
import random

# Definir modo GPIO
GPIO.setmode(GPIO.BOARD)

# Definir pinos GPIO
botao1 = 36
botao2 = 35
led1 = 38
led2 = 37

# Configurar pinos GPIO
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(botao1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Pontuação dos jogadores
pontuacao_jogador1 = 0
pontuacao_jogador2 = 0

# Perguntas e respostas
perguntas = [
    {"pergunta": "Qual é a capital da França?", "resposta": "Paris"},
    {"pergunta": "Quanto é 2 + 2?", "resposta": "4"},
    {"pergunta": "Qual é a cor do céu em um dia claro?", "resposta": "Azul"},
    {"pergunta": "Qual a raiz quadrada de 16?", "resposta": "4"},
    {"pergunta": "O complemento da frase matemática: ordem dos fatores não altera o", "resposta": "produto"},
    {"pergunta": "Qual o nome do filo ao qual o ser humano pertence", "resposta": "cordados"},
    {"pergunta": "Qual o primeiro grupo de animais a dominarem efetivamente o ambiente terrestre", "resposta": "répteis"},
    {"pergunta": "Qual o primeiro grupo de animais a irem para a terra, não de maneira a dominarem esse ambiente", "resposta": "anfíbios"},
    {"pergunta": "PERGUNTA BONUS!: Qual o nome da melhor professora do mundo", "resposta": "Ivna"},
]

# Função para determinar a ordem dos jogadores
def determinar_ordem():
    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)
    while True:
        if GPIO.input(botao1) == GPIO.HIGH:
            GPIO.output(led1, GPIO.HIGH)
            return 1
        elif GPIO.input(botao2) == GPIO.HIGH:
            GPIO.output(led2, GPIO.HIGH)
            return 2

try:
    for pergunta_atual in perguntas:
        # Mostrar o timer antes da pergunta
        print("A próxima pergunta aparecerá em:")
        for i in range(5, 0, -1):
            print(i)
            sleep(1)

        # Exibir a pergunta
        print("Pergunta: " + pergunta_atual["pergunta"])

        # Determinar a ordem dos jogadores
        ordem = determinar_ordem()
        sleep(1)  # Esperar um pouco antes de solicitar a resposta

        # Pedir resposta ao jogador que apertou primeiro
        resposta = input("Jogador {}: ".format(ordem))

        # Verificar se a resposta está correta
        if resposta.strip().lower() == pergunta_atual["resposta"].strip().lower():
            if ordem == 1:
                pontuacao_jogador1 += 1
            else:
                pontuacao_jogador2 += 1
            print("Resposta correta!")
        else:
            print("Resposta errada!")

        # Mostrar pontuação
        print("Pontuação Jogador 1: ", pontuacao_jogador1)
        print("Pontuação Jogador 2: ", pontuacao_jogador2)
        print("\n")

    # Determinar o vencedor
    if pontuacao_jogador1 > pontuacao_jogador2:
        print("Jogador 1 venceu!")
    elif pontuacao_jogador2 > pontuacao_jogador1:
        print("Jogador 2 venceu!")
    else:
        print("Empate!")

finally:
    GPIO.cleanup()
    print('GPIO cleanup complete')