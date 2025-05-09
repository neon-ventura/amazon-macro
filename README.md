
# 👗 Macro Amazon Fashion - Automação com Python + Selenium

Este script em Python automatiza a navegação pela seção de moda da Amazon Brasil, interagindo com os primeiros 13 produtos listados na página. Ele tenta diferentes formas de localizar e clicar nos itens para garantir maior estabilidade e flexibilidade.

## 🚀 Funcionalidades

- Acessa diretamente a seção de **moda da Amazon Brasil**.
- Encontra os produtos usando múltiplos seletores CSS para maior confiabilidade.
- Clica sequencialmente nos 13 primeiros produtos.
- Retorna à lista principal após cada interação.
- Usa diferentes métodos de clique: direto, JavaScript, ActionChains e PyAutoGUI.

## 🧰 Requisitos

- Python 3.7+
- Google Chrome instalado
- ChromeDriver compatível com sua versão do Chrome

## 📦 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/neon-ventura/amazon-macro.git
   cd amazon-macro
   ```

2. (Opcional) Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # no Windows use: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install selenium pyautogui
   ```

4. Certifique-se de que o `chromedriver` esteja acessível. Você pode:
   - Adicioná-lo ao PATH do sistema (recomendado), ou
   - Deixar o executável na mesma pasta do script

## ▶️ Como Usar

Execute o script com:

```bash
python nome_do_script.py
```

O script abrirá o navegador, navegará pelos produtos da seção de moda da Amazon e interagirá automaticamente com os 13 primeiros.

> ⚠️ **Modo de segurança do PyAutoGUI:** Mova o mouse para o canto superior esquerdo da tela para interromper o script a qualquer momento.

## 🛠️ Sobre o Script

- `abrir_amazon_fashion()`: Acessa a página de moda.
- `encontrar_produtos()`: Busca elementos de produto com múltiplos seletores.
- `clicar_produto()`: Tenta vários métodos de clique para garantir interação.
- `clicar_produto_especifico()`: Coordena a seleção e clique em cada item.
- `main()`: Executa a automação completa.

## 📌 Observações

- O script depende da estrutura atual da página da Amazon — mudanças no layout podem exigir atualização nos seletores.
- Testado na Amazon Brasil em maio de 2025.
