class TerEx8:
    pontos = []

    # Validando posição final - superior
    def verificar_bracos_ACIMA(pontos):
        # declarando variáveis dos pontos
        cabeca_V = 0
        punhoEsquerdo_H = 0
        punhoEsquerdo_V = 0
        ombroEsquerdo_H = 0
        cotoveloEsquerdo_H = 0
        punhoDireito_H = 0
        punhoDireito_V = 0
        ombroDireito_H = 0
        cotoveloDireito_H = 0

        for indx, p in enumerate(pontos):
            # p[0] é na horizontal
            # p[1] é na vertical
            if indx == 0:
                cabeca_V = p[1]
            elif indx == 2:
                ombroDireito_H = p[0]
            elif indx == 3:
                cotoveloDireito_H = p[0]
            elif indx == 4:
                punhoDireito_H = p[0]
                punhoDireito_V = p[1]
            elif indx == 5:
                ombroEsquerdo_H = p[0]
            elif indx == 6:
                cotoveloEsquerdo_H = p[0]
            elif indx == 7:
                punhoEsquerdo_H = p[0]
                punhoEsquerdo_V = p[1]

        # quanto menor a posição da altura, mais alto o ponto está
        # quanto maior a posição da altura, mais baixo o ponto está
        if punhoEsquerdo_V and punhoDireito_V < cabeca_V:
            if (punhoEsquerdo_H >= ombroEsquerdo_H) and (punhoDireito_H <= ombroDireito_H):
                if (cotoveloEsquerdo_H >= ombroEsquerdo_H) and (cotoveloDireito_H <= ombroDireito_H):
                    if punhoEsquerdo_V == punhoDireito_V:
                        return True
        else:
            return False

    # Validando posição errada - superior
    def verificar_bracos_ERRADO(pontos):
        # declarando variáveis dos pontos
        cabeca_V = 0
        pescoco_V = 0
        punhoEsquerdo_V = 0
        punhoDireito_V = 0

        for indx, p in enumerate(pontos):
            # p[0] é na horizontal
            # p[1] é na vertical
            if indx == 0:
                cabeca_V = p[1]
            elif indx == 1:
                pescoco_V = p[1]
            elif indx == 4:
                punhoDireito_V = p[1]
            elif indx == 7:
                punhoEsquerdo_V = p[1]

        # quanto menor a posição da altura, mais alto o ponto está
        # quanto maior a posição da altura, mais baixo o ponto está
        if punhoEsquerdo_V != punhoDireito_V:
            if punhoEsquerdo_V < pescoco_V and punhoDireito_V >= pescoco_V:
                return True

            elif punhoEsquerdo_V >= pescoco_V and punhoDireito_V < pescoco_V:
                return True

            elif punhoEsquerdo_V < cabeca_V and punhoDireito_V >= cabeca_V:
                return True

            elif punhoEsquerdo_V >= cabeca_V and punhoDireito_V < cabeca_V:
                return True
        else:
            return False

    # Validando posição inicial - superior
    def verificar_bracos_ABAIXO(pontos):
        # declarando variáveis dos pontos
        punhoEsquerdo_H = 0
        punhoEsquerdo_V = 0
        ombroEsquerdo_H = 0
        ombroEsquerdo_V = 0
        cotoveloEsquerdo_H = 0
        cotoveloDireito_H = 0
        punhoDireito_H = 0
        punhoDireito_V = 0
        ombroDireito_H = 0
        ombroDireito_V = 0

        for indx, p in enumerate(pontos):
            # p[0] é na horizontal
            # p[1] é na vertical
            if indx == 2:
                ombroDireito_H = p[0]
                ombroDireito_V = p[1]
            elif indx == 3:
                cotoveloDireito_H = p[0]
            elif indx == 4:
                punhoDireito_V = p[1]
            elif indx == 5:
                ombroEsquerdo_H = p[0]
                ombroEsquerdo_V = p[1]
            elif indx == 6:
                cotoveloEsquerdo_H = p[0]
            elif indx == 7:
                punhoEsquerdo_V = p[1]
                punhoEsquerdo_H = p[0]

        # quanto menor a posição da altura, mais alto o ponto está
        # quanto maior a posição da altura, mais baixo o ponto está
        if (punhoEsquerdo_V >= ombroEsquerdo_V) and (punhoDireito_V >= ombroDireito_V):
            if (punhoEsquerdo_H >= ombroEsquerdo_H) and (punhoDireito_H <= ombroDireito_H):
                if (punhoEsquerdo_H >= cotoveloEsquerdo_H) and (punhoDireito_H <= cotoveloDireito_H):
                    if punhoEsquerdo_V == punhoDireito_V:
                        return True
        else:
            return False

    #Validando posição final - inferior
    def verificar_pernas_JUNTAS(pontos):
        # declarando variáveis dos pontos
        tornozeloEsquerdo_H = 0
        tornozeloDireito_H = 0
        quadrilEsquerdo_H = 0
        quadrilDireito_H = 0

        for indx, p in enumerate(pontos):
            # p[0] é na horizontal
            # p[1] é na vertical
            if indx == 8:
                quadrilDireito_H = p[0]
            elif indx == 10:
                tornozeloDireito_H = p[0]
            elif indx == 11:
                quadrilEsquerdo_H = p[0]
            elif indx == 13:
                tornozeloEsquerdo_H = p[0]

        # quanto menor a posição da altura, mais alto o ponto está
        # quanto maior a posição da altura, mais baixo o ponto está
        if (tornozeloDireito_H >= quadrilDireito_H) and (tornozeloEsquerdo_H <= quadrilEsquerdo_H):
            return True
        else:
            return False