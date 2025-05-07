from vosk import Model, KaldiRecognizer
import pyaudio
import os
import sys
import webbrowser
import json
import requests
import datetime
from bs4 import BeautifulSoup
import pyttsx3
from playsound import playsound
from token_tmdb import API_KEY_TMDB
from token_openwheather import API_KEY_CLIMA
from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES, Translator
import subprocess

# função cria audio da IA
def rosa_audio(audio):
    voz = pyttsx3.init()
    voz.say(audio)
    voz.runAndWait()
# fim da função 

# função responsavel por ouvir o usuario
def rosa_ouvir():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "model_vosk", "vosk-model-small-pt-0.3")
    model = Model(model_path)
    rec = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio().open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
    
    print("rosa ouvindo....")
    
    while True:
        data = mic.read(4092, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            text = json.loads(rec.Result())["text"]
            print("voce disse: ", text)
            rosa_audio(text)
            executa_comando(text)
            
# fim da função

# noticias 

def noticias():
    rosa_audio( "Buscando notícias")
    site = requests.get('https://news.google.com/news/rss?ned=pt_br&gl=BR&hl=pt')
    noticias = BeautifulSoup(site.text, 'lxml-xml')
    
    noticias_lista = []
    
    for item in noticias.findAll('item')[:5]:
        text = item.title.text
        noticias_lista.append(text)
    rosa_audio(text)
    
# fim da função

# cotação 
def cotacao(moeda): 
    rosa_audio( f"Buscando cotação da moeda {moeda}")
    requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/last/' + moeda + '-BRL')
    cotacao = requisicao.json()
    
    moeda_brl = moeda + "BRL"
    
    if moeda_brl in cotacao:
        nome = cotacao[moeda_brl]["name"] # cotacao["EURBRL"]["Euro/Real Brasileiro"]
        data = cotacao[moeda_brl]["create_date"]
        valor = cotacao[moeda_brl]["bid"]
    
        rosa_audio("cotação do " + nome + "em" + data + "é" + valor)
    else:
        rosa_audio( "não foi possivel achar o valor da moeda")
        print("não foi possivel achar o valor da moeda")

# fim da função

# filmes lançamento 
def filmes():
    rosa_audio( "Buscando filmes em lançamento")
    requisicao = requests.get("https://api.themoviedb.org/3/movie/upcoming?api_key=" + API_KEY_TMDB + "&language=pt-BR")
    dataJSON = requisicao.json()
    dataFormat = json.dumps(dataJSON, indent=1, ensure_ascii=False)
    # print(dataFormat) 
    
    filmes_lista = []
    
    for filme in dataJSON.get("results", []):
            titulo = filme.get("title", "Título não disponível")
            data_lancamento = filme.get("release_date", "Data não disponível")
            filmes_lista.append((titulo, data_lancamento))
            
    if not filmes_lista:
        print("nenhum filme encontrado")
    else:
        titulo, data_lancamento = filmes_lista[0]
        rosa_audio( "filmes em lançamento " + titulo + "em" + data_lancamento + "")
# executa commandos função

# clima
def clima():
    rosa_audio( "Buscando informações do clima")
    requisicao = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo&appid=" + API_KEY_CLIMA + "&lang=pt_br")
    dataJSON = requisicao.json()
    # dataFormat = json.dumps(dataJSON, indent=1, ensure_ascii=False)
    #print(dataFormat)
    if dataJSON.get("cod") == 200:
        temp = dataJSON["main"]["temp"] - 273.15 
        desc = dataJSON["weather"][0]["description"]
        
        rosa_audio( "em sao paulo esta " + str(temp) + "graus e " + desc)
    else:
        print("não foi possivel obter as informações do clima")
        rosa_audio( "não foi possivel obter as informações do clima")

# tradutor 
def traduzir(text):
    rosa_audio("Iniciando tradução")
    try:        
        text = text.replace("traduza", "").strip()

        tradutor = Translator()
        
        traducao = tradutor.translate(text, dest='pt')
         
        rosa_audio(f"A tradução é: {traducao.text}")
        
    except Exception as e:
        print(f"Erro detalhado na tradução: {str(e)}")  # Debug mais detalhado
        rosa_audio("Desculpe, não consegui traduzir o texto")
    
# calculadora
def calculadora(text):
    rosa_audio("Iniciando cálculo")
    try:
        text = text.replace("calcule", "").replace("quanto é", "").strip()        

        text = text.replace("mais", "+").replace("menos", "-")
        text = text.replace("vezes", "*").replace("dividido por", "/")

        text = text.replace("x", "*")            

        resultado = eval(text)
            
        rosa_audio(f"O resultado é {resultado}")
        
    except Exception as e:
        print(f"Erro no cálculo: {e}")
        print(f"Texto que causou o erro: {text}")
        rosa_audio("Desculpe, não consegui realizar o cálculo")



def executa_comando(text):
    
    text = text.lower()
    
    # fecha a rosa
    
    if "desligue rosa" in text or "desligar rosa" in text:
        rosa_audio("Desligando a Rosa")
        print("Desligando...")
        sys.exit()
        
    # diz as horas
        
    elif "horas" in text or "que horas são" in text:
        rosa_audio("Verificando as horas")
        hora = datetime.datetime.now().strftime('%H:%M')
        frase = f"Agora são {hora}"
        rosa_audio(frase)
    
    # desliga o computador
        
    elif "desligar computador" in text and "15 minutos" in text:
        rosa_audio("Desligando o computador em 15 minutos")
        print("computador desligara em 15 minutos")
        os.system("shutdown - s -t 900")
        
    elif "cancelar desligamento" in text:
        rosa_audio("Cancelando o desligamento do computador")
        print("desligamento do computador foi cancelado")
        os.system("shutdown -a")
        
    # pesquisa no google 
    
    elif "pesquisar" in text and "google" in text:
        rosa_audio("Pesquisando no Google")
        text = str(text).replace("pesquisar", "")
        text = str(text).replace("google","")
        webbrowser.open(f'https://google.com/search?q={text}') 
    
    # pesquisa youtube
    
    elif "pesquisar" in text and "youtube" in text:
        rosa_audio("Pesquisando no YouTube")
        text = str(text).replace("pesquisar","")
        text = str(text).replace("youtube", "")
        webbrowser.open(f'https://youtube.com/results?search_query={text}')
    
    # spotify 
    
    elif "melhor" in text and "track" in text:
        rosa_audio("Abrindo a melhor música")
        webbrowser.open('https://open.spotify.com/intl-pt/track/0Sxyxqs4PXOKRojWomqMrK?si=59f8dcd9a98f4f98')
    elif "melhor" in text and "playlist" in text:
        rosa_audio("Abrindo a melhor playlist")
        webbrowser.open('https://open.spotify.com/playlist/3tQO69FxY5bTEAGqu19p9c?si=NEMKuwBeQ3WU9xA2BvIbEg')
    elif "melhor" in text and "álbum" in text:
        rosa_audio("Abrindo o melhor álbum")
        webbrowser.open('https://open.spotify.com/intl-pt/album/1KerGJUScYGffP3Mjmjz8c?si=USaDLaAiQn2YXGtQRk50Dw')
    elif "playlist" in text and "rock" in text:
        rosa_audio("Abrindo playlist de rock")
        webbrowser.open('https://open.spotify.com/playlist/4tO9NRivwxjNrTKJ5kax4f?si=y2f4rKvST16BgtkIBRsqUg')
    elif 'playlist' in text and 'eletro' in text:
        rosa_audio("Abrindo playlist de música eletrônica")
        webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DZ06evO2zE29q?si=jfhl3tZdR6aP4k4uoH3qMQ')
    elif 'playlist' in text and 'flume' in text:
        rosa_audio("Abrindo playlist do Flume")
        webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DZ06evO3LwGQM?si=UgBflCNFTLSx2XXqhkzjXg')
    elif 'playlist' in text and 'dar' in text:
        rosa_audio("Abrindo playlist Dar")
        webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DZ06evO0JOSZB?si=5c3hfkXDTfqV32uz0pfYNg')
    elif 'playlist' in text and 'blade' in text:
        rosa_audio("Abrindo playlist Blade")
        webbrowser.open('https://open.spotify.com/playlist/0gCNFjw72jmOgLPyIkrGrm?si=pYFe9QXuQ26tvGVRh9ajjw')
    
    # noticias 
    elif "news" in text:
        noticias()
    
    # cotação
    elif "moeda americana" in text:
        cotacao('USD')
    elif "euro" in text:
        cotacao('EUR')
    elif "bitcoin" in text:
        cotacao('BTC')
    
    # filmes em lançamento 
    
    elif "filmes em lançamento" in text:
        filmes()
    
    # clima
    elif "clima" in text:
        clima()
    
    # tradutor
    elif "traduza" in text:
        traduzir(text)
    
    # calculadora
    elif "calcule" in text or "quanto é" in text:
        calculadora(text)
    
    # abrir programas
    
    elif "abrir" in text and "visual studio code" in text:
        rosa_audio("Abrindo Visual Studio Code")
        os.system("code")
        
    elif "abrir" in text and "chrome" in text:
        rosa_audio("Abrindo Google Chrome")
        subprocess.Popen("chrome")
        
    elif "abrir" in text and "bloco de notas" in text:
        rosa_audio("Abrindo Bloco de Notas")
        subprocess.Popen("notepad")
        
    elif "abrir" in text and "calculadora" in text:
        rosa_audio("Abrindo Calculadora")
        subprocess.Popen("calc")
        
    elif "abrir" in text and "docker" in text:
        rosa_audio("Abrindo Docker")
        subprocess.Popen("docker")
        
    elif "abrir" in text and "spotify" in text:
        rosa_audio("Abrindo Spotify")
        subprocess.Popen('"C:/Users/T-GAMER/AppData/Roaming/Spotify/Spotify.exe"') 
        
    elif "abrir" in text and "discord" in text:
        rosa_audio("Abrindo Discord")
        subprocess.Popen("C:/Users/T-GAMER/AppData/Local/Discord/app-1.0.9187/Discord.exe")
        
    elif "abrir" in text and "desenho" in text: # figma
        rosa_audio("Abrindo Figma")
        subprocess.Popen("C:/Users/T-GAMER/AppData/Local/Figma/app-125.2.3/Figma.exe")
        
    elif "abrir" in text and "notion" in text:
        rosa_audio("Abrindo Notion")
        subprocess.Popen("C:/Users/T-GAMER/AppData/Local/Programs/Notion/Notion.exe")
        
    elif "abrir" in text and "streamlabs" in text:
        rosa_audio("Abrindo Streamlabs")
        subprocess.Popen("C:/Program Files/Streamlabs OBS/Streamlabs OBS.exe")
            
    elif "abrir" in text and "hydra" in text:
        rosa_audio("Abrindo Hydra")
        subprocess.Popen("C:/Users/T-GAMER/AppData/Local/Programs/Hydra/Hydra.exe")
        
    elif "abrir" in text and "epic games" in text:
        rosa_audio("Abrindo Epic Games")
        subprocess.Popen("C:/Program Files (x86)/Epic Games/Launcher/Portal/Binaries/Win64/EpicGamesLauncher.exe")
        
    elif "abrir" in text and "oracle" in text:
        rosa_audio("Abrindo Oracle VirtualBox")
        subprocess.Popen("C:/Program Files/Oracle/VirtualBox/VirtualBox.exe")
        
    elif "abrir" in text and "opera" in text:
        rosa_audio("Abrindo Opera GX")
        subprocess.Popen("C:/Users/T-GAMER/AppData/Local/Programs/Opera GX/opera.exe")
        
    elif "abrir" in text and "gerenciador de tarefas" in text:
        rosa_audio("Abrindo Gerenciador de Tarefas")
        os.startfile("taskmgr.exe")
        
# fim da função

# abrir jogos

    elif "abrir" in text and "cat quest" in text:
        rosa_audio("Abrindo Cat Quest")
        os.startfile('"C:/Program Files/Epic Games/CatQuest/Cat Quest.exe"')
        
    elif "abrir" in text and "lego marvel super hero" in text:
        rosa_audio("Abrindo LEGO Marvel Super Heroes 2")
        os.startfile("C:/Program Files (x86)/Steam/steamapps/common/LEGO Marvel Super Heroes 2/LEGOMARVEL2_DX11.exe")
        
    elif "abrir" in text and "valorant" in text:
        rosa_audio("Abrindo Valorant")
        os.startfile("C:/Riot Games/Riot Client/RiotClientElectron/Riot Client.exe")
        
    elif "abrir" in text and "call of duty" in text:
        rosa_audio("Abrindo Call of Duty")
        print("abrindo melhor jogo do mundo")
        os.startfile("C:/Program Files (x86)/Steam/steamapps/common/Call of Duty HQ/cod.exe")
        print("jogo aberto")
        
    elif "abrir" in text and "fortnite" in text:
        rosa_audio("Abrindo Fortnite")
        os.startfile("C:/Program Files/Epic Games/Fortnite/FortniteGame/Binaries/Win64/FortniteClient-Win64-Shipping.exe")
# fim da função


        
# função principal
def main():
    rosa_audio("Olá, como posso ajudar ?")
    
    while True:  # Loop infinito para ouvir e responder
        text = rosa_ouvir()  # Se o usuário falar algo
       
# chama a função main para iniciar o processo

main()