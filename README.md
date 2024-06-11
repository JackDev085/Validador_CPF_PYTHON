# Gerador e Validador de CPF

Este script em Python permite aos usuários gerar um número de CPF (Cadastro de Pessoas Físicas) válido ou validar um número de CPF existente. O CPF é um número de identificação utilizado no Brasil para pessoas físicas.

## Funcionalidades

1. **Gerar CPF**: Cria um número de CPF válido de forma aleatória.
2. **Validar CPF**: Verifica se um número de CPF existente é válido.

## Requisitos

- Python 3.x

## Como Usar

### Executando o Script

Para executar o script, basta rodá-lo em um ambiente Python. O script solicitará que você escolha uma opção do menu:

1. **Gerar CPF**: Selecione esta opção para gerar um novo número de CPF.
2. **Validar CPF**: Selecione esta opção para verificar a validade de um CPF existente.
3. **Sair**: Selecione esta opção para encerrar o programa.

### Menu de Opções

- **1 - Gerar CPF**: Esta opção gera um número de CPF válido e o exibe formatado.
- **2 - Validar CPF**: Esta opção valida um CPF digitado pelo usuário.
- **3 - Sair**: Esta opção encerra a execução do script.

### Gerar CPF

Ao selecionar a opção para gerar um CPF, o script realiza os seguintes passos:

1. Gera nove dígitos aleatórios.
2. Calcula o primeiro dígito verificador.
3. Calcula o segundo dígito verificador.
4. Exibe o CPF completo e formatado.

### Validar CPF

Ao selecionar a opção para validar um CPF, o script realiza os seguintes passos:

1. Solicita ao usuário que insira um CPF (sem pontos ou traços).
2. Calcula o primeiro dígito verificador do CPF inserido.
3. Calcula o segundo dígito verificador do CPF inserido.
4. Verifica se os dígitos verificadores calculados coincidem com os dígitos do CPF inserido.
5. Informa ao usuário se o CPF é válido ou inválido.
