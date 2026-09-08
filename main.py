import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random

words_by_level = {
    "fácil": ["gato", "cachorro", "azul", "vermelho", "carro"],
    "médio": ["amarelo", "verde", "casa", "ônibus", "computador"],
    "difícil": ["importante", "diferente", "aventura", "desafio", "experiência"]
}

print("Escolha o nível de dificuldade:")
print("1- fácil")
print("2- médio")
print("3- difícil")

dificuldade = input("Escreva o nível de dificuldade:")

if dificuldade == "1":
    nível = "fácil"
elif dificuldade == "2":
    nível = "médio"
elif dificuldade == "3":
    nível = "difícil"
else: 
    print("Falha ao executar função")

palavra = random.choice(words_by_level[nível])
print(palavra)

duration = 5  # segundos de gravação
sample_rate = 44100

print("Fale agora...")
recording = sd.rec(
  int(duration * sample_rate), # o número de amostras a serem registradas
  samplerate=sample_rate,      # taxa de amostras
  channels=1,                  # 1 significa gravação mono
  dtype="int16")               # tipo de dados para as amostras registradas
sd.wait()  # aguardando o término da gravação

wav.write("output.wav", sample_rate, recording)
print("Gravação concluída, estou reconhecendo...")

recognizer = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

recognizer = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language="en-US")
    print("Você disse:", text)

    lang = input(
    "Digite o código do idioma:"
    "en = Inglês, "
    "es = Espanhol, "
    "fr = Francês, "
    "de = Alemão, "
    "it = Italiano, "
    "ja = Japonês, "
    "pt = Português, "
    "Digite o código: "
)

    translator = Translator()
    translated = translator.translate(text, dest=lang)  # O 'en' aqui é um código para inglês
    print("🌍 Tradução para o lang:", translated.text)

except sr.UnknownValueError:             # - se o Google não conseguiu entender a fala devido a ruídos ou silêncio
    print("A fala não pôde ser reconhecida.")
except sr.RequestError as e:             # - se não houver conexão com a Internet ou a API estiver indisponível
    print(f"Service error: {e}")
