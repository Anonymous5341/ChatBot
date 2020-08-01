import webbrowser as wb
import wikipedia as wiki
import calendar
import requests as r
import socket as s
import random
import smtplib
import datetime
import pyttsx3
import time
import os
import winsound
import googletrans
import translate
import getmac as gm

greeting_text_ques = ['hii bot', 'hello bot', 'hii', 'hello', 'hey', 'hi', 'heyy', 'hii bro', 'hello bro',
                      'hey bro', 'hi bro', 'hello brother', 'hii brother', 'hi brother', 'hi sir',
                      'hello sir', 'hii sir', 'hi sir', 'Namaste', 'hi bot', 'hey bot', 'helloo',
                      'hellooo', 'heyy', 'hii bot ', 'hello bot ', 'hii ', 'hello ', 'hey ', 'hi ',
                      'heyy ', 'hii bro ', 'hello bro','helo'
                      'hey bro ', 'hi bro ', 'hello brother ', 'hii brother ', 'hi brother ', 'hi sir ',
                      'hello sir ', 'hii sir ', 'hi sir ', 'Namaste ', 'hi bot ', 'hey bot ', 'helloo ',
                      'hellooo ', 'heyy ', ]

greeting_text_answer = ['hii', 'hello', 'hey', 'hi', 'heyy', 'hi sir',
                        'hello sir', 'hii sir', 'hi sir', 'Namaste', 'hi brother', 'hello brother',
                        'hey brother', 'hii brother', ]

greeting_msg_ques = ['how are you', 'howz you', 'how about you',
                     'how you doing', 'how\'z you', 'how\'re you', 'how\'re you', 'how are you?',
                     'how\'z you?', 'how you doing?', 'how\'re you?', 'how are you ', 'howz you ',
                     'how about you ', 'how you doing ', 'how\'z you ', 'how\'re you ',
                     'how\'s you','how\'s you ','how\'re you ', 'how are you? ',
                     'how\'z you? ', 'how you doing? ', 'how\'re you? ', 'how are you ?',
                     'how\'z you ?', 'how you doing ?', 'how\'re you ?', 'how are you ? ',
                     'how\'z you ? ', 'how you doing ? ', 'how\'re you ? ', ]

greeting_msg_answer = ['i am good and how are you?', 'good how\'s about you?',
                       'perfect and yours?', 'good and yours', 'good.. yours?', 'perfect..yours?','i am also'
                       'perfect and yours']

user_ans = ['i am good', 'good', 'i am perfect','i am also good','i am also perfect','nice','perfect ',
            'perfect', 'good and thanks', 'me good', 'me perfect', 'me nice']

thanks_msg = ['Thanks', 'Nice', 'perfect', 'good']

info_msg = ['tell me about yourself?', 'whats your name?',
            'where you live?', 'how you doing?', 'know about me?']

eror_msg = ['sorry i don\'t find anything','i think i am lost','oops!!',
            'oops! i think i am lost','sorry! i don\'t know',]

hash_msg = ['#wiki','#search','#open','#quote','#translate','#fact','#info','#advice','#cal','#weather',
            '#calender','#ip_address','#ip','#mac','#mac_address','#beep','#speak']

date_msg = ['date','date ','what is date','date?','today?','today','today ','date today ','date today']

time_msg = ['time','time ','what is time','time?','time?','today','today ','time now ','time now']

text = greeting_msg_ques + greeting_text_ques + user_ans + date_msg+time_msg

main_msg = '''Hi! Here's a list of stuff I can help with you with:
#weather PLACE: Check out the weather at any place.
#wiki NAME: Search Wikipedia for anything you want.
#search QUERY: Search Names According to your Query.
#translate -LANGUAGE_NAME Query: Translates Query in Your Preffered Languages.
#open WEBSITE_NAME: Opens a WebBrowser with your searched Website!
#quote: We’ll send you an awesome quote whenever you want it.
#speak QUERY: Reads the Query You Write.
#fact: Awesome facts, served steaming hot, whenever you want it!
#corona: To get information regarding coronavirus
#info COUNTRY_NAME: Give Basic Information about a country.
#weather COUNTRY_NAME: Give Details of Weather of a country.
#beep : Plays a Beep Sound On Your PC(PERSONAL COMPPUTER).
#ip : It gives Your Current Ip(INTERNET PROTOCOL) Address.
#mac : It gives Your mac Address of Your Computer.
#calender -YEAR: To get current status of Coronavirus in India.
#advice: We’ll send you an awesome advice whenever you want it.'''


# for i in range(len(text)):
#     print(text[i])


