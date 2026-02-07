import discord
from discord.ext import commands

# Configuração de permissões (Intents)
intents = discord.Intents.default()
intents.message_content = True  # Necessário para ler o conteúdo das mensagens

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logado como {bot.user.name}')

@bot.event
async def on_message(message):
    # Evita que o bot responda a si mesmo
    if message.author == bot.user:
        return

    # Verifica se há links na mensagem
    if "http://" in message.content.lower() or "https://" in message.content.lower():
        await message.delete()
        await message.channel.send(f"Hey {message.author.mention}, não é permitido enviar links neste canal!", delete_after=5)
    
    # Permite que outros comandos continuem funcionando
    await bot.process_commands(message)

# SEU_TOKEN_AQUI' 
bot.run('SEU_TOKEN_AQUI')