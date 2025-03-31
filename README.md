# Rosa - Assistente Virtual

Rosa é uma assistente virtual desenvolvida em Python que utiliza reconhecimento de voz e síntese de fala para interagir com o usuário.

## Funcionalidades

### Comandos Básicos

- "Desligue Rosa" ou "Desligar Rosa" - Encerra o programa
- "Que horas são" - Informa o horário atual
- "Desligar computador em 15 minutos" - Agenda o desligamento do computador
- "Cancelar desligamento" - Cancela o desligamento programado

### Pesquisas

- "Pesquisar [termo] no Google" - Realiza pesquisa no Google
- "Pesquisar [termo] no YouTube" - Realiza pesquisa no YouTube

### Música e Entretenimento

- "Melhor track" - Abre uma música específica no Spotify
- "Melhor playlist" - Abre uma playlist específica no Spotify
- "Playlist rock" - Abre playlist de rock
- "Playlist eletro" - Abre playlist de música eletrônica
- "Playlist flume" - Abre playlist do Flume
- "Playlist dar" - Abre playlist específica
- "Playlist blade" - Abre playlist específica

### Informações

- "News" - Lê as últimas notícias
- "Moeda americana" - Mostra cotação do dólar
- "Euro" - Mostra cotação do euro
- "Bitcoin" - Mostra cotação do Bitcoin
- "Filmes em lançamento" - Mostra próximos lançamentos de filmes
- "Clima" - Informa o clima em São Paulo

### Ferramentas

- "Traduza [texto]" - Traduz o texto para português
- "Calcule [expressão]" ou "Quanto é [expressão]" - Realiza cálculos matemáticos
- "Sudário" - Inicia a gravação de um relatório

### Abertura de Programas

- Visual Studio Code
- Chrome
- Bloco de Notas
- Calculadora
- Docker
- Spotify
- Discord
- Figma
- Notion
- Streamlabs
- Hydra
- Epic Games
- Oracle VirtualBox
- Opera GX
- Gerenciador de Tarefas

### Jogos

- Cat Quest
- LEGO Marvel Super Heroes 2
- Valorant
- Call of Duty
- Fortnite

## Requisitos

- Python 3.x
- Bibliotecas necessárias (instaladas via pip):
  - speech_recognition
  - gTTS
  - playsound
  - beautifulsoup4
  - requests
  - googletrans
  - tkinter

## Configuração

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Configure as chaves de API necessárias:

- Crie um arquivo `token_tmdb.py` com sua chave da API do TMDB
- Crie um arquivo `token_openwheather.py` com sua chave da API do OpenWeather

## Uso

Execute o arquivo principal:

```bash
python ROSA.PY
```

## Observações

- Certifique-se de ter um microfone funcionando
- Alguns comandos podem requerer conexão com a internet
- Os caminhos dos programas podem precisar ser ajustados de acordo com sua instalação
