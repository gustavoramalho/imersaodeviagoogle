# 🧮 Calculadora Simples em Python

Projeto desenvolvido como parte prática da **Imersão Engenharia de Software: Dev na Era da IA**, uma iniciativa realizada pela **Alura** em parceria com o **Google**.

---

## 📌 Sobre o Projeto

Este projeto consiste em uma calculadora interativa via linha de comando (CLI) desenvolvida em **Python**. O objetivo principal é consolidar conceitos fundamentais de programação e engenharia de software para quem está iniciando os estudos, explorando boas práticas como modularização de funções, validação de entradas de dados e tratamento de erros.

---

## ⚙️ Funcionalidades

- ➕ **Adição** (`+`)
- ➖ **Subtração** (`-`)
- ✖️ **Multiplicação** (`*`)
- ➗ **Divisão** (`/`)
- 🔢 **Porcentagem** (`%`)
- 🛡️ **Tratamento de divisão por zero**: Evita erros matemáticos informando o usuário com mensagem amigável.
- 🔍 **Validação de entrada**: Proteção contra digitação de valores não numéricos com `try/except`.
- 🔁 **Menu interativo em loop**: Permite realizar múltiplas operações consecutivas até escolher a opção de sair (`0`).

---

## 📋 Pré-requisitos

Para executar este projeto, você precisa apenas de:

- **Python 3.8 ou superior** instalado em sua máquina.
- **Nenhuma biblioteca externa é necessária**: O projeto utiliza exclusivamente recursos nativos da biblioteca padrão do Python.

Para verificar se você já possui o Python instalado, execute no terminal:

```bash
python3 --version
```
*(ou `python --version` dependendo do seu sistema operacional)*

---

## 🚀 Como Executar

1. **Abra o terminal** e navegue até a pasta do projeto:
   ```bash
   cd /caminho/para/o/projeto
   ```

2. **Execute o script da calculadora**:
   ```bash
   python3 calculadora.py
   ```
   *(No Windows, você também pode usar: `python calculadora.py`)*

3. **Interaja com o menu**:
   - Digite o número correspondente à operação desejada (`1` a `5`).
   - Insira os valores quando solicitado.
   - Veja o resultado na tela.
   - Para encerrar, selecione a opção `0`.

---

## 📂 Estrutura do Código

- [`somar(a, b)`](calculadora.py): Realiza a soma de dois valores.
- [`subtrair(a, b)`](calculadora.py): Realiza a subtração entre dois valores.
- [`multiplicar(a, b)`](calculadora.py): Calcula o produto de dois valores.
- [`dividir(a, b)`](calculadora.py): Efetua a divisão, com validação para impedir divisão por zero.
- [`porcentagem(valor, taxa)`](calculadora.py): Calcula o percentual de um valor base (ex: `15% de 200 = 30`).
- [`calculadora()`](calculadora.py): Função principal que orquestra o menu, captura as opções do usuário e exibe as mensagens no terminal.

---

## 🎓 Contexto: Imersão Alura + Google

Este repositório foi construído durante a **Imersão Engenharia de Software: Dev na Era da IA**, promovida pela [Alura](https://www.alura.com.br/) em parceria com o [Google](https://about.google/). A imersão aborda a integração de ferramentas de Inteligência Artificial moderna no fluxo de trabalho de desenvolvimento de software, acelerando o aprendizado e a produtividade no código.
