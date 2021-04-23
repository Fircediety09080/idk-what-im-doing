import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/")


admins = [443190708665581602,397229775053389835,430274415318663178]
banned = []
botid = [833471279331672075]

def Checkadmin(id):
    if id in admins:
        return True
    else:
        return False

#ban word
@bot.command()
async def nono(ctx, word):
    if not Checkadmin(ctx.author.id):
        return
    banned.append(word)
    await ctx.send(f'@everyone {ctx.author} has delcared u can`t use {word}')

#delete message
@bot.event
async def on_message(ctx):
    return ctx.author.id == 833471279331672075
    for word in ctx.content.split(" "):
        if word in banned:
            await ctx.delete()

    await bot.process_commands(ctx)


#unban word
@bot.command()
async def okok(ctx, word):
     if not Checkadmin(ctx.author.id):
        return
     
     if word in banned:
        banned.pop(banned.index(word))
        await ctx.send(f'@everyone {ctx.author} has delcared u can use {word}')
     else:
       await ctx.send(f'usable word')

#list banned words
@bot.command()
async def lnono(ctx):
    for word in banned:
        await ctx.send(f'{word}')


@bot.command()
async def epic(ctx, *, arg):
    await ctx.send(arg)




if __name__ == "__main__":
    with open("token.text") as f:
        token = f.read()


    bot.run(token)
