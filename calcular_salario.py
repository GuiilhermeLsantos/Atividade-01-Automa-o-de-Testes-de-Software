def calcular_salario(valor_hora_aula, num_aulas, desconto_inss):

    salario_bruto = valor_hora_aula * num_aulas

    desconto = salario_bruto * (desconto_inss / 100 )

    salario_liquido = salario_bruto - desconto

    return salario_liquido


