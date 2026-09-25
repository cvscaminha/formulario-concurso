print("=" * 40)
print("FORMULÁRIO DE INSCRIÇÃO - CONCURSO")
print("=" * 40)

# Entrada de Dados
nome = input("Digite seu nome completo: ")
cpf = input("Digite seu CPF: ")
idade = int(input("Digite sua idade: "))

print("\nEscolha sua escolaridade:")
print("1 - Ensino Médio")
print("2 - Ensino Superior")
print("3 - Pós-graduação")
escolaridade = int(input("Opção: "))

sexo = input("Digite seu sexo (M/F): ").upper()

# Verificação da idade
if idade < 18:
    print("\nInscrição não permitida!")
    print("O candidato deve possuir 18 anos ou mais.")
else:
    print("\nIdade aprovada!")

# Verificação da escolaridade
if escolaridade == 1:
    nivel = "Ensino Médio"
elif escolaridade == 2:
    nivel = "Ensino Superior"
elif escolaridade == 3:
    nivel = "Pós-graduação"
else:
    nivel = "Escolaridade inválida"

# Verificação do sexo
if sexo == "M":
    documento = "Certificado de Reservista"
elif sexo == "F":
    documento = "Não necessita de documento militar"
else:
    documento = "Sexo informado inválido"

# Área Profissional
print("\nEscolha a área desejada:")
print("1 - Administração")
print("2 - Tecnologia da Informação")
print("3 - Educação")
area = int(input("Área: "))

if area == 1:
    cargo = "Analista Administrativo"
elif area == 2:
    cargo = "Analista de Sistemas"
elif area == 3:
    cargo = "Professor"
else:
    cargo = "Área Inválidade"

# Resumo
print("\n"+ "=" * 40)
print("INSCRIÇÃO DO CANDIDATO")
print("=" * 40)

print(f"Candidato: {nome}")
print(f"CPF: {cpf}")
print(f"Idade: {idade} anos")
print(f"Escolaridade: {nivel}")
print(f"Cargo escolhido: {cargo}")
print(f"Documento: {documento}")

if idade >= 18 and escolaridade>0 and sexo in ["M", "F"]:
    print("\nSITUAÇÃO: INSCRIÇÃO APROVADA!")
else:
    print("\nSITUAÇÃO: INSCRIÇÃO COM PENDÊNCIAS!")