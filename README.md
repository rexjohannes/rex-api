# rex-api

You can use the Otter API with https://api-otter--rexjohannes.repl.co/

Example:

Discord.py:

@client.command()
async def otter(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://api-otter--rexjohannes.repl.co/') as r:
            res = await r.text()
            await ctx.send(res)
            
            
            
You can use the Dog API with https://api-dog--rexjohannes.repl.co/

Example:

Discord.py:

@client.command()
async def dog(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://api-dog--rexjohannes.repl.co/') as r:
            res = await r.text()
            await ctx.send(res)
            

You can use the Squirrel API with https://api-squirrel--rexjohannes.repl.co/
Example:

Discord.py:

@client.command()
async def squirrel(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://api-squirrel--rexjohannes.repl.co/') as r:
            res = await r.text()
            await ctx.send(res)           
          
You can see the Status here: http://api.rex-bot.ga/
