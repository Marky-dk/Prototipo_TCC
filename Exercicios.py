# importando as bibliotecas
import cv2
import numpy as np
from terEx8 import TerEx8
from segEx9 import SegEx9
from sexEx5 import SexEx5

# Carregando os modelos e estruturas da rede neural pré-treinados
arquivo_proto = '/home/marky/Documents/Curso_openCV/pose/pose/body/mpi/pose_deploy_linevec_faster_4_stages.prototxt'
arquivo_pesos = '/home/marky/Documents/Curso_openCV/pose/pose/body/mpi/pose_iter_160000.caffemodel'

numero_pontos = 15
pares_pontos = [[0, 1], [1, 2], [2, 3], [3, 4], [1, 5], [5, 6], [6, 7], [1, 14], [14, 8], [8, 9], [9, 10], [14, 11],
                [11, 12], [12, 13]]

cor_pontoA, cor_pontoB, cor_linha = (14, 201, 255), (255, 0, 128), (192, 192, 192)
cor_txtponto, cor_txtinicial, cor_txtandamento = (10, 216, 245), (255, 0, 128), (192, 192, 192)

tamanho_fonte, tamanho_linha, tamanho_circulo, espessura = 0.8, 2, 8, 5
fonte = cv2.FONT_HERSHEY_SIMPLEX

# Definindo variáveis condicionais
valida_pernas_juntas = 0
valida_bracos_abaixo, valida_bracos_acima = 0, 0
valida_movimento_errado, frame_movimento_errado = 0, 0
valida_quant_movimento1, valida_quant_movimento2 = 0, 0
movimento_valido, valida_movimento2 = 0, 0
valida_movimento, temp_frame = 0, 0

# Definindo as dimensões da imagem e entrada
entrada_largura = 256
entrada_altura = 256

# Carregado o vídeo da maquina local
caminho_video = input("Informe o nome do vídeo: ")
video = '/home/marky/Documents/'
video = video + caminho_video
captura = cv2.VideoCapture(video)
conectado, frame = captura.read()

# Criando a variável para salvar os resultados
nomeVideo = input("Como quer salvar seu vídeo? ")
resultado = "./" + nomeVideo + ".avi"
gravar_video = cv2.VideoWriter(resultado, cv2.VideoWriter_fourcc(*'XVID'), 10, (frame.shape[1], frame.shape[0]))

# Criando variável para o modelo carregado
modelo = cv2.dnn.readNetFromCaffe(arquivo_proto, arquivo_pesos)

# Criando seleção de exercícios
numero_escolhido = input(
    "Digite (1) para o exercício 9 de segunda, (2) para o exercício 8 de terça e (3) para o exercício 5 de sexta: ")
exercicio_escolhido = int(numero_escolhido)

