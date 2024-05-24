# Telegram Bot com Google Sheets

Este projeto envolve a criação de um bot do Telegram que interage com planilhas do Google Sheets para gerenciar cotações motivacionais, palavras banidas e dados de membros. O bot é construído usando a biblioteca `python-telegram-bot` e a `Google Sheets API`, permitindo que funcionalidades ricas e automatizadas sejam implementadas facilmente.

## Funcionalidades

- **Receber e processar comandos**: Responde a comandos específicos iniciados pelos usuários.
- **Gerenciamento de contatos**: Capta e processa informações de contato enviadas pelos usuários.
- **Responder a mensagens de texto**: Filtra e responde a mensagens com base em palavras-chave ou conteúdo.
- **Gerenciar novos membros**: Automatiza ações quando novos membros entram no chat.
- **Integração com Google Sheets**: Armazena e recupera informações de várias planilhas para diferentes propósitos.

## Tecnologias Utilizadas

- Python
- python-telegram-bot
- Google Sheets API
- Google Cloud Platform (Service Accounts)

## Como Usar

### Configuração Inicial

1. **Configuração do Ambiente**:
   - Certifique-se de que o Python está instalado em sua máquina.
   - Instale as dependências necessárias através do comando:
     ```bash
     pip install python-telegram-bot google-auth google-api-python-client
     ```

2. **Configuração do Bot do Telegram**:
   - Crie um bot no Telegram utilizando o `BotFather` e anote o token fornecido.

3. **Configuração do Google Sheets API**:
   - Acesse o [Google Developers Console](https://console.developers.google.com/).
   - Crie um projeto e habilite a API do Google Sheets.
   - Crie uma conta de serviço e baixe o arquivo de chave JSON.
   - Compartilhe as planilhas do Google com o e-mail da conta de serviço.

4. **Atualize as Variáveis de Configuração**:
   - Adicione o caminho para o arquivo de chave da conta de serviço na variável `SERVICE_ACCOUNT_FILE`.
   - Adicione os IDs das planilhas na seção de IDs das planilhas.

### Executando o Bot

1. **Inicie o Script**:
   - Execute o script Python com o comando:
     ```bash
     python nome_do_arquivo.py
     ```

2. **Interagindo com o Bot**:
   - No Telegram, inicie uma conversa com seu bot usando o comando `/start`.
   - Experimente enviar diferentes comandos e mensagens para ver as respostas do bot e a interação com as planilhas do Google Sheets.

## Contribuições

Contribuições são bem-vindas para melhorar o bot e expandir suas funcionalidades. Sinta-se à vontade para clonar o repositório, propor mudanças ou reportar problemas.
