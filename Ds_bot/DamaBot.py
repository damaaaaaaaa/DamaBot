import discord 
from discord.ext import commands 
import random
import yt_dlp # type: ignore

permessi = discord.Intents.all ()
permessi.message_content = True

bot = commands.Bot (command_prefix='!', intents=permessi)

@bot.event
async def on_ready ():
    testuale1 = bot.get_channel (1333167074842906648)
    await testuale1.send (f"{bot.user.mention} e' online!")
    print (f"loggato come {bot.user}")

@bot.event
async def on_message (message):
    listaRisposteSeve = ['cock', 'ciolino', 'gay', 'ti scopo', 'bluh', 'sesso']
    mess = message.content.capitalize ()
    if message.author == bot.user:
        return
    if message.author.id == 714733610065985597 and not mess.startswith ('Ciolino') and message.content[0] != '!':
        await message.channel.send (f"{random.choice (listaRisposteSeve)}{message.author.mention}")
    
    elif message.author.id == 714733610065985597 and mess.startswith ('Ciolino'): 
        await message.channel.send (f"{message.author.mention} zitta merdaccia")

    elif message.author.id != 714733610065985597 and mess.startswith ('Ciolino'):
        await message.channel.send (f"Ciolino {message.author.mention}")

    if mess.startswith ('Ciao'):
        await message.channel.send (f"Ciao {message.author.mention}!")

    if message.content.startswith(bot.user.mention) and message.author.id not in (714733610065985597, 711866613594587188, 759132857879756821):
        await message.channel.send (f"{message.author.mention} cazzo vuoi porco dio")

    elif message.content.startswith (bot.user.mention) and message.author.id in (711866613594587188, 759132857879756821):
        await message.channel.send (f"{message.author.mention} Padrone🙏")

    print (f"Nuovo messaggio -> Utente: [{message.author}] Messaggio: [{message.content}]")

    await bot.process_commands (message)

@bot.event          
async def on_message_edit (before, after):
    with open ('logMes.txt', 'a') as f:
        f.write (f"[{before.content}] -> modificato: {after.content} da {after.author}\n")
    print (f"Messaggio modificato -> Utente: [{after.author}] Messaggio precendente: [{before.content}] Dopo: [{after.content}]")
 

@bot.event
async def on_member_join (member):
    Testuale1 = bot.get_channel (1333167074842906648)
    await Testuale1.send (f"Benvenuto {member.mention}!")
    print (f"Un nuovo utente e' entrato nel server -> Utente: [{member.name}]")
    with open ('logUtenti.txt', 'a') as f:
        f.write (f"{member.name} ({member.id} si e' unito al server alle ore {member.joined_at})\n")


@bot.event
async def on_voice_state_update (member, before, after):
    ch = member.guild.system_channel
    if ch is None:
        return 

    if before.self_mute != after.self_mute:
        if after.self_mute:
            await ch.send (f"{member.display_name} si e' messo in mute")
        else:
            await ch.send (f"{member.display_name} si e' tolto il mute")
    elif before.channel != after.channel:
        if before.channel is None and after.channel is not None:
            await ch.send (f"{member.display_name} e' entrato nel canale {after.channel.name}")
        elif before.channel is not None and after.channel is None:
            await ch.send (f"{member.display_name} e' escito dal canale {before.channel.name}")
        elif before.channel is not None and after.channel is not None:
            await ch.send (f"{member.display_name} e' passato da {before.channel.name} a {after.channel.name}")


#COMANDI IMMAGINI / GIF