# Criando a saída para o exercício 9 de segunda
if exercicio_escolhido == 1:
    limite = 0.1
    while (cv2.waitKey(1) < 0):

        conectado, video = captura.read()

        video_copia = np.copy(video)

        if not conectado:
            cv2.waitKey()
            break

        video_largura = video.shape[1]
        video_altura = video.shape[0]

        # Criação da máscara com fundo preto
        tamanho = cv2.resize(video, (video_largura, video_altura))
        mapa_suave = cv2.GaussianBlur(tamanho, (3, 3), 0, 0)
        fundo = np.uint8(mapa_suave > limite)

        # Conversão do tipo da imagem
        blob_entrada = cv2.dnn.blobFromImage(video, 1.0 / 255, (entrada_largura, entrada_altura), (0, 0, 0),
                                             swapRB=False,
                                             crop=False)

        modelo.setInput(blob_entrada)
        saida = modelo.forward()

        altura = saida.shape[2]
        largura = saida.shape[3]

        # Adicionando pontos chaves do corpo
        pontos = []
        for i in range(numero_pontos):
            mapa_confianca = saida[0, i, :, :]
            _, confianca, _, ponto = cv2.minMaxLoc(mapa_confianca)

            x = (video_largura * ponto[0]) / largura
            y = (video_altura * ponto[1] / altura)

            if confianca > limite:
                cv2.circle(video_copia, (int(x), int(y)), 4, cor_pontoB, thickness=tamanho_circulo, lineType=cv2.FILLED)
                cv2.putText(video_copia, "{}".format(i), (int(x), int(y)), fonte, tamanho_fonte, cor_txtponto, 3,
                            lineType=cv2.LINE_AA)
                cv2.putText(fundo, " ", (int(x), int(y)), fonte, tamanho_fonte, cor_txtponto, 3, lineType=cv2.LINE_AA)

                pontos.append((int(x), int(y)))
            else:
                pontos.append((0, 0))

        # Desenho do esqueleto
        for par in pares_pontos:
            parteA = par[0]
            parteB = par[1]

            if pontos[parteA] and pontos[parteB]:
                cv2.line(video, pontos[parteA], pontos[parteB], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
                cv2.line(video_copia, pontos[parteA], pontos[parteB], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
                cv2.line(fundo, pontos[parteA], pontos[parteB], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)

                cv2.circle(video, pontos[parteA], 4, cor_pontoA, thickness=espessura, lineType=cv2.FILLED)
                cv2.circle(video, pontos[parteB], 4, cor_pontoA, thickness=espessura, lineType=cv2.FILLED)
                cv2.circle(fundo, pontos[parteA], 4, cor_pontoA, thickness=espessura, lineType=cv2.FILLED)
                cv2.circle(fundo, pontos[parteB], 4, cor_pontoA, thickness=espessura, lineType=cv2.FILLED)

        # Verifica se o usuário está na posição inicial
        if SegEx9.verificar_cabeca_CENTRO(pontos[0:8]) == True:
            frame_movimento_errado = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Braco: Posicao inicial", (50, 50), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)
        # Verifica cabeça para esquerda
        elif SegEx9.verificar_cabeca_ESQUERDA(pontos[0:8]) == True:
            valida_movimento = 0.5
            frame_movimento_errado = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Bracos: Posicao final esquerda", (50, 50), fonte, tamanho_fonte, cor_txtinicial,
                        0,
                        lineType=cv2.LINE_AA)
        # Verifica cabeça para direita
        elif SegEx9.verificar_cabeca_DIREITA(pontos[0:8]) == True:
            if valida_movimento == 0.5:
                valida_movimento = 1
            frame_movimento_errado = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Bracos: Posicao final direita", (50, 50), fonte, tamanho_fonte, cor_txtinicial,
                        0,
                        lineType=cv2.LINE_AA)
        # Validando posição errada
        elif SegEx9.verificar_movimento_ERRADO(pontos[0:8]) == True:
            # movimento errado
            if frame_movimento_errado < 3:
                frame_movimento_errado += 1

            elif frame_movimento_errado == 3:
                valida_movimento_errado = 1
                cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
                cv2.putText(video_copia, " Bracos: Movimento Errado", (50, 50), fonte, tamanho_fonte, cor_txtinicial, 0,
                            lineType=cv2.LINE_AA)

        # Analisando movimento em andamento
        else:
            if valida_movimento == 1:
                temp_frame = temp_frame + 1
                if temp_frame > 5:
                    valida_movimento = 0
            frame_movimento_errado = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Bracos: em andamento", (50, 50), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)

        # Validando posição final - pernas
        if SegEx9.verificar_pernas_JUNTAS(pontos[8:14]) == True:
            # 50% do movimento
            valida_movimento2 = 1
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Pernas: Posicao final", (50, 70), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)

        # Validando movimento errado
        else:
            valida_movimento2 = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Pernas: Movimento errado", (50, 70), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)

        # Validar exercício completo
        if valida_movimento == 1 and valida_movimento2 == 1:
            cv2.putText(video_copia, " Exercicio valido",
                        (50, 200), fonte, tamanho_fonte, cor_txtinicial, 0, lineType=cv2.LINE_AA)

        # Validar movimeno feito de forma errada
        elif valida_movimento_errado == 1:
            cv2.putText(video_copia, " Exercicio errado ", (50, 200), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)
            valida_movimento_errado = 0

        # Escolhendo o estilo da saída
        cv2.imshow("", video_copia)
        # cv2_imshow(video)
        # cv2_imshow(fundo)

        # Salvando resultado
        gravar_video.write(video_copia)

