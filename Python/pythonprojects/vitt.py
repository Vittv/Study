import discord
from discord.ext import commands
from random import randint
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.command()
async def hello(ctx):
    print('Hello!')


@bot.command()
async def punch(ctx, arg):

    # >punch Whoever

    await ctx.send(f'Punched {arg}')


@bot.command()
async def double_punch(ctx, arg1, arg2):

    # >punch Whoever

    await ctx.send(f'Double punched {arg1} and {arg2}')


@bot.command()
async def info(ctx):

    # ctx = context (information about how the command was executed)

    # >info

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

@bot.command()
async def roll(ctx):

    roll = randint(1, 100)
    print(f'@user rolled {roll}!')


birthdays = []

@bot.command()
async def get_birthday(ctx):

    birthday = input('Please, type in your birthday (YYYY-MM-DD): ')
    try:
        birthday_date = datetime.strptime(birthday, "%Y-%m-%d").date()
        birthdays.append(birthday_date)
        return birthday_date
    
    except ValueError:
        print("Invalid date format. Please enter your birthday in")


def check_birthdays_today():

    today = datetime.now().date()
    for birthday in birthdays:

        if birthday.month == today.month and birthday.day == today.day:
            print(f"Happy Birthday, @user! >w<\nHope you have a great day!")
