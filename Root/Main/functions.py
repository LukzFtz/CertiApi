def unidade(number):
    if number == '1':
        return 'um'
    elif number == '2':
        return 'dois'
    elif number == '3':
        return 'três'
    elif number == '4':
        return 'quatro'
    elif number == '5':
        return 'cinco'
    elif number == '6':
        return 'seis'
    elif number == '7':
        return 'sete'
    elif number == '8':
        return 'oito'
    elif number == '9':
        return 'nove'

def dezena(numbers):
    if numbers == '10':
        return 'dez'
    if numbers == '11':
        return 'onze'
    elif numbers == '12':
        return 'doze'
    elif numbers == '13':
        return 'treze'
    elif numbers == '14':
        return 'quatorze'
    elif numbers == '15':
        return 'quinze'
    elif numbers == '16':
        return 'dezesseis'
    elif numbers == '17':
        return 'dezessete'
    elif numbers == '18':
        return 'dezoito'
    elif numbers == '19':
        return 'dezenove'

def dezenaGeral(numbers):
    if numbers[0] == '2':
        dezenaAtual = 'vinte'
        if numbers == '20':
            return dezenaAtual

        aux = numbers[1:]
        auxTxtValor = unidade(aux)
        dezenaAtual += " e "+auxTxtValor
        return dezenaAtual

    elif numbers[0] == '3':
        dezenaAtual = 'trinta'
        if numbers == '30':
            return dezenaAtual

        aux = numbers[1:]
        auxTxtValor = unidade(aux)
        dezenaAtual += " e " + auxTxtValor
        return dezenaAtual

    elif numbers[0] == '4':
        dezenaAtual = 'quarenta'
        if numbers == '40':
            return dezenaAtual

        aux = numbers[1:]
        auxTxtValor = unidade(aux)
        dezenaAtual += " e " + auxTxtValor
        return dezenaAtual

    elif numbers[0] == '5':
        dezenaAtual = 'cinquenta'
        if numbers == '50':
            return dezenaAtual

        aux = numbers[1:]
        auxTxtValor = unidade(aux)
        dezenaAtual += " e " + auxTxtValor
        return dezenaAtual

    elif numbers[0] == '6':
        dezenaAtual = 'sessenta'
        if numbers == '60':
            return dezenaAtual

        aux = numbers[1:]
        auxTxtValor = unidade(aux)
        dezenaAtual += " e " + auxTxtValor
        return dezenaAtual

    elif numbers[0] == '7':
        dezenaAtual = 'setenta'
        if numbers == '70':
            return dezenaAtual

        aux = numbers[1:]
        auxTxtValor = unidade(aux)
        dezenaAtual += " e " + auxTxtValor
        return dezenaAtual

    elif numbers[0] == '8':
        dezenaAtual = 'oitenta'
        if numbers == '80':
            return dezenaAtual

        aux = numbers[1:]
        auxTxtValor = unidade(aux)
        dezenaAtual += " e " + auxTxtValor
        return dezenaAtual

    elif numbers[0] == '9':
        dezenaAtual = 'noventa'
        if numbers == '90':
            return dezenaAtual

        aux = numbers[1:]
        auxTxtValor = unidade(aux)
        dezenaAtual += " e " + auxTxtValor
        return dezenaAtual

