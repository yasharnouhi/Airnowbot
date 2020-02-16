# !/usr/bin/env python

# -*- coding: utf-8 -*-

from Bot import Token
from telegram.ext import (Updater, CommandHandler)
import logging
from selenium import webdriver

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def start(update, context):
    startshow = '''
    سلام این من میتونم بهت وضعیت هوای تهران رو نشون بدم.
    فقط کافیه از دستور >>/vaziat<< استفاده کنی برو حال کن ...
    Hi i can show you the weather quality in tehran you can use /vaziat to see air polution ,
    and other tings enjoy ...
    '''
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=startshow)


def vaziat(update, context):
    chat_id = update.effective_chat.id
    opt = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    opt.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=opt)
    driver.get('http://aqicn.org/city/iran/tehran/tehran-university/')
    quality = driver.find_element_by_id('aqiwgtvalue').text

    driver.execute_script(
        'window.open("http://www.irimo.ir/far/wd/701-%D9%BE%DB%8C%D8%B4-%D8%A8%DB%8C%D9%86%DB%8C-%D9%88%D8%B6%D8%B9'
        '-%D9%87%D9%88%D8%A7%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86.html?id=17561" , "new window")')
    driver.switch_to_window(driver.window_handles[1])
    degree = driver.find_element_by_xpath('//*[@id="divCurrentWeather"]/table/tbody/tr[1]/td[1]/div[1]').text
    img = driver.find_element_by_xpath('//*[@id="divCurrentWeather"]/table/tbody/tr[1]/td[1]/img').get_attribute('src')
    situation = driver.find_element_by_xpath('//*[@id="divCurrentWeather"]/table/tbody/tr[1]/td[1]/div[2]').text
    intedquality = int(quality)
    if intedquality < 50:

        vaziattext = '''
        خوب من وضعیت کیفیت هوای تهرانو نزدیک یه منطقه دو رو در اوردم :          
                {}  
        هوا {} و {} هست.         
                ولی در کل هوا خیلی خوبه یه نظزم 🙂🙂🙂🙂
                this is polution : {}
                this is the temperature: {}


            '''.format(quality, degree, situation, quality, degree)

        context.bot.send_photo(chat_id=chat_id, photo=img)
        context.bot.send_message(chat_id=chat_id, text=vaziattext)
    elif intedquality > 50 and (intedquality < 100):

        vaziattext = '''
        خوب من وضعیت کیفیت هوای تهرانو نزدیک یه منطقه دو رو در اوردم :          
                {}  
        هوا {} و {} هست.         
                ولی در کل هوا بد نیست یه نظزم 😐😐😐😐
                this is polution : {}
                this is the temperature: {}
                
                
            '''.format(quality, degree, situation , quality , degree)

        context.bot.send_photo(chat_id=chat_id, photo=img)
        context.bot.send_message(chat_id=chat_id, text=vaziattext)
    elif intedquality > 100 and (intedquality < 150):
        vaziattext = '''
        خوب من وضعیت کیفیت هوای تهرانو نزدیک یه منطقه دو رو در اوردم :          
                {}  
        هوا {} و {} هست.         
                ولی در کل هوا بده بره بعضیا یه نظزم ☹️☹️☹️☹️
                this is polution : {}
                this is the temperature: {}


            '''.format(quality, degree, situation, quality, degree)

        context.bot.send_photo(chat_id=chat_id, photo=img)
        context.bot.send_message(chat_id=chat_id, text=vaziattext)
    elif intedquality > 150 and (intedquality < 200):

        vaziattext = '''
        خوب من وضعیت کیفیت هوای تهرانو نزدیک یه منطقه دو رو در اوردم :          
                {}  
        هوا {} و {} هست.         
                ولی در کل هوا خیلی بده یه نظزم 🤢🤢🤢🤢
                this is polution : {}
                this is the temperature: {}


            '''.format(quality, degree, situation, quality, degree)

        context.bot.send_photo(chat_id=chat_id, photo=img)
        context.bot.send_message(chat_id=chat_id, text=vaziattext)
    elif intedquality > 200 and (intedquality < 300):

        vaziattext = '''
        خوب من وضعیت کیفیت هوای تهرانو نزدیک یه منطقه دو رو در اوردم :          
                {}  
        هوا {} و {} هست.         
                ولی در کل هوا در حد مرگ بده یه نظزم 🤮🤮🤮🤮
                this is polution : {}
                this is the temperature: {}


            '''.format(quality, degree, situation, quality, degree)

        context.bot.send_photo(chat_id=chat_id, photo=img)
        context.bot.send_message(chat_id=chat_id, text=vaziattext)
if __name__ == '__main__':
    updater = Updater(Token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('vaziat', vaziat))

    updater.start_polling()
    updater.idle()
