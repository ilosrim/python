from transliterate import to_cyrillic, to_latin
import re 
import telebot

matn = input("Matn kiriting, men uni krilda bo'lsa, lotinga, lotinda bo'lsa, krilga o'girib beraman: \n")

def has_cyrillic(text):
  return bool(re.search('[а-яА-Я]', text))

if has_cyrillic(matn):
  print(to_latin(matn))
else:
  print(to_cyrillic(matn))

  
bot = telebot.TeleBot("5230689513:AAFVs9jpmHXu00LmfCIwsc-7j6d9HzgGlTc", parse_mode=None)