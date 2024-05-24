def calcular_conta_energia(consumo_kwh, tarifa_tusd, tarifa_te, iluminacao_publica, icms_cde):
    # Calcula o valor da TUSD
    tusd = consumo_kwh * tarifa_tusd
    
    # Calcula o valor da TE
    te = consumo_kwh * tarifa_te
    
    # Soma os valores da iluminação pública municipal e ICMS - CDE
    iluminacao_icms_cde = iluminacao_publica + icms_cde
    
    # Calcula o valor total da conta de energia
    valor_total_conta = tusd + te + iluminacao_icms_cde
    return valor_total_conta

# Dados fornecidos pela Neoenergia
consumo_kwh_diario = 302 / 28  # Consumo diário em kWh
quantidade_dias = 28  # Quantidade de dias de consumo
tarifa_tusd = 0.56501497  # Tarifa de TUSD em R$/kWh
tarifa_te = 0.45039947  # Tarifa de TE em R$/kWh
iluminacao_publica = 31.68  # Valor da iluminação pública municipal em R$
icms_cde = 1.31  # Valor do ICMS - CDE em R$

# Calcula o consumo total de energia para o período de 28 dias
consumo_total_kwh = consumo_kwh_diario * quantidade_dias

# Exibe apresentação
print("\n\t##### Conta de energia #####\n")
# Calcula o valor total da conta de energia
valor_total_conta = calcular_conta_energia(consumo_total_kwh, tarifa_tusd, tarifa_te, iluminacao_publica, icms_cde)
print(f"O valor total da conta de energia é R$ {valor_total_conta:.2f}")
