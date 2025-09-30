print("menu robô")

print("1 - cadastrar")
print("2 - listar")
print("3 - atualizar")
print("4 - excluir")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    print("Cadastrar")
elif opcao == 2:
    print("Listar")
elif opcao == 3:
    print("Atualizar")
elif opcao == 4:
    print("Excluir")
else:
    print("Opção inválida")

# Regras de Nomeclatura PEP-8
# snake_case: variaveis e funções
# PascalCase: classes   
# SCREAMING_SNAKE_CASE: constantes