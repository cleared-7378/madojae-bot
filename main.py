from email import message
import discord, asyncio, os
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix="마도제 ")
TOKEN = 'OTg3MzU2OTg1NjcyNDk1MTc0.GN2FVW.46HzIgqvc8jv2dwUs4yXXK7hH0K_VxNzGguXLU'

@bot.event
async def on_ready():
    print("MC-C Bot started up")
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="마도제 도움말 [건의사항은 CLEARED#0456]"))

@bot.command()
async def 도움말(ctx):
    e = discord.Embed(title="*마도제봇 도움말*", description="\n.", color = 0xD3D3D3)

    e.add_field(name="마도제 정보", value="마도제 정보를 볼 수 있습니다.\n.", inline = False)
    e.add_field(name="마도제 내정보", value="자신의 디코닉을 보여줍니다.\n.", inline = False)
    e.add_field(name="마도제 봇정보", value="마도제봇의 정보를 볼 수 있습니다.\n.", inline = False)
    e.add_field(name="마도제 위키 (등록명)", value="마도제 위키에 등록된 도시를 간단하게 볼 수 있습니다.\n.", inline=False)
    e.add_field(name="마도제 위키 목록", value="마도제 위키에 등록된 도시와 등록명을 DM으로 보내줍니다.\n.", inline=False)
   
    await ctx.author.send (embed = e)

    await ctx.channel.send("{}님께 도움말을 DM으로 전송했습니다!".format(ctx.author.mention))

@bot.command()
async def 내정보(ctx):
    await ctx.channel.send("{}님의 디코 닉 : {}".format(ctx.author.mention, ctx.author))

@bot.command()
async def 정보(ctx):
    e = discord.Embed(title="마도제", description="마인크래프트 도시 제작\n...", color=0x0000FF)
       
    e.add_field(name="네이버 카페 주소", value="https://cafe.naver.com/gangkyeong\n...", inline = False)
    e.add_field(name="마도제 규칙", value = "https://cafe.naver.com/gangkyeong/6998\n...", inline = False)
    e.add_field(name="모바일 카페대문", value="https://cafe.naver.com/gangkyeong/7578\n...", inline = False)
    e.add_field(name="마도제 대표도시", value="(아래 사진)",inline=False)
    e.set_image (url="https://cdn.discordapp.com/attachments/988788592451137566/988792612251111464/164829e54d95a065.png")

    await ctx.channel.send (embed=e)

@bot.command()
async def 봇정보(ctx):
    e = discord.Embed(title=".마도제봇.", description="마도제 공식 디코봇", color=0x00FF00)

    e.add_field(name="패치노트 및 공지", value="https://discord.com/channels/808123629950468106/987732994993295381", inline = False)
    e.add_field(name="현재 버전", value="ver 0.1.1", inline = False)
    e.add_field(name="문의사항 및 건의사항", value="CLEARED#0456 << 여기로 DM 부탁드립니다 \:)", inline = False)

    await ctx.channel.send (embed=e)

@bot.command()
async def 위키(ctx, arg):
    if arg == "목록":
        list = discord.Embed(title="마도제 위키", description="마도제 위키 MINI ... 도시 목록\n.", color=0x006400)
        list.add_field(name="소한민국 (국가)", value="등록명 : 소한민국\n.", inline=False)
        await ctx.author.send (embed = list)
        await ctx.channel.send("{}님께 마도제 위키 목록을 DM으로 전송했습니다!".format(ctx.author.mention))

    #국기는 set_thumbnail // 사진은 set_image

    elif arg == "소한민국":
        URL = "https://cdn.discordapp.com/attachments/988788592451137566/988788731127406642/unknown.png"
        e = discord.Embed(title="소한민국 (국가)", description="마도제 위키 MINI\n...", color=0x006400)
        e.add_field(name="제작자", value="대니 외 2명", inline=False)
        e.add_field(name="수도    ...", value="성천특별시", inline=True)
        e.add_field(name="대통령    ...", value=".", inline=True)
        e.add_field(name="화폐   ...", value="에메랄드", inline=True)
        e.add_field(name="도시 소개", value="https://cafe.naver.com/gangkyeong/7561\n...", inline=False)
        e.add_field(name="성천특별시 시청", value="(아래 사진)", inline=False)
        e.set_image (url=URL)
        await ctx.channel.send (embed = e)

    else: await ctx.channel.send("찾을 수 없는 도시입니다.")


bot.run(os.environ[TOKEN])