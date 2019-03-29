import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
import configparser
import sys

config = configparser.RawConfigParser()#load config parser
configFilePath = r'C:\Users\ccampagn\Documents\Python\BergLake\config.ini'#file path of config file
config.read(configFilePath)#read config file

try:#try/except block
    browser = config.get('file', 'browser')#get browser from file
    website = config.get('file', 'website')#get website from file
    textfile = config.get('file', 'textfile')#get textfile from file
    fromaddr = config.get('file', 'from')#get fromaddress from file
    toaddrs = config.get('file', 'to')#get toaddress from file
    username = config.get('file', 'username')#get username from file
    password = config.get('file', 'password')#get password from file
    mailserver = config.get('file', 'mailserver')#get mailserver from file
except configparser.NoOptionError :#except with no options error
    print('could not read configuration file')#Error message if can't read 
    sys.exit(1)  #exit program on error
try:#try/except block
    browser = webdriver.Firefox(executable_path=browser)#get brower
    browser.get(website)#website to check
    time.sleep(5)#slow thing down to process
except Exception as e:
    file_obj = open(textfile,"a") #open text file
    file_obj.write(str(datetime.datetime.now())+str(e)+" browser\n") #write to text for browser error
    file_obj.close()#close text file
try:#try/except block
    restype = browser.find_element_by_id('selResType')#get element of res type
    restype.send_keys('Backcountry')#get element of backcountry
    time.sleep(5)#slow thing down to process
except Exception as e:
    file_obj = open(textfile,"a") #open text file
    file_obj.write(str(datetime.datetime.now())+str(e)+" res type\n") #write to type for res type error 
    file_obj.close()#close text file
try:#try/except block
    resmonth = browser.find_element_by_id('selArrMth')#get element of selarrmth
    resmonth.send_keys(Keys.ENTER)#down key
    time.sleep(5)#slow thing down to process
    for _ in range(datetime.datetime.now().month,8):#loop thru month to get right month
        resmonth.send_keys(Keys.DOWN)#press the down key
        time.sleep(5)#slow thing down to process
    resmonth.send_keys(Keys.ENTER)#press enter key
    time.sleep(5)#slow thing down to process
    resday = browser.find_element_by_id('selArrDay')#get element of selarrday
    resday.send_keys(Keys.ENTER)#press enter key
    time.sleep(5)#slow thing down to process
    for _ in range(13):#loop thru until get 
        resday.send_keys(Keys.DOWN)#down key
        time.sleep(5)#slow thing down to process
    resday.send_keys(Keys.ENTER)#enter key
    time.sleep(5)#slow thing down to process
except Exception as e:
    file_obj = open(textfile,"a") #open text file
    file_obj.write(str(datetime.datetime.now())+str(e)+" date\n") #write to text for date error
    file_obj.close()#close text file
try:#try/except block
    restentpad = browser.find_element_by_id('selTentPads')#get element for tent pads
    restentpad.send_keys('1')  #send tent pads number
    time.sleep(5)#slow thing down to process
except Exception as e:
    file_obj = open(textfile,"a") #open text file
    file_obj.write(str(datetime.datetime.now())+str(e)+" tent pad\n") #write to tent pad
    file_obj.close()#close text file
try:#try/except block
    content = browser.find_element_by_id('selItineraryResource')#get element for what available
    content = content.find_elements_by_class_name('avail')
except Exception as e:
    file_obj = open(textfile,"a") #open text file
    file_obj.write(str(datetime.datetime.now())+str(e)+" find elements\n") #write to text for error find elements 
    file_obj.close()#close text file
try: #try/except block
    match=False#set match to false
    msg =""
    for x in content:#loop thru the content that was return 
        text=x.text.split(' - ')[1]
        if text=="Emperor Falls" or text=="Marmot" or text=="Berg Lake" or text=="Rearguard" or text=="Robson Pass" :#check if any available is number 30
            msg=msg +text+" "#msg to sent as text               
            match=True#set match to true
    if match:#running if content greater than 1
        server = smtplib.SMTP(mailserver)#set the mail server
        server.ehlo()#say hello to other server
        server.starttls()#start secure connection
        server.login(username,password)#login using username and password
        server.sendmail(fromaddr, toaddrs, msg)#send mail 
        server.quit()#exit the server
        file_obj = open(textfile,"a") #open text file
        file_obj.write(str(datetime.datetime.now())+" "+msg+" - Available\n") #write to file for none available
        file_obj.close()#close text file
    else:
        file_obj = open(textfile,"a") #open text file
        file_obj.write(str(datetime.datetime.now())+" - None\n") #write to file for none available
        file_obj.close()#close text file
except Exception as e:
    file_obj = open(textfile,"a") #open text file
    file_obj.write(str(datetime.datetime.now())+str(e)+" txt\n") #error to problem with txt
    file_obj.close()#close text file

    
