import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-') # Prefijo para usar el bot

@bot.command('h')
async def ayuda(ctx):
    mensaje = "Funciones: " \
              "\nSuma: -s num1 num2 ... " \
              "\nResta: -r num1 num2 ... " \
              "\nMultiplicación: -m num1 num2 ..." \
              "\nDivición: -d num1 num2 ... "
    await ctx.send(mensaje)

@bot.command('s')
async def sumar(ctx, *args):
    if len(args) < 2:
        await ctx.send('Debe tener almenos 2 numeros (-s num1 num2)')
    else:
        suma = 0
        try:
            for n in args:
                suma += int(n)
            await ctx.send(suma)
        except Exception as x:
            print(type(x).__name__)
            await ctx.send('Datos incorrectos, deben ser numeros')

@bot.command('r')
async def resta(ctx, *args):
    if len(args) < 2:
        await ctx.send('Debe tener almenos 2 numeros (-r num1 num2)')
    else:
        try:
            resta = int(args[0])
            cont = 0
            for n in args:
                if cont != 0:
                    resta -= int(n)
                cont += 1
            await ctx.send(resta)
        except Exception as x:
            print(type(x).__name__)
            await ctx.send('Datos incorrectos, deben ser numeros')

@bot.command('m')
async def multiplicacion(ctx, *args):
    if len(args) < 2:
        await ctx.send('Debe tener almenos 2 numeros (-m num1 num2)')
    else:
        try:
            mul = int(args[0])
            cont = 0
            for n in args:
                if cont != 0:
                    mul *= int(n)
                cont += 1
            await ctx.send(mul)
        except Exception as x:
            print(type(x).__name__)
            await ctx.send('Datos incorrectos, deben ser numeros')

@bot.command('d')
async def divicion(ctx, *args):
    if len(args) < 2:
        await ctx.send('Debe tener almenos 2 numeros (-d num1 num2)')
    else:
        try:
            div = int(args[0])
            cont = 0
            for n in args:
                if cont != 0:
                    div /= int(n)
                cont += 1
            await ctx.send(div)
        except ZeroDivisionError:
            await ctx.send('No se puede dividir entre 0')
        except Exception as x:
            print( type(x).__name__ )
            await ctx.send('Datos incorrectos, deben ser numeros')

bot.run(TOKEN)
