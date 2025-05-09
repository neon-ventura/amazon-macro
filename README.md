
# 📦 Script Automatizado de Acesso aos Mais Vendidos da Amazon

Este script em Python utiliza Selenium e PyAutoGUI para automatizar a navegação na página de **Mais Vendidos da Amazon Brasil**. Ele abre os produtos mais populares da lista, interage com eles e retorna à página inicial automaticamente.

## 🚀 Funcionalidade

- Acessa a página de best-sellers da Amazon Brasil.
- Clica sequencialmente nos 3 primeiros produtos da lista.
- Retorna à página inicial de mais vendidos após cada clique.
- Mantém o navegador aberto até que o usuário pressione Enter para fechar.


## 🎥 Demonstração em Vídeo

👉 [Assista à demonstração aqui](https://www.loom.com/share/b901182eba424cbf8323b32e974d1145?sid=f7930d86-0ba5-41a5-83ff-2c7888a91064)


## 🧰 Requisitos

- Python 3.7+
- Google Chrome instalado
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatível com sua versão do Chrome

## 📦 Instalação

1. **Clone o repositório ou copie o script:**

   ```bash
   git clone https://github.com/neon-ventura/amazon-macro.git
   cd seu-repo
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # no Windows use: venv\Scripts\activate
   ```

3. **Instale as dependências necessárias:**

   ```bash
   pip install selenium pyautogui
   ```

4. **Coloque o `chromedriver` no mesmo diretório do script ou adicione-o ao PATH do sistema.**
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatível com sua versão do Chrome

## ▶️ Como Usar

Execute o script diretamente:

```bash
python amazon_macro.py
```

O script abrirá o navegador, visitará a página dos mais vendidos da Amazon Brasil e interagirá automaticamente com os 3 primeiros produtos.

> ⚠️ **Nota:** O PyAutoGUI está configurado com um "modo de segurança". Mova o mouse para o canto superior esquerdo da tela para interromper o script a qualquer momento.

## 🛠️ Sobre o Script

- `abrir_amazon_bestsellers()`: Inicia o Chrome e acessa os best-sellers.
- `clicar_produto_especifico()`: Interage com um produto específico da lista.
- `main()`: Coordena toda a sequência de ações.

## 📌 Observações

- Certifique-se de que sua conexão com a internet está ativa.
- A Amazon pode alterar a estrutura da página, exigindo ajustes no seletor CSS.
