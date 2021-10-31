class SexEx5:
    pontos = []

    # Validando posição inicial - superior
    def verificar_bracos_ESTICADOS(pontos):
        # declarando variáveis dos pontos
        punhoDireito_V = 0
        punhoEsquerdo_V = 0
        cotoveloDireito_V = 0
        cotoveloEsquerdo_V = 0
        ombroDireito_V = 0
        ombroEsquerdo_V = 0
        quadrilDireito_V = 0
        quadrilEsquerdo_V = 0
        peito_V = 0

        for indx, p in enumerate(pontos):
            # p[0] é na horizontal
            # p[1] é na vertical
            if indx == 2:
                ombroDireito_V = p[1]
            elif indx == 3:
                cotoveloDireito_V = p[1]
            elif indx == 4:
                punhoDireito_V = p[1]
            elif indx == 5:
                ombroEsquerdo_V = p[1]
            elif indx == 6:
                cotoveloEsquerdo_V = p[1]
            elif indx == 7:
                punhoEsquerdo_V = p[1]
            elif indx == 8:
                quadrilDireito_V = p[1]
            elif indx == 11:
                quadrilEsquerdo_V = p[1]
            elif indx == 14:
                peito_V = p[1]

        if (punhoDireito_V > cotoveloDireito_V) and (punhoEsquerdo_V > cotoveloEsquerdo_V):
            if (cotoveloDireito_V > ombroDireito_V) and (cotoveloEsquerdo_V > ombroEsquerdo_V):
                if (punhoDireito_V > peito_V) and (punhoDireito_V > peito_V):
                    if (cotoveloDireito_V < quadrilDireito_V) and (cotoveloEsquerdo_V < quadrilEsquerdo_V):
                        return True
        else:
            return False

    # Validando posição final - superior
    def verificar_bracos_DESCENDO(pontos):
        # declarando variáveis dos pontos
        cotoveloDireito_V = 0
        punhoDireito_V = 0
        cotoveloEsquerdo_V = 0
        punhoEsquerdo_V = 0
        quadrilDireito_V = 0
        joelhoDireito_V = 0
        quadrilEsquerdo_V = 0
        joelhoEsquerdo_V = 0

        for indx, p in enumerate(pontos):
            # p[0] é na horizontal
            # p[1] é na vertical
            if indx == 3:
                cotoveloDireito_V = p[1]
            elif indx == 4:
                punhoDireito_V = p[1]
            elif indx == 6:
                cotoveloEsquerdo_V = p[1]
            elif indx == 7:
                punhoEsquerdo_V = p[1]
            elif indx == 8:
                quadrilDireito_V = p[1]
            elif indx == 9:
                joelhoDireito_V = p[1]
            elif indx == 11:
                quadrilEsquerdo_V = p[1]
            elif indx == 12:
                joelhoEsquerdo_V = p[1]

        if (cotoveloDireito_V > quadrilDireito_V) and (cotoveloEsquerdo_V > quadrilEsquerdo_V):
            if (punhoDireito_V > joelhoDireito_V) and (punhoEsquerdo_V > joelhoEsquerdo_V):
                return True
        else:
            return False

    # Validando posição final - superior
    def verificar_movimento_ERRADO(pontos):
        # declarando variáveis dos pontos
        punhoDireiro_H = 0
        punhoEsquerdo_H = 0
        quadrilDireito_H = 0
        tornozeloDireito_H = 0
        quadrilEsquerdo_H = 0
        tornozeloEsquerdo_H = 0

        for indx, p in enumerate(pontos):
            # p[0] é na horizontal
            # p[1] é na vertical
            if indx == 4:
                punhoDireiro_H = p[0]
            elif indx == 7:
                punhoEsquerdo_H = p[0]
            elif indx == 8:
                quadrilDireito_H = p[0]
            elif indx == 10:
                tornozeloDireito_H = p[0]
            elif indx == 11:
                quadrilEsquerdo_H = p[0]
            elif indx == 13:
                tornozeloEsquerdo_H = p[0]

        if (punhoDireiro_H >  quadrilEsquerdo_H) and (punhoEsquerdo_H < quadrilDireito_H):
            return True
        elif (quadrilDireito_H > tornozeloEsquerdo_H) and (quadrilEsquerdo_H < tornozeloDireito_H):
            return True
        else:
            return False

    # Validando posição inicial - inferior
    def verificar_pernas_ESTICADAS(pontos):
        # declarando variáveis dos pontos
        cotoveloDireito_V = 0
        cotoveloEsquerdo_V = 0
        tornozeloEsquerdo_H = 0
        tornozeloDireito_H = 0
        quadrilEsquerdo_H = 0
        quadrilEsquerdo_V = 0
        quadrilDireito_H = 0
        quadrilDireito_V = 0
        joelhoDireito_V = 0
        joelhoEsquerdo_V =0

        for indx, p in enumerate(pontos):
            # p[0] é na horizontal
            # p[1] é na vertical
            if indx == 3:
                cotoveloDireito_V = p[1]
            elif indx == 6:
                cotoveloEsquerdo_V = p[1]
            elif indx == 8:
                quadrilDireito_H = p[0]
                quadrilDireito_V = p[1]
            elif indx == 9:
                joelhoDireito_V = p[1]
            elif indx == 10:
                tornozeloDireito_H = p[0]
            elif indx == 11:
                quadrilEsquerdo_H = p[0]
                quadrilEsquerdo_V = p[1]
            elif indx == 12:
                joelhoEsquerdo_V = p[1]
            elif indx == 13:
                tornozeloEsquerdo_H = p[0]

        # quanto menor a posição da altura, mais alto o ponto está
        # quanto maior a posição da altura, mais baixo o ponto está
        if (tornozeloDireito_H >= quadrilDireito_H) and (tornozeloEsquerdo_H <= quadrilEsquerdo_H):
            if (joelhoDireito_V > quadrilDireito_V) and (joelhoEsquerdo_V > quadrilEsquerdo_V):
                if (cotoveloDireito_V < quadrilDireito_V) and (cotoveloEsquerdo_V < quadrilEsquerdo_V):
                    return True
        else:
            return False

    # Validando posição final - superior
    def verificar_pernas_DESCENDO(pontos):
        # declarando variáveis dos pontos
        cotoveloDireito_V = 0
        punhoDireito_V = 0
        cotoveloEsquerdo_V = 0
        punhoEsquerdo_V = 0
        joelhoDireito_V = 0
        tornozeloDireito_V = 0
        joelhoEsquerdo_V = 0
        tornozeloEsquerdo_V = 0

        for indx, p in enumerate(pontos):
            # p[0] é na horizontal
            # p[1] é na vertical
            if indx == 3:
                cotoveloDireito_V = p[1]
            elif indx == 4:
                punhoDireito_V = p[1]
            elif indx == 6:
                cotoveloEsquerdo_V = p[1]
            elif indx == 7:
                punhoEsquerdo_V = p[1]
            elif indx == 9:
                joelhoDireito_V = p[1]
            elif indx == 10:
                tornozeloDireito_V = p[1]
            elif indx == 12:
                joelhoEsquerdo_V = p[1]
            elif indx == 13:
                tornozeloEsquerdo_V = p[1]
        if (cotoveloDireito_V >= joelhoDireito_V) and (cotoveloEsquerdo_V >= joelhoEsquerdo_V):
            if (punhoDireito_V >= tornozeloDireito_V) and (punhoEsquerdo_V >= tornozeloEsquerdo_V):
                return True
        else:
            return False