def centena(numbers):
    if numbers[0] == '1':
        centenaAtual = 'cem'
        if numbers == '100':
            return centenaAtual

        aux = numbers[1:]
        auxInt = int(aux)
        auxTxtValor = " "
        if auxInt < 10:
            auxTxtValor += unidade(str(auxInt))
        elif auxInt < 20:
            auxTxtValor += dezena(aux)
        else:
            auxTxtValor += dezenaGeral(aux)

        centenaAtual = 'cento'
        centenaAtual += " e " + auxTxtValor
        return centenaAtual

    elif numbers[0] == '2':
        centenaAtual = 'duzentos'
        if numbers == '200':
            return centenaAtual

        aux = numbers[1:]
        auxInt = int(aux)
        auxTxtValor = " "
        if auxInt < 10:
            auxTxtValor += unidade(str(auxInt))
        elif auxInt < 20:
            auxTxtValor += dezena(aux)
        else:
            auxTxtValor += dezenaGeral(aux)

        centenaAtual += " e " + auxTxtValor
        return centenaAtual

    elif numbers[0] == '3':
        centenaAtual = 'trezentos'
        if numbers == '300':
            return centenaAtual

        aux = numbers[1:]
        auxInt = int(aux)
        auxTxtValor = " "
        if auxInt < 10:
            auxTxtValor += unidade(str(auxInt))
        elif auxInt < 20:
            auxTxtValor += dezena(aux)
        else:
            auxTxtValor += dezenaGeral(aux)

        centenaAtual += " e " + auxTxtValor
        return centenaAtual

    elif numbers[0] == '4':
        centenaAtual = 'quatrocentos'
        if numbers == '400':
            return centenaAtual

        aux = numbers[1:]
        auxInt = int(aux)
        auxTxtValor = " "
        if auxInt < 10:
            auxTxtValor += unidade(str(auxInt))
        elif auxInt < 20:
            auxTxtValor += dezena(aux)
        else:
            auxTxtValor += dezenaGeral(aux)

        centenaAtual += " e " + auxTxtValor
        return centenaAtual

    elif numbers[0] == '5':
        centenaAtual = 'quinhetos'
        if numbers == '400':
            return centenaAtual

        aux = numbers[1:]
        auxInt = int(aux)
        auxTxtValor = " "
        if auxInt < 10:
            auxTxtValor += unidade(str(auxInt))
        elif auxInt < 20:
            auxTxtValor += dezena(aux)
        else:
            auxTxtValor += dezenaGeral(aux)

        centenaAtual += " e " + auxTxtValor
        return centenaAtual

    elif numbers[0] == '6':
        centenaAtual = 'seiscentos'
        if numbers == '400':
            return centenaAtual

        aux = numbers[1:]
        auxInt = int(aux)
        auxTxtValor = " "
        if auxInt < 10:
            auxTxtValor += unidade(str(auxInt))
        elif auxInt < 20:
            auxTxtValor += dezena(aux)
        else:
            auxTxtValor += dezenaGeral(aux)

        centenaAtual += " e " + auxTxtValor
        return centenaAtual

    elif numbers[0] == '7':
        centenaAtual = 'setecentos'
        if numbers == '400':
            return centenaAtual

        aux = numbers[1:]
        auxInt = int(aux)
        auxTxtValor = " "
        if auxInt < 10:
            auxTxtValor += unidade(str(auxInt))
        elif auxInt < 20:
            auxTxtValor += dezena(aux)
        else:
            auxTxtValor += dezenaGeral(aux)

        centenaAtual += " e " + auxTxtValor
        return centenaAtual

    elif numbers[0] == '8':
        centenaAtual = 'oitocentos'
        if numbers == '400':
            return centenaAtual

        aux = numbers[1:]
        auxInt = int(aux)
        auxTxtValor = " "
        if auxInt < 10:
            auxTxtValor += unidade(str(auxInt))
        elif auxInt < 20:
            auxTxtValor += dezena(aux)
        else:
            auxTxtValor += dezenaGeral(aux)

        centenaAtual += " e " + auxTxtValor
        return centenaAtual

    elif numbers[0] == '9':
        centenaAtual = 'novecentos'
        if numbers == '400':
            return centenaAtual

        aux = numbers[1:]
        auxInt = int(aux)
        auxTxtValor = " "
        if auxInt < 10:
            auxTxtValor += unidade(str(auxInt))
        elif auxInt < 20:
            auxTxtValor += dezena(aux)
        else:
            auxTxtValor += dezenaGeral(aux)

        centenaAtual += " e " + auxTxtValor
        return centenaAtual

def milhar(numbers):
    aux = numbers[:-3]
    unidadeAtual = 'mil'
    valorExtenso = " "

    if len(aux) < 2:
        valorCentenas = str(int(numbers[1:]))
        valorCentenasLength = len(valorCentenas)
        if aux == '1':
            valorExtenso += unidadeAtual
            if valorCentenas == '0':
                return valorExtenso

            if valorCentenasLength == 1:
                valorExtenso += " e "+unidade(valorCentenas)
            elif valorCentenasLength == 2 and valorCentenas[0] == '1':
                valorExtenso += " e " + dezena(valorCentenas)
            elif valorCentenasLength == 2 and valorCentenas[0] != '1':
                valorExtenso +=" e " + dezenaGeral(valorCentenas)
            else:
                valorExtenso += " " + centena(valorCentenas)
        else:
            valorExtenso += unidade(aux) + ' ' + unidadeAtual
            if valorCentenasLength == 1:
                valorExtenso += " e " + unidade(valorCentenas)
            elif valorCentenasLength == 2 and valorCentenas[0] == '1':
                valorExtenso += " e "+ dezena(valorCentenas)
            elif valorCentenasLength == 2 and valorCentenas[0] != '1':
                valorExtenso += " e " + dezenaGeral(valorCentenas)
            else:
                valorExtenso +=" " + centena(valorCentenas)
    else:
        valorCentenas = str(int(numbers[2:]))
        valorCentenasLength = len(valorCentenas)

        if aux[0] == '1':
            valorExtenso += dezena(aux) + ' ' + unidadeAtual
        else:
            valorExtenso += dezenaGeral(aux) + ' ' + unidadeAtual

        if valorCentenasLength == 1:
            valorExtenso += " e " + unidade(valorCentenas)
        elif valorCentenasLength == 2 and valorCentenas[0] == '1':
            valorExtenso += " e " + dezena(valorCentenas)
        elif valorCentenasLength == 2 and valorCentenas[0] != '1':
            valorExtenso += " e " + dezenaGeral(valorCentenas)
        else:
            valorExtenso +=" " + centena(valorCentenas)

    return valorExtenso


def transformNumToStr(numbers):
    tamanhoNumero = len(numbers)
    numeroExtenso = ""

    moduloNumero = numbers

    if moduloNumero[0] == '-':
        numeroExtenso = "menos "
        moduloNumero=numbers[1:]

    numeroExtenso += milhar(moduloNumero)

    return numeroExtenso
