import discord
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import datetime

client = discord.Client()
ToDoList={}
order = {}


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send('Hello!')

    #ToDoList
    if message.content.startswith('?'):
        date = datetime.date.today()
        if 'show To Do List' in message.content:
            if ToDoList == {} :
                await message.channel.send('To Do List: all done!')
            else :
                await message.channel.send('To Do List:')
                for show_date in ToDoList :
                    await message.channel.send(show_date)
                    for show_task in ToDoList[show_date] :
                        await message.channel.send(show_task)

        if 'delete To Do List' in message.content:
            ToDoList == {}
            await message.channel.send('To Do List: all done!')
        
        if '+' in message.content:
            task=message.content
            task = task[2:]
            if date not in ToDoList :
                ToDoList[date] = []
            ToDoList[date].append(task)
            await message.channel.send('To Do List:')
            for show_date in ToDoList :
                    await message.channel.send(show_date)
                    for show_task in ToDoList[show_date] :
                        await message.channel.send(show_task)

        if '-' in message.content:
            task=message.content
            task = task[2:]
            ToDoList[date].remove(task)
            await message.channel.send('To Do List:')
            for show_date in ToDoList :
                    await message.channel.send(show_date)
                    for show_task in ToDoList[show_date] :
                        await message.channel.send(show_task)

    #order
    if message.content.startswith('!'):
        global order
        dish = message.content
        if '+' in dish :
            n = dish.find('+')
            num = dish[n+1]
            dish = dish[1:n]
            if dish not in order :
                order[dish] = 0
            order[dish] += int(num)
            for order_dish in order :
                send_order_dish = str(order_dish+ ':'+str(order[order_dish]))
                await message.channel.send(send_order_dish)
        elif '-' in dish :
            n = dish.find('-')
            num = dish[n+1]
            dish = dish[1:n]
            order[dish] -= int(num)
            for order_dish in order :
                send_order_dish = str(order_dish+ ':'+str(order[order_dish]))
                await message.channel.send(send_order_dish)
        if 'delete order' in dish :
            order = {}
            await message.channel.send('No order!')
        if 'show order' in dish:
            for order_dish in order :
                send_order_dish = str(order_dish+ ':'+str(order[order_dish]))
                await message.channel.send(send_order_dish)
            

client.run('OTg3MzQ4MTY4MDM3NDk4OTAw.GXmejo.rrEPyQ5F-c0EEUfDCeNOBCKoCfdsls5QLOXHgU')