@bot.command (name='image', aliases=['foto', 'meme', 'immagine'])
async def foto (ctx):
    listaImmagini = [
        'https://i.imgflip.com/2/7d3spl.jpg',
        'https://i.imgflip.com/4/8n82sp.jpg',
        'https://i.imgflip.com/4/4tqto2.jpg',
        'https://i.imgflip.com/2/7d3spl.jpg',
        'https://i.imgflip.com/4/4tqto2.jpg',
        'https://i.pinimg.com/736x/96/38/0e/96380e81e21f3cc6ff5f50d509aec639.jpg',
        'https://i.pinimg.com/736x/73/82/b2/7382b2e8e8c7be98240ef28a2506800e.jpg',
        'https://i.pinimg.com/1200x/5d/12/fa/5d12fac187d1f880c20f1bc8df24bfbf.jpg',
        'https://i.pinimg.com/736x/d3/ad/35/d3ad3533dbf6efcba6f14ace7d0235c8.jpg',
        'https://i.pinimg.com/736x/a9/2a/6e/a92a6e29e9b0661117a8629a582ddb26.jpg',
        'https://i.pinimg.com/736x/0a/8c/0a/0a8c0a91dd10eab5e49236b2b071af48.jpg',
        'https://i.pinimg.com/1200x/68/62/7c/68627c938156308f5b57718e8b9d4e67.jpg',
        'https://i.pinimg.com/736x/f2/4f/95/f24f9515c219303c9f2ae81ea8b9d39e.jpg',
        'https://i.pinimg.com/736x/26/0f/d5/260fd5f74a8766f11477a1e9fc0333e2.jpg',
        'https://i.pinimg.com/736x/93/0a/cb/930acb057460c14cea70cb705b62a024.jpg',
        'https://i.pinimg.com/736x/1b/83/65/1b8365b0ef9ffab35ab6ae7c5be7ff17.jpg',
        'https://i.pinimg.com/736x/b9/52/ba/b952ba11d783aa7ae94458110ff3512a.jpg',
        'https://i.pinimg.com/736x/15/3c/67/153c67560a08321f94101c2c70c4f508.jpg',
        'https://i.pinimg.com/736x/82/29/75/82297524e017fa163d11120ef5a8cb89.jpg',
        'https://i.pinimg.com/736x/ec/40/cf/ec40cfb2541906c957f44d63e73a6c7a.jpg',
        'https://i.pinimg.com/736x/5d/73/6a/5d736a2886e1e3be4a94ceb75f003358.jpg',
        'https://i.pinimg.com/736x/1d/20/f0/1d20f07d3d5cff046eff61c993204248.jpg',
        'https://i.pinimg.com/1200x/c8/a6/57/c8a657d1a52c2352d3b0a99160367303.jpg',
        'https://i.pinimg.com/736x/23/1f/1e/231f1ed8432052a740d412663f85c3d4.jpg',
        'https://i.pinimg.com/736x/ec/06/7d/ec067d40ce93dfdf29f70ff132533931.jpg',
        'https://i.pinimg.com/736x/66/3f/44/663f44615971d6c10843c34b9b4ae087.jpg',
        'https://i.pinimg.com/736x/39/a5/ab/39a5ab2f834e0733d6a373ccf8eabc94.jpg',
        'https://i.pinimg.com/736x/62/6e/64/626e649e891c28cc9495d34be7d800a2.jpg',
        'https://i.pinimg.com/736x/71/74/03/717403bb5d0563d1e3f180b29418e19d.jpg',
        'https://i.pinimg.com/736x/b7/76/33/b77633e84b0c2a6c37c74b32349d510a.jpg',
        'https://i.pinimg.com/736x/d7/11/c1/d711c1610ae0774ef5821ecf59f457f0.jpg',
        'https://i.pinimg.com/736x/0b/c9/92/0bc992924c81ac05035103df1e4f65bf.jpg'
    ]
    if ctx.author.id == 714733610065985597:
        await ctx.send ('https://i.imgflip.com/4/5vlgsf.jpg')
    else:
        await ctx.send (random.choice (listaImmagini))

    
@bot.command (name='gif')
async def gif (ctx):
    listaGif = [
        'https://media.tenor.com/sOx-FmwPgDIAAAAM/missvindicta-vindicord.gif',
        'https://media.tenor.com/oYOrXr2-bV4AAAAm/funny-memes.webp',
        'https://media.tenor.com/mjVzqm78TdcAAAAM/6-1-6-7-meme.gif',
        'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3l5ZWExZW4xODNuZXJ0eGhscnE3N21rcnQ4bjJlbm9keXk5ZGJuNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/lxxOGaDRk4f7R5TkBd/giphy.gif',
    ]
    await ctx.send (random.choice (listaGif))

