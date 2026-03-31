# Sistema de Cadastro + Relatório Financeiro

Projeto em Python que simula o cadastro de um usuário e a geração de um relatório financeiro simples.

---

## 🔹 Funcionalidades

### Cadastro e Tratamento de Dados
- Remoção de espaços com .strip()
- Padronização:
  - Nome com .title()
  - Email com .lower()
- Extração de informações:
  - Primeiro nome
  - Servidor do email

---

### Análise Financeira
- Cálculo do lucro:

lucro = faturamento - custo

- Cálculo da margem:

margem = (lucro / faturamento) * 100

---

### Saída Formatada
- Exibição com padrão monetário (R$)
- Duas casas decimais
- Percentual de margem

---

## 🔹 Exemplo de saída

Usuário Joao foi cadastrado com sucesso
Servidor de email: gmail.com
Lucro: R$1,400.00
Margem: 40.00%
