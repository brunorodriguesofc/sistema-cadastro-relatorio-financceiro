# SISTEMA DE CADASTRO + RELATÓRIO

# listas para armazenar dados
lista_nomes = []
lista_margens = []

# repetir 3 vezes (3 usuários)
for i in range(3):
    print(f"\nCadastro {i+1}")

    nome = input("Digite o nome: ").strip().title()
    email = input("Digite o email: ").strip().lower()
    faturamento = float(input("Digite o faturamento: ").replace("R$", "").replace(",", "."))
    custo = float(input("Digite o custo: ").replace("R$", "").replace(",", "."))

    # pegar primeiro nome
    posicao = nome.find(" ")
    primeiro_nome = nome[:posicao]

    # pegar servidor do email
    posicao_email = email.find("@")
    servidor = email[posicao_email+1:]

    # cálculo financeiro
    lucro = faturamento - custo
    margem = (lucro / faturamento) * 100

    # salvar dados
    lista_nomes.append(primeiro_nome)
    lista_margens.append(margem)

    # saída individual
    print(f"\nUsuário {primeiro_nome} cadastrado")
    print(f"Servidor: {servidor}")
    print(f"Lucro: R${lucro:,.2f}")
    print(f"Margem: {margem:.2f}%")

# --- RELATÓRIO FINAL ---

print("\n--- RELATÓRIO FINAL ---")

# média das margens
media_margem = sum(lista_margens) / len(lista_margens)

print(f"Total de usuários: {len(lista_nomes)}")
print(f"Média das margens: {media_margem:.2f}%")

print("Usuários cadastrados:")
print(lista_nomes)
