import discord
from discord.ext import commands
from discord.ext.commands import check
import os

intents = discord.Intents.default()
intents.message_content = True 
intents.members = True

def is_owner():
    async def predicate(ctx):
        return ctx.author.id == 999470418178080789
    return check(predicate)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_member_join(member):
    cargo_nome = "La comunidad" 
    cargo = discord.utils.get(member.guild.roles, name=cargo_nome)

    if cargo:
        await member.add_roles(cargo)
        print(f'Dei o cargo {cargo.name} para {member.name}')
    else:
        print(f'Cargo "{cargo_nome}" não encontrado!')

    canal_id = 1396175480075452506  
    canal = bot.get_channel(canal_id)

    if canal:
        await canal.send(f"👋 Olá {member.mention}, bem-vindo ao **Kaykypremiere Community**! Não se esqueça de conferir as **<#1396144956829077634>**. 🚀")

@bot.event
async def on_ready():
    print(f'Logado como {bot.user}')


@bot.command()
@is_owner()
async def regras(ctx):
    embed = discord.Embed(
        title="",
        description=(
            "### 1. Seja respeitoso com todos no servidor\n"
            "Queremos que este servidor seja um lugar amigável para todos. Respeite as opiniões, crenças e limites dos outros.\n\n"
            "### 2. Nada de discurso de ódio, racismo ou discriminação\n"
            "Qualquer forma de discurso de ódio, comentários racistas, sexistas ou ataques com base em religião ou identidade não serão tolerados.\n\n"
            "### 3. Sem spam, flood ou propaganda\n"
            "Evite enviar mensagens repetidas, menções desnecessárias, links ou propagandas. Mantenha o chat limpo e agradável.\n\n"
            "### 4. Mantenha o conteúdo apropriado\n"
            "Conteúdo NSFW (impróprio para o trabalho), gore ou ofensivo não é permitido — isso inclui imagens e mensagens.\n\n"
            "### 5. Use os canais corretamente\n"
            "Cada canal tem um propósito. Mantenha-se no tema de cada canal e evite conversas fora de contexto nos espaços específicos.\n\n"
            "### 6. Siga as orientações da equipe\n"
            "Moderadores e administradores estão aqui para manter o servidor seguro e divertido. Siga as instruções quando necessário.\n\n"
            "### 7. Use o bom senso\n"
            "Mesmo que alguma regra não esteja listada aqui, use o bom senso para manter um comportamento adequado.\n\n"
            "_Ao entrar no **Kaykypremiere Community**, você concorda com os [Termos de Serviço](https://discord.com/terms) e [Diretrizes da Comunidade](https://discord.com/guidelines) do **Discord**._"
        ),
        color=discord.Color.blue()
    )

    await ctx.send(embed=embed)

@bot.command()
@is_owner()
async def regras2(ctx):
    embed = discord.Embed(
        title="",
        description=(
            "# 📜 Regras\n"
            "## Para manter o ambiente seguro e acolhedor, siga as regras abaixo com respeito e bom senso."
        ),
        color=discord.Color.blue()
    )

    await ctx.send(embed=embed)

@bot.command()
@is_owner()
async def curso(ctx):
    embed = discord.Embed(
        title="",
        description=(
            "# 🌐 O curso\n"
            "## O curso de edição do Kaykypremiere está em desenvolvimento, ele será lançado com 5 dias de antecedência aqui, com um preço mais barato."
        ),
        color=discord.Color.blue()
    )

    await ctx.send(embed=embed)

CHANNEL_ID = 1396485518614855783  
TIKTOK_RSS_URL = "https://rsshub.app/tiktok/user/kaykypremiere"  

last_video = None


@bot.event
async def on_ready():
    print(f'Logado como {bot.user}')
    check_tiktok.start()


@tasks.loop(minutes=10)
async def check_tiktok():
    global last_video
    feed = feedparser.parse(TIKTOK_RSS_URL)
    if not feed.entries:
        return

    latest = feed.entries[0]
    if latest.link != last_video:
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send(f"🎵 Novo vídeo postado no TikTok: {latest.link}")
        last_video = latest.link

bot.run(os.getenv("DISCORD_TOKEN"))
