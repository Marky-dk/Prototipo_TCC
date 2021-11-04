class SegEx9:
    pontos = []

    # Validando posição final 1 - superior
    def verificar_cabeca_ESQUERDA(pontos):
        # declarando variáveis dos pontos
        cabeca_V = 0
        cabeca_H = 0
        punhoEsquerdo_H = 0
        cotoveloEsquerdo_H = 0
        cotoveloEsquerdo_V = 0
        ombroEsquerdo_H = 0

        for indx, p in enumerate(pontos):
            # p[0] é na horizontal
            # p[1] é na vertical
            if indx == 0:
                cabeca_V = p[1]
                cabeca_H = p[0]
            elif indx == 5:
                ombroEsquerdo_H = p[0]
            elif indx == 6:
                cotoveloEsquerdo_V = p[1]
                cotoveloEsquerdo_H = p[0]
            elif indx == 7:
                punhoEsquerdo_H = p[0]

        # quanto menor a posição da altura, mais alto o ponto está
        # quanto maior a posição da altura, mais baixo o ponto está
        if cabeca_H >= ombroEsquerdo_H:
            if punhoEsquerdo_H > cabeca_H:
                if punhoEsquerdo_H < cotoveloEsquerdo_H:
                    if cabeca_V <= cotoveloEsquerdo_V:
                            return True
        else:
            return False

    # Validando posição final 2 - superior
    def verificar_cabeca_DIREITA(pontos):
        # declarando variáveis dos pontos
        cabeca_V = 0
        cabeca_H = 0
        punhoDireito_H = 0
        cotoveloDireito_H = 0
        cotoveloDireito_V = 0
        ombroDireito_H = 0

        for indx, p in enumerate(pontos):
            # p[0] é na horizontal
            # p[1] é na vertical
            if indx == 0:
                cabeca_V = p[1]
                cabeca_H = p[0]
            elif indx == 2:
                ombroDireito_H = p[0]
            elif indx == 3:
                cotoveloDireito_V = p[1]
                cotoveloDireito_H = p[0]
            elif indx == 4:
                punhoDireito_H = p[0]

        # quanto menor a posição da altura, mais alto o ponto está
        # quanto maior a posição da altura, mais baixo o ponto está
        if cabeca_H <= ombroDireito_H:
            if punhoDireito_H < cabeca_H:
                if punhoDireito_H > cotoveloDireito_H:
                    if cabeca_V <= cotoveloDireito_V:
                        if cabeca_H <= ombroDireito_H:
                            return True
        else:
            return False

    # Validando posição inicial - superior
    def verificar_cabeca_CENTRO(pontos):
        # declarando variáveis dos pontos
        cabeca_H = 0
        ombroEsquerdo_H = 0
        ombroDireito_H = 0
        punhoDireito_V = 0
        cotoveloDireito_V = 0
        punhoEsquerdo_V = 0
        cotoveloEsquerdo_V = 0
        ombroDireito_V = 0
        ombroEsquerdo_V = 0

        for indx, p in enumerate(pontos):
            # p[0] é na horizontal
            # p[1] é na vertical
            if indx == 0:
                cabeca_H = p[0]
            elif indx == 2:
                ombroDireito_H = p[0]
                ombroDireito_V = p[1]
            elif indx == 3:
                cotoveloDireito_V = p[1]
            elif indx == 4:
                punhoDireito_V = p[1]
            elif indx == 5:
                ombroEsquerdo_H = p[0]
                ombroEsquerdo_V = p[1]
            elif indx == 6:
                cotoveloEsquerdo_V = p[1]
            elif indx == 7:
                punhoEsquerdo_V = p[1]

        if cabeca_H < ombroEsquerdo_H and cabeca_H > ombroDireito_H:
            if punhoDireito_V > cotoveloDireito_V and punhoEsquerdo_V > cotoveloEsquerdo_V:
                if cotoveloDireito_V > ombroDireito_V and cotoveloEsquerdo_V > ombroEsquerdo_V:
                    return True
        else:
            return False

    # Validando posição errada - superior
    def verificar_movimento_ERRADO(pontos):
        # declarando variáveis dos pontos
        cabeca_H = 0
        cabeca_V = 0
        cotoveloDireito_V = 0
        punhoDireito_H = 0
        cotoveloEsquerdo_V = 0
        punhoEsquerdo_H = 0

        for indx, p in enumerate(pontos):
            # p[0] é na horizontal
            # p[1] é na vertical
            if indx == 0:
                cabeca_H = p[0]
                cabeca_V = p[1]
            elif indx == 3:
                cotoveloDireito_V = p[1]
            elif indx == 4:
                punhoDireito_H = p[0]
            elif indx == 6:
                cotoveloEsquerdo_V = p[1]
            elif indx == 7:
                punhoEsquerdo_H = p[0]

        if cabeca_V > cotoveloEsquerdo_V or cabeca_V > cotoveloDireito_V:
            return True
        elif cabeca_H > punhoEsquerdo_H or cabeca_H < punhoDireito_H:
            return True
        else:
            return False

    # Validando posição final - inferior
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