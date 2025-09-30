# --- Constantes ---
# 1 km² em m² (1 milhão de metros quadrados).
# O underscore (_) é usado para melhorar a legibilidade de números grandes no código.
KM2_PARA_M2 = 1_000_000

# Área de um campo de futebol padrão FIFA (105m x 68m).
AREA_CAMPO_FIFA_M2 = 105 * 68  # 7140 m²

# Área devastada que o usuário forneceu ( exemplo: 10 km²).
AREA_DEVASTADA_KM2 = float(input("Digite a área devastada em km²: "))

# --- Cálculo ---
# 1. Converte a área devastada de km² para m²
area_devastada_m2 = AREA_DEVASTADA_KM2 * KM2_PARA_M2

# 2. Calcula quantos campos de futebol cabem na área
campos_que_cabem = area_devastada_m2 / AREA_CAMPO_FIFA_M2

# --- Saída ---
# Usamos f-string com a formatação :,.2f para:
# - :, => Adicionar separador de milhares (vírgula no ambiente Python padrão)
# - .2f => Limitar a duas casas decimais
print(f"Área em km²: {AREA_DEVASTADA_KM2:,} km²")
print(f"Área em m²: {area_devastada_m2:,} m²")
print(f"Área de 1 campo FIFA: {AREA_CAMPO_FIFA_M2:,} m²")
print("-" * 30)
print(f"Total de campos de futebol que cabem na área: {campos_que_cabem:,.2f}")