while True:
    inp = input("Type To Chat With Bot: ")
    def checkifexist(items):
        for i in range(len(items)):
            if (inp.lower() == items[i]):
                return True
        return False

    def printrandom(items):
        rand = random.choice(items)
        print(rand.strip().capitalize())

    def checkHash(item):
        if(item[0]=='#'):
            items = item.split(' ')
            for i in range(len(hash_msg)):
                if(items[0]==hash_msg[i]):
                    return True
            return False
        


    if(checkifexist(text) == True):
        if(checkifexist(greeting_text_ques) == True):
            printrandom(greeting_text_answer)

        elif(checkifexist(greeting_msg_ques) == True):
            printrandom(greeting_msg_answer)

        elif(checkifexist(user_ans) == True):
            printrandom(thanks_msg)

        elif(checkifexist(date_msg)==True):
            date = datetime.datetime.now()
            date = date.timetuple()
            print(date[2],'-',date[1],'-',date[0])

        elif(checkifexist(time_msg)==True):
            t = time.asctime()
            t = t.split(' ')
            print(t[4])

        elif(inp.lower() == 'quit'):
            break

    elif(checkHash(inp)==True):
        inp = inp.split(' ')
        if(inp[0]=='#wiki'):
            query =""
            for i in range(len(inp)-1):
                query+=inp[i+1]
            w = wiki.summary(query)
            print(w)
        elif(inp[0]=='#open'):
            query =""
            for i in range(len(inp)-1):
                query+=inp[i+1]
            a = wb.open('www.google.com.tr/search?q={}'.format(query))
        elif(inp[0]=='#search'):
            query =""
            for i in range(len(inp)-1):
                query+=inp[i+1]
            a = wiki.search(query,15)
            print(a)
        elif(inp[0]=='#translate'):
            query = ""
            for i in range(len(inp)-2):
                query+=inp[i+2]
            if inp[1][0]== '-':
                lang = inp[1][1:len(inp[1])]
                if len(lang)==2:
                    print(lang)
                    pass
                else:
                    for i in range(len(googletrans.LANGCODES)):
                        if googletrans.LANGCODES.keys == lang:
                            lang = googletrans.LANGCODES.items
                            print(lang)
                
            a = translate.Translator(to_lang=lang).translate(query)
            print(a)
            
        elif(inp[0].lower()=='#quote'):
            url = 'https://quotes.rest/qod?category=management'
            api_token = "AMANDEEP"
            header = {'content-type': 'application/json','Access-Control-Allow-Headers': format(api_token)}
            req = r.get(url,headers=header)
            quote = req.json()['contents']['quotes'][0]['quote']
            author =req.json()['contents']['quotes'][0]['author']
            print(quote,'\n\t\t','BY',author)

        elif(inp[0].lower()=='#info'):
            url ='https://restcountries.eu/rest/v2/name/{}'.format(inp[1])
            req =r.get(url)
            a = req.json()
            name = a[0]['name']
            topdomain = a[0]['topLevelDomain'][0]
            capital =a[0]['capital']
            population = a[0]['population']
            region = a[0]['region']
            currency = a[0]['currencies'][0]['name']
            symbol = a[0]['currencies'][0]['symbol']
            call_code = a[0]['callingCodes'][0]
            print('Name:',name,'\n''Calling Code:',call_code,'\n''Region:',region,'\n''Capital:',
            capital,'\n''Top Level Domain:',topdomain,'\n''Population:',population,'\n'
            'Currency:',currency,'\n''Currency Symbol:',symbol)

        elif(inp[0].lower()=='#advice'):
            url = 'https://api.adviceslip.com/advice'
            req = r.get(url)
            a = req.json()
            advice = a['slip']['advice']
            print(advice)
        
        elif(inp[0].lower()=='#calender' or inp[0].lower()=='#cal'):
            print(inp[1])
            if inp[1][0]=='-':
                string = inp[1][1:len(inp[1])]
                if string.lower() =='today':
                    y=time.localtime().tm_year
                    print(calendar.calendar(int(y)))
                elif len(string)==4:
                    print(calendar.calendar(int(string)))
                else:
                    print('YOU ENTERED A WRONG INPUT ARGUMENT')
            

        elif(inp[0].lower()=='#ip_address' or inp[0].lower()=='#ip'):
            get_host = s.gethostname()
            get_ip = s.gethostbyname(get_host)
            print(f"Your IP Address is: ",get_ip)
        
        elif(inp[0].lower()=='#mac_address' or inp[0].lower()=='#mac'):
            mac = gm.get_mac_address()
            print("Your MAC Address is: ",mac)

        elif(inp[0].lower() =='#weather'):
            api_key = '4187cfb45358eb0a570b1e216b9b127f'
            place =inp[1]
            url =f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}"
            req =r.get(url)
                # desp = req.json()['weather'][0]['description']
            temp = req.json()['main']['temp']
            feel_like = req.json()['main']['feels_like']
            print(F'Current Tempurature: {temp} & Feels Like: {feel_like}')
                
        elif(inp[0].lower()=='#beep'):
            freq = input('Enter Frequency between 38 to 32767: ')
            sound = winsound.Beep(int(freq),1000)
            sound

        elif(inp[0].lower()=='#speak'):
            a = inp[1:len(inp)]
            def listtostring(a):
                str1 =''
                for i in a:
                    str1+=i
                return str1
            query = listtostring(a)
            pyttsx3.speak(query)

        else:
            print('no search')
            print(inp[0])
                
    else:
        printrandom(eror_msg)

        # Todo: Add The Things you can do msg









        