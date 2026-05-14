# 🐍 Curso: Lógica de Programação com Python & Git/GitHub

## 📌 Conteúdo Programático Geral
* Fundamentos do pensamento computacional.
* Estruturas lógicas e sintaxe Python.
* Controle de versão local com Git.
* Colaboração e portfólio no GitHub.

---

## 💻 1. Git e GitHub (Controle de Versão)

### Conceitos Básicos
* **Git:** Sistema de controle de versão local.
* **GitHub:** Plataforma na nuvem para hospedar repositórios.
* **Repositório:** Pasta gerenciada pelo Git.

### Comandos Essenciais do Git
* `git init`: Inicializa um repositório local.
* `git add .`: Adiciona arquivos para a área de preparação.
* `git commit -m "mensagem"`: Grava as alterações com uma nota.
* `git status`: Verifica o estado atual dos arquivos.

### Conexão Humana com GitHub
* `git branch -M main`: Renomeia a ramificação principal.
* `git remote add origin URL`: Vincula o repositório local ao remoto.
* `git push -u origin main`: Envia o código para o GitHub.

---

## ⚡ 2. Variáveis, Tipos de Dados e Entrada/Saída

### Tipos de Dados em Python
* `int`: Inteiros (Ex: `idade = 20`).
* `float`: Decimais (Ex: `altura = 1.75`).
* `str`: Textos (Ex: `curso = "Lógica"`).
* `bool`: Booleanos (`True` ou `False`).

### Entrada e Saída
* `print()`: Exibe dados no terminal.
* `input()`: Captura dados digitados textualmente.
* **Casting:** Conversão obrigatória como `int(input())`.

---

## 🔁 3. Operadores Lógicos e Aritméticos

### Operadores Aritméticos
* Cálculos: Adição (`+`), Subtração (`-`), Multiplicação (`*`).
* Divisões: Real (`/`), Inteira (`//`), Resto (`%`).

### Operadores Relacionais e Lógicos
* Comparação: Igual (`==`), Diferente (`!=`), Maior (`>`).
* Conjunção: `and` (E), `or` (OU), `not` (NÃO).

---

## 🚦 4. Estruturas Condicionais

### Fluxo de Decisão
* `if`: Executa se a condição for verdadeira.
* `elif`: Teste alternativo intermediário.
* `else`: Executa se nenhuma condição anterior for atendida.

### Exemplo Prático
```python
idade = int(input("Idade: "))

if idade >= 18:
    print("Acesso liberado.")
else:
    print("Acesso bloqueado.")
```

---

## 🔄 5. Estruturas de Repetição (Loops)

### Laços de Repetição
* `while`: Executa enquanto a condição for verdadeira.
* `for`: Percorre sequências ou intervalos numéricos.
* `range(inicio, fim)`: Gera sequências para o laço `for`.

### Exemplo Prático
```python
# Imprime números de 0 a 4
for numero in range(5):
    print(numero)
```

---

## 🗃️ 6. Listas e Funções

### Listas
* Armazenam múltiplos valores ordenados.
* Métodos comuns: `.append(item)` insere ao final.

### Funções
* Blocos reutilizáveis declarados com `def`.
* Utilizam `return` para enviar dados de volta.