'''******************************************************************************

    easylogging v0.1.1 Class Initialization
    Date Last Updated: 07/28/2015
    Created by: Justin Hanley
    Notes:
    Change Log: Please see end of file.

*****************************************************************************'''

import os
import json
import logging.config
from urllib import request, parse

##Workaround for email triggers within intranet security. Written and provided by Vaughn Book
def sendMail(frm,to,subject,message, attachment = None):

    myData = {"from":frm,
              "to":to,
              "subject":subject,
              "messageBody":message,
              "mimeattach":attachment
              }
    mailUrl = 'http://info.arrowheadcu.org/callout/sendmail/sendmail.cfm?'
    request.urlopen(mailUrl + parse.urlencode(myData));
    return True


def setupLogging(
    logoutput_path = __file__
    ,logconfig_file='loggingconfig.json'
    ,default_level=logging.INFO
    ,env_key='LOG_CFG'
):


    #Setup dynamic path to module for I/O
    script_path = os.path.abspath(logoutput_path) # Path to script containing setupLogging() function
    packagedirectory_path = os.path.dirname(script_path) # Directory containing setupLogging() function
    logoutput_path = os.path.join(packagedirectory_path, '__logs') #Output log file location. 
    logconfig_path = os.path.join(os.path.dirname(__file__), logconfig_file) #Input log config file location. This should exist in easylogging directory
    value = os.getenv(env_key, None)

    #print('Log Output Directory:',logoutput_path)
    
    # Look to see if __logs directory exists fo log outputs. If DNE create directory and uses path as working directory
    if not os.path.exists(logoutput_path):
        os.mkdir(logoutput_path)
    os.chdir(logoutput_path)
    

    #Setup logging configuration
    #print('Log Config Path: ',logconfig_path)
    if value:
        logconfig_path = value


    # Locate and open log configuration file
    if os.path.exists(logconfig_path):
        with open(logconfig_path, 'rt') as f:
            addformatter = {'user':os.getlogin()}
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


if __name__ == '__main__':
    print(os.getcwd())
    setupLogging()













'''******************************************************************************
    Change Log

        07/28/2015 - Initial file created by Justin Hanley
        08/27/2015 - Adding email function for email trigger notifications 

*****************************************************************************'''
