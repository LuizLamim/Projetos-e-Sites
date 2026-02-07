import discord
from discord.ext import commands

# Configuração de permissões (Intents)
intents = discord.Intents.default()
intents.message_content = True  # Necessário para ler o conteúdo das mensagens