# Criando a saída para o exercício 8 de terça
elif exercicio_escolhido == 2:
    limite = 0.1
    while (cv2.waitKey(1) < 0):

        conectado, video = captura.read()

        video_copia = np.copy(video)

        if not conectado:
            cv2.waitKey()
            break

        video_largura = video.shape[1]
        video_altura = video.shape[0]

        # Criação da máscara com fundo preto
        tamanho = cv2.resize(video, (video_largura, video_altura))
        mapa_suave = cv2.GaussianBlur(tamanho, (3, 3), 0, 0)
        fundo = np.uint8(mapa_suave > limite)

        # Conversão do tipo da imagem
        blob_entrada = cv2.dnn.blobFromImage(video, 1.0 / 255, (entrada_largura, entrada_altura), (0, 0, 0),
                                             swapRB=False,
                                             crop=False)

        modelo.setInput(blob_entrada)
        saida = modelo.forward()

        altura = saida.shape[2]
        largura = saida.shape[3]

        # Adicionando pontos chaves do corpo
        pontos = []
        for i in range(numero_pontos):
            mapa_confianca = saida[0, i, :, :]
            _, confianca, _, ponto = cv2.minMaxLoc(mapa_confianca)

            x = (video_largura * ponto[0]) / largura
            y = (video_altura * ponto[1] / altura)

            if confianca > limite:
                cv2.circle(video_copia, (int(x), int(y)), 4, cor_pontoB, thickness=tamanho_circulo, lineType=cv2.FILLED)
                cv2.putText(video_copia, "{}".format(i), (int(x), int(y)), fonte, tamanho_fonte, cor_txtponto, 3,
                            lineType=cv2.LINE_AA)
                cv2.putText(fundo, " ", (int(x), int(y)), fonte, tamanho_fonte, cor_txtponto, 3, lineType=cv2.LINE_AA)

                pontos.append((int(x), int(y)))
            else:
                pontos.append((0, 0))

        # Desenho do esqueleto
        for par in pares_pontos:
            parteA = par[0]
            parteB = par[1]

            if pontos[parteA] and pontos[parteB]:
                cv2.line(video, pontos[parteA], pontos[parteB], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
                cv2.line(video_copia, pontos[parteA], pontos[parteB], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
                cv2.line(fundo, pontos[parteA], pontos[parteB], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)

                cv2.circle(video, pontos[parteA], 4, cor_pontoA, thickness=espessura, lineType=cv2.FILLED)
                cv2.circle(video, pontos[parteB], 4, cor_pontoA, thickness=espessura, lineType=cv2.FILLED)
                cv2.circle(fundo, pontos[parteA], 4, cor_pontoA, thickness=espessura, lineType=cv2.FILLED)
                cv2.circle(fundo, pontos[parteB], 4, cor_pontoA, thickness=espessura, lineType=cv2.FILLED)

        # Validando posição inicial - braços
        if TerEx8.verificar_bracos_ABAIXO(pontos[0:8]) == True:
            # 25% do movimento concluído
            valida_bracos_abaixo = 0.25
            frame_movimento_errado = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Braco: Posicao inicial", (50, 50), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)
            if valida_quant_movimento1 == 0:
                valida_quant_movimento2 = 1
                valida_quant_movimento1 = 1
        # Validando posição final - braços
        elif TerEx8.verificar_bracos_ACIMA(pontos[0:8]) == True:
            # 50% do movimento concluído
            valida_bracos_acima = 0.5
            frame_movimento_errado = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Bracos: Posicao final", (50, 50), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)
            if valida_quant_movimento2 == 1:
                movimento_valido = movimento_valido + 1
                valida_quant_movimento2 = 0
                valida_quant_movimento1 = 0
        # Validando posição errada - braços
        elif TerEx8.verificar_bracos_ERRADO(pontos[0:8]) == True:
            # movimento errado
            if frame_movimento_errado < 3:
                frame_movimento_errado += 1

            elif frame_movimento_errado == 3:
                valida_movimento_errado = 1
                cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
                cv2.putText(video_copia, " Bracos: Movimento Errado", (50, 50), fonte, tamanho_fonte, cor_txtinicial, 0,
                            lineType=cv2.LINE_AA)

        # Analisando movimento em andamento - braços
        else:
            valida_bracos_abaixo = 0
            valida_bracos_acima = 0
            frame_movimento_errado = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Bracos: em andamento", (50, 50), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)

        # Validando posição final - pernas
        if TerEx8.verificar_pernas_JUNTAS(pontos[8:14]) == True:
            # 50% do movimento
            valida_pernas_juntas = 0.5
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Pernas: Posicao final", (50, 70), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)

        # Validando movimento errado
        else:
            valida_pernas_afastadas = 0
            valida_pernas_juntas = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Pernas: Movimento errado", (50, 70), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)

        # Validar exercício completo e quantidade feito
        if valida_bracos_acima == 0.5 and valida_pernas_juntas == 0.5:
            cv2.putText(video_copia, " Exercicio valido: " + str(movimento_valido),
                        (50, 200), fonte, tamanho_fonte, cor_txtinicial, 0, lineType=cv2.LINE_AA)

        # Validar movimeno feito de forma errada
        elif valida_movimento_errado == 1:
            cv2.putText(video_copia, " Exercicio errado ", (50, 200), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)
            valida_movimento_errado = 0

        # Escolhendo o estilo da saída
        cv2.imshow("", video_copia)
        # cv2_imshow(video)
        # cv2_imshow(fundo)

        # Salvando resultado
        gravar_video.write(video_copia)

# Criando a saída para o exercício 5 de sexta
elif exercicio_escolhido == 3:
    limite = 0.1
    while (cv2.waitKey(1) < 0):

        conectado, video = captura.read()

        video_copia = np.copy(video)

        if not conectado:
            cv2.waitKey()
            break

        video_largura = video.shape[1]
        video_altura = video.shape[0]

        # Criação da máscara com fundo preto
        tamanho = cv2.resize(video, (video_largura, video_altura))
        mapa_suave = cv2.GaussianBlur(tamanho, (3, 3), 0, 0)
        fundo = np.uint8(mapa_suave > limite)

        # Conversão do tipo da imagem
        blob_entrada = cv2.dnn.blobFromImage(video, 1.0 / 255, (entrada_largura, entrada_altura), (0, 0, 0),
                                             swapRB=False,
                                             crop=False)

        modelo.setInput(blob_entrada)
        saida = modelo.forward()

        altura = saida.shape[2]
        largura = saida.shape[3]

        # Adicionando pontos chaves do corpo
        pontos = []
        for i in range(numero_pontos):
            mapa_confianca = saida[0, i, :, :]
            _, confianca, _, ponto = cv2.minMaxLoc(mapa_confianca)

            x = (video_largura * ponto[0]) / largura
            y = (video_altura * ponto[1] / altura)

            if confianca > limite:
                cv2.circle(video_copia, (int(x), int(y)), 4, cor_pontoB, thickness=tamanho_circulo, lineType=cv2.FILLED)
                cv2.putText(video_copia, "{}".format(i), (int(x), int(y)), fonte, tamanho_fonte, cor_txtponto, 3,
                            lineType=cv2.LINE_AA)
                cv2.putText(fundo, " ", (int(x), int(y)), fonte, tamanho_fonte, cor_txtponto, 3, lineType=cv2.LINE_AA)

                pontos.append((int(x), int(y)))
            else:
                pontos.append((0, 0))

        # Desenho do esqueleto
        for par in pares_pontos:
            parteA = par[0]
            parteB = par[1]

            if pontos[parteA] and pontos[parteB]:
                cv2.line(video, pontos[parteA], pontos[parteB], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
                cv2.line(video_copia, pontos[parteA], pontos[parteB], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
                cv2.line(fundo, pontos[parteA], pontos[parteB], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)

                cv2.circle(video, pontos[parteA], 4, cor_pontoA, thickness=espessura, lineType=cv2.FILLED)
                cv2.circle(video, pontos[parteB], 4, cor_pontoA, thickness=espessura, lineType=cv2.FILLED)
                cv2.circle(fundo, pontos[parteA], 4, cor_pontoA, thickness=espessura, lineType=cv2.FILLED)
                cv2.circle(fundo, pontos[parteB], 4, cor_pontoA, thickness=espessura, lineType=cv2.FILLED)

        # Verifica Posição inicial - superior
        if SexEx5.verificar_bracos_ESTICADOS(pontos[0:15]) == True:
            valida_movimento = 0
            frame_movimento_errado = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Braco: Posicao inicial", (50, 50), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)
        # Verifica posição final - superior
        elif SexEx5.verificar_bracos_DESCENDO(pontos[0:15]) == True:
            valida_movimento = 0
            frame_movimento_errado = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Bracos: Posicao final", (50, 50), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)
        # Verifica movimento errado
        elif SexEx5.verificar_movimento_ERRADO(pontos[0:15]) == True:
            if frame_movimento_errado < 3:
                frame_movimento_errado += 1

            elif frame_movimento_errado == 3:
                valida_movimento_errado = 1
                cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
                cv2.putText(video_copia, " Bracos: Movimento Errado", (50, 50), fonte, tamanho_fonte, cor_txtinicial, 0,
                            lineType=cv2.LINE_AA)
        # Verifica movimeno em andamento - superior
        else:
            valida_movimento = 0
            frame_movimento_errado = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Bracos: em andamento", (50, 50), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)
        # Verifica movimento inicial - inferior
        if SexEx5.verificar_pernas_ESTICADAS(pontos[0:15]) == True:
            valida_movimento2 = 0
            frame_movimento_errado = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Pernas: Posicao incial", (50, 70), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)
        # Verifica movimento final - inferior
        if SexEx5.verificar_pernas_DESCENDO(pontos[0:15]) == True:
            valida_movimento2 = 1
            frame_movimento_errado = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Pernas: Posicao final", (50, 70), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)
        # Verifica movimento em andamento - inferior
        else:
            valida_movimento2 = 0
            frame_movimento_errado = 0
            cv2.line(video_copia, pontos[0], pontos[1], cor_linha, tamanho_linha, lineType=cv2.LINE_AA)
            cv2.putText(video_copia, " Pernas: em andamento", (50, 70), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)
        # Valida exercício
        if valida_movimento == 1 and valida_movimento2 == 1:
            cv2.putText(video_copia, " Exercicio valido",
                        (50, 200), fonte, tamanho_fonte, cor_txtinicial, 0, lineType=cv2.LINE_AA)

        # Valida movimento errado
        elif valida_movimento_errado == 1:
            cv2.putText(video_copia, " Exercicio errado ", (50, 200), fonte, tamanho_fonte, cor_txtinicial, 0,
                        lineType=cv2.LINE_AA)
            valida_movimento_errado = 0

        # Escolhendo o estilo da saída
        cv2.imshow("", video_copia)
        # cv2_imshow(video)
        # cv2_imshow(fundo)

        # Salvando resultado
        gravar_video.write(video_copia)

else:
    print("opção invalida!")

gravar_video.release()
