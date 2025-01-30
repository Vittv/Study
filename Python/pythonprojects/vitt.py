import discord
from discord.ext import commands
from discord.ext import tasks
from random import randint
from datetime import datetime
import pytz

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=">", intents=intents)

# EVENTS:

joined = []

@bot.event
async def on_member_join(member:discord.member):            # Greets new members as they join the server
    channel = bot.get_channel(544577606150914057)                # and adds their name to a list.
    await channel.send(f'Welcome {member.display_name}!')
    joined.append(member.display_name)


left = []

@bot.event
async def on_member_remove(member:discord.member):                  # Notifies when someone leaves the server
    channel = bot.get_channel(544577606150914057)                        # and adds their name to a list.
    await channel.send(f'{member.display_name} left the server.')
    left.append(member.display_name)


# COMMANDS:

@bot.command()
async def roll(ctx):

    roll = randint(1, 100)
    await ctx.send(f'{ctx.author.display_name} rolled {roll}!')

est = pytz.timezone('America/New_York')
birthdays = []

@bot.command()
async def get_birthday(ctx):

    current_time_est = datetime.now(est)

    user = ctx.author                                                   # Grabs the message's author

    await ctx.send('Please, type in your birthday (YYYY-MM-DD): ')
    try:
        message = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30)
        birthday_date = datetime.strptime(message.content, "%Y-%m-%d").date()
        birthdays.append((user, birthday_date))
        await ctx.send(f'Thank you, {user.mention}. Your birthday has been recorded.')
        return birthday_date
    
    except ValueError:
        print('Invalid date format. Please enter your birthday in (YYYY-MM-DD): ')

@tasks.loop(hours=12)
async def check_birthdays():

    today = datetime.now(est).date()
    for user, birthday in birthdays:

        if birthday.month == today.month and birthday.day == today.day:

            channel = bot.get_channel(918339121179664447)  
            await channel.send(f'Happy Birthday, {user.mention}! >w<\nHope you have a great day!')

@bot.event
async def on_ready():
    print('Bot is ready.')
    check_birthdays.start()

# runs the bot
bot.run()
