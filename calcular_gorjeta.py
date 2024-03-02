def calcular_gorjeta(valor_despesas):
    
    valor_gorjeta = valor_despesas * 0.1
    
    valor_total_conta = valor_despesas + valor_gorjeta

    return (valor_total_conta, valor_gorjeta)

