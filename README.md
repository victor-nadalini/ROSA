# Rosa - Assistente Virtual em Python

## Descrição
Rosa é uma assistente virtual desenvolvida em Python que utiliza reconhecimento de voz e síntese de fala para interagir com o usuário. Ela é capaz de realizar diversas tarefas cotidianas através de comandos de voz em português.

## Tecnologias Utilizadas
- **Linguagem**: Python 3.x
- **Bibliotecas Principais**:
  - `speech_recognition`: Para reconhecimento de voz
  - `gTTS` (Google Text-to-Speech): Para síntese de fala
  - `playsound`: Para reprodução de áudio
  - `requests`: Para requisições HTTP
  - `beautifulsoup4`: Para web scraping
  - `datetime`: Para manipulação de data e hora

## Funcionalidades Implementadas

### 1. Comandos Básicos
- **Reconhecimento de Voz**: Captura comandos de voz do usuário
- **Síntese de Fala**: Responde através de áudio
- **Encerramento**: Pode ser desligada por comando de voz

### 2. Informações do Sistema
- **Horário**: Informa a hora atual
- **Controle do Computador**: 
  - Desligamento programado (15 minutos)
  - Cancelamento de desligamento

### 3. Pesquisas e Navegação
- **Google**: Realiza pesquisas no Google
- **YouTube**: Pesquisa vídeos no YouTube
- **Spotify**: Abre playlists e músicas específicas

### 4. Informações em Tempo Real
- **Clima**: Fornece informações meteorológicas de São Paulo
- **Cotações**: Consulta valores de moedas (USD, EUR, BTC)
- **Notícias**: Lê as principais notícias do Google News
- **Filmes**: Informa sobre próximos lançamentos de filmes

## APIs Utilizadas
- OpenWeather API (clima)
- TMDB API (filmes)
- Awesome API (cotações)
- Google Speech Recognition API

## Requisitos
- Python 3.x
- Microfone funcional
- Conexão com internet
- Chaves de API para serviços externos

## Como Usar
1. Instale as dependências:
```bash
pip install -r requirements.txt
```
2. Configure suas chaves de API nos arquivos:
   - `token_tmdb.py`
   - `token_openwheather.py`
3. Execute o programa:
```bash
python ROSA.PY
```
4. Interaja com a Rosa através de comandos de voz

## Comandos de Voz Disponíveis
- "Que horas são?"
- "Pesquisar no Google [termo]"
- "Pesquisar no YouTube [termo]"
- "Clima"
- "Moeda americana/Euro/Bitcoin"
- "News"
- "Filmes em lançamento"
- "Playlist [tipo]"
- "Desligar computador em 15 minutos"
- "Cancelar desligamento"
- "Desligue rosa"

## Status do Projeto
Em desenvolvimento ativo, com novas funcionalidades sendo implementadas regularmente.
