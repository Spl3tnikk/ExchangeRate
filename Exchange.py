import giphy_client as gc
from giphy_client.rest import ApiException
import random as rn
import requests
import tkinter as tk
import datetime as dt
from datetime import *
import pycbrf as cb
from pycbrf import ExchangeRates

inst = gc.DefaultApi()
key = "YOUR KEY FROM GIPHY DEVELOPERS"
for_mat = "gif"


############################################
###### ппоиск валют и их сравнение #########
############################################
date_today = dt.date.today()
date_yesterday = date_today + timedelta(days=-1)

today = ExchangeRates(date_today, locale_en=True) #момент доллара сегодня
yesterday = ExchangeRates(date_yesterday, locale_en=True) #момент доллар вчера\


if today['USD'].value > yesterday['USD'].value:
    search = "rich"
    name = "rich.gif"
else:
    search = "broke"
    name = "broke.gif"
    
#####################################
######    скачивание гифки  #########
#####################################


try:
    response = inst.gifs_search_get(key,search,limit=1,offset=rn.randint(1,100),fmt=for_mat)
    gif_id = response.data[0]
    url_gif = gif_id.images.downsized.url
except ApiException:
    print("OK")

with open(name,'wb') as f:
    f.write(requests.get(url_gif).content)


#####################################
###### вывод гифки и текста #########
#####################################

gifway = "YOUR WAY TO FILE WITHOUT GIF's"+name
if search == "rich":
    textt = "Сегодня курс поднялся"
    color = "#008000"#текст
else:
    textt = "Сегодня курс упал"
    color = "#FF0000"#текст

window = tk.Tk()
window.title("AlphaGIF")
window['bg'] = '#000000'


cors = "Сегондя USD = "+ str(today['USD'].value) + ", а вчера USD = " + str(yesterday['USD'].value)
course = tk.Label(text=cors,  font='Times 20')  #текст
course.pack()


raznica = today['USD'].value - yesterday['USD'].value
raz = tk.Label(text="Разница = " + str(raznica),  font='Times 15')  #текст
raz.pack()

photo = tk.PhotoImage(file = gifway) #гифка
label = tk.Label(image = photo)
label.pack()

stat = tk.Label(text=textt, font='Times 30', fg=color, bg = "black")
stat.pack()





window.mainloop()