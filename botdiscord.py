import discord
from discord.ext import commands

# Configuração de permissões (Intents)
intents = discord.Intents.default()
intents.message_content = True  # Necessário para ler o conteúdo das mensagens

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logado como {bot.user.name}')