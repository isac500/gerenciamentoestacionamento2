# gerenciamentoestacionamento2.0
# 🅿️ Sistema de Gerenciamento de Estacionamento 2.0

Este é um sistema de gerenciamento de estacionamento desenvolvido em **Python**, com foco na organização, facilidade de uso e praticidade para pequenos negócios e estacionamentos. A versão 2.0 traz melhorias significativas em relação à versão anterior, com validações de entrada, visualização mais clara dos dados, controle financeiro automatizado e recursos personalizáveis.

## 📽️ Demonstração em vídeo

Confira a apresentação completa do sistema no YouTube:

👉 [Clique aqui para assistir ao vídeo](https://youtu.be/tjKWyEI4Tn0?si=N9cX5sHcJl_lmY8I)

## 🚀 Funcionalidades

- **Entrada de veículos**  
  - Validação de placas no padrão nacional (Mercosul)
  - Registro de **data e hora** da entrada
  - Registro do **modelo do veículo**

- **Saída de veículos**
  - Cálculo automático do valor a pagar
  - Respeita **tempo de tolerância** definido
  - Armazena dados completos em um arquivo `.txt` (modelo, placa, entrada, saída, valor, etc.)

- **Visualização do pátio**
  - Lista veículos presentes no estacionamento com:
    - Placa
    - Modelo
    - Data e hora de entrada

- **Histórico de saídas**
  - Exibe todos os registros de veículos que já saíram do pátio

- **Configurações**
  - Permite definir:
    - Valor por hora
    - Tempo de tolerância em minutos
  - Cada entrada considera os valores vigentes no momento da entrada

## 🧠 Tecnologias utilizadas

- Python 3.x
- Programação modular
- Manipulação de arquivos `.txt` como banco de dados simples

## 🛠️ Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Isac500/gerenciamentoestacionamento2.0.git
