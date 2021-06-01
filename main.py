import discord
import os
import requests
import json
from riotwatcher import LolWatcher, ApiError

client = discord.Client()


api_key = 'RGAPI-7b827727-aa04-463e-8ccc-c4e049a42d47'
regiao = 'br1'
watcher = LolWatcher('RGAPI-7b827727-aa04-463e-8ccc-c4e049a42d47')
#me = watcher.summoner.by_name(regiao, 'OdisBy')


def nickreturn(nickname):
  try:
    response = requests.get('https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}'.format(nickname, api_key))
    json_data = json.loads(response.text)
    resultado = json_data['name']
    return resultado;
  except:
    json_data = json.loads(response.text)
    erro = json_data['status', 'status_code']
    if erro == 400:
        print('Pedido ruim!')
    elif KeyError == 'name':
        print("Teste")
    elif erro == 403:
      print('Peça para o desenvolvedor atualizar a api_key')
    elif erro == 404:
        print('Não foi encontrado nenhum jogador com esse nick.')
    else:
        raise
  

@client.event
async def on_ready():
  print('Bot rodando {0.user}'.format(client))

@client.event
async def on_message(message):
  msg = message.content

  if message.author == client.user:
    return
  
  if msg.startswith('.teste'):
    await message.channel.send('testado :sunglasses:')

  if msg.startswith('.nick'):
    nickname = msg.split('.nick ',1)[1]
    resultado = nickreturn(nickname)
    await message.channel.send(resultado)


client.run(os.environ['TOKEN']) #Token = token do discord;

