# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 14:08:30 2020

@author: Soccerguy03
"""

import os
from time import sleep



def cleanupNow(count):
    while (True):
        try:
            os.remove('speech' + str(count) + '.mp3')
            print("Deleting " + 'speech' + str(count) + '.mp3')
            count += 1
        except PermissionError:
            print("Couldn't delete file, moving on.")
            count += 1
            os.remove('speech' + str(count) + '.mp3')
            print("Deleting " + 'speech' + str(count) + '.mp3')
            
        except:
            print("Cleanup Finished.")
            sleep(2)
            break


    