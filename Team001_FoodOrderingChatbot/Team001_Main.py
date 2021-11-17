from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
from tabulate import tabulate

bot = ChatBot('Food Ordering Chatbot')

bot_name='Bot'
orders=[]
receipt=[]

conv = open('Team001_Greetings.txt','r').readlines()
order = open('Team001_FoodOrders.txt','r').readlines()

trainer = ListTrainer(bot)

trainer.train(conv)
trainer.train(order)

#retrieve data from Excel file
df=pd.read_excel("Team001_FoodList.xlsx", usecols=[1,2,3]) 
    
def get_response(msg):
    while True:
        response = bot.get_response(msg)
        if 'malay' in msg or 'Malay' in msg:
            #malay menu
            return tabulate(df.head(13), headers=["Item", "Price", "Delivery"], stralign="left", numalign="left", floatfmt=".2f") 
        elif 'mamak' in msg or 'Mamak' in msg:
            #mamak menu
            return tabulate(df.loc[13:31], headers=["Item", "Price", "Delivery"], stralign="left", numalign="left", floatfmt=".2f") 
        elif 'drinks' in msg or 'Drinks' in msg or 'beverage' in msg or 'Beverage' in msg:
            #beverage menu
            return tabulate(df.loc[32:46], headers=["Item", "Price", "Delivery"], stralign="left", numalign="left", floatfmt=".2f") 
        elif 'korean' in msg or 'Korean' in msg:
            #korean menu
            return tabulate(df.loc[47:61], headers=["Item", "Price", "Delivery"], stralign="left", numalign="left", floatfmt=".2f") 
        elif 'japanese' in msg or 'Japanese' in msg:
            #japanese menu
            return tabulate(df.loc[62:86], headers=["Item", "Price", "Delivery"], stralign="left", numalign="left", floatfmt=".2f") 
        #to get orders
        elif msg[0].isdigit():
            #add orders to list
            orders.extend(msg.split()) 
            total = 0
            receipt.clear()
            for x in orders:
                #add orders to receipt
                receipt.append(df.iloc[int(x),0] +" "+"{:.2f}".format(df.iloc[int(x),1]))
                #calculate total of all orders
                total+=df.iloc[int(x),1] 
            receipt.append("Total {:.2f}".format(total))
            return '\n'.join(receipt)
        #to confirm orders
        elif msg=='confirm' or msg=='Confirm':
            return ("Your order is confirmed. Please pay for it when you pick up your orders or when the orders is \ndelivered to you. Thank you for your purchase! Have a nice day and enjoy the orders! :)")
        #to cancel orders
        elif msg[0:6]=="cancel":
            #remove order from orders list
            orders.remove(msg[7:]) 
            total = 0
            receipt.clear()
            for x in orders:
                #generate new receipt with new orders list
                receipt.append(df.iloc[int(x),0] +" "+"{:.2f}".format(df.iloc[int(x),1])) 
                total+=df.iloc[int(x),1]
            receipt.append("Total {:.2f}".format(total))
            return ("The order has been cancelled successfully.")   
        #to show orders
        elif "myorder" in msg:
            return '\n'.join(receipt)   
        else:
            return response