#COMANDI PER EMBED

@bot.command (name='phishing', aliases= ['tool', 'phish', 'hack', 'hacking'])
async def box (ctx):
    listaLinkPhishing = [
        'https://github.com/htr-tech/zphisher', 
        'https://github.com/wifiphisher/wifiphisher', 
        'https://github.com/gophish/gophish', 
        'https://github.com/UndeadSec/SocialFish',
        'https://github.com/htr-tech/nexphisher'
    ]
    box = discord.Embed (
        colour=random.randint (0, 0xffffff),
        title='PHISHING',
        type='rich',
        description='tool su github per phishing',
        url=random.choice (listaLinkPhishing)
    )
    await ctx.send (embed=box)

 #COMANDI PER EMBED SOCIAL

@bot.command (name='instagram', aliases=['Instagram', 'insta', 'Insta'])
async def insta (ctx):
    box = discord.Embed (
        color= 0xff9bc8,
        title='Instagram',
        type='rich',
        description='Pagina Home di Instagram',
        url='https://www.instagram.com/',
    )
    await ctx.send (embed=box)

@bot.command (name='youtube', aliases=['Youtube'])
async def youtube (ctx):
    box = discord.Embed (
        color=0x600000,
        title='Youtube',
        type='rich',
        description='Pagine home di youtube',
        url='https://www.youtube.com/'
    )
    await ctx.send (embed=box)

@bot.command (name='twitch', aliases=['Twitch'])
async def twitch (ctx):
    box = discord.Embed (
        color=0x800080,
        title='twitch',
        type='rich',
        description='pagine home di twitch',
        url='https://www.twitch.tv/'
    )
    await ctx.send (embed=box)


    #---COMANDI PER LA MUSICA---


ydl_opts = {

    'format': 'bestaudio/best',      
    'noplaylist': True,
    'default_search': 'ytsearch',
    'match_filter': 'duration < 600', 
    'no_warnings': True,
    'verbose': False,
    'retries': 3,
    'preferredcodec':'mp3',
    'geo_bypass': True

}

ydl = yt_dlp.YoutubeDL (ydl_opts)

@bot.command (name='join', aliases=['entra', 'connect'])
async def join (ctx):
    try:
        if not ctx.author.voice:
            print (f"{ctx.author.name} deve essere in un canale vocale per attivare il bot")
            await ctx.send (f"{ctx.author.mention} devi essere connesso a un canale vocale.")
            return
    except Exception as e:
        print ("madonna puttana", e)
    try:
        canale = ctx.author.voice.channel
        await canale.connect ()
    except Exception as e:
        print ("dio cane non va un cazzo", e)
        await ctx.send ("Errore durante la connesione al canale vocale.")
        return
    
    print ("Il bot si e' connesso alla chat vocale")  

@bot.command (name='leave', aliases=['quit', 'quitta', 'disconnetti', 'esci', 'porcodioesci'])
async def disconnect (ctx):
    try:
        if (not ctx.author.voice) or ctx.author.voice_channel != ctx.voice_client.channel:
            print (f"{ctx.author.name} deve essere nel canale vocale del bot per disconnetterlo")
            await ctx.send (f"{ctx.author.mention} devi essere connesso allo stesso canale vocale del bot.")
            return 
    except Exception as e:
        print ('non va una sega per la disconnessione', e)
    try:
        canale = ctx.voice_client
        await canale.disconnect ()
    except Exception as e:
        print ("non va u' cazz", e)
        await ctx.send ('Errore durante la disconessione dal canale.')
        return
    
@bot.command (name='play')
async def play (self, ctx, *, url):
    queue = []
    canzone = ctx.message.attachments.url[0]
    queue.append (canzone)
    print (queue)
    


bot.run("TOKEN")

