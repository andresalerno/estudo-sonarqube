"""Exemplo de CODE SMELL: método longo, complexo e com más práticas."""


def processar_relatorio(vendas, tipo, regiao, desconto, bonus, meta):
    # TODO: refatorar esse método, ele cresceu demais (dívida técnica)
    resultado = 0
    total_bruto = 0
    contador_erros = 0  # CODE SMELL: variável declarada e nunca usada

    if tipo == 1:
        if regiao == "norte":
            if desconto > 0:
                if desconto < 50:
                    resultado = vendas - (vendas * desconto / 100)
                else:
                    resultado = vendas * 0.5
            else:
                resultado = vendas
        elif regiao == "sul":
            if desconto > 0:
                if desconto < 30:
                    resultado = vendas - (vendas * desconto / 100)
                else:
                    resultado = vendas * 0.7
            else:
                resultado = vendas
        else:
            resultado = vendas
    elif tipo == 2:
        if bonus > 100:
            resultado = vendas + bonus - 15
        else:
            resultado = vendas + bonus

    total_bruto = resultado * 1.2

    if resultado > meta:
        status = "Meta atingida"
    else:
        status = "Meta nao atingida"

    return {
        "resultado": resultado,
        "total_bruto": total_bruto,
        "status": status,
    }
