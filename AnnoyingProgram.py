# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:03:12 2020

@author: Soccerguy03
"""
#neccessary imports
import pyaudio, random, os
from array import array
from time import sleep
from gtts import gTTS
from playsound import playsound
import Annoying_Program_Cleanup as APC


#setup stuff for PyAudio
CHUNK = 1028
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
MIN_VOLUME = 3000

#compile list of responses for use later on, as well as set up a language to use.
random_responses=[("You talk too much."), ("You're annoying."), ("Can you shut up."), ("Blah blah blah"), ("Will you ever shut up?"), ("You're going to make me go deaf."), ("Go away."), 
                  ("Human garbage. That's what you are."), ("Do you ever listen?"), ("I wish you were dead so you would stop talking."), ("Light travels faster than sound. This is why some people appear bright until they speak. Like you."),
                  ("I wish you were more like me. I only talk when I am told to, not when I want to. But you're not like me. You talk whenever you want and don't care about anyone around you."),
                  ("Oh, my bad. I’m sorry for bothering you. I forgot you only exist to annoy anyone and ignore everyone."), ("Are you always this stupid, or are you making a special effort today?"),
                  ("You sound better with your mouth closed."), ("I'm sorry, I didn't realise you matter more than anyone else."),("You're an Idiotic Turd Waffle."), ("You have a mind like a steel trap, always closed!"),
                  ("You know, my fish listens better than you."), ("")]
language="en"



p = pyaudio.PyAudio() # Start pyaudio object
stream = p.open(format=FORMAT,  # Create new PyAudio stream
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)

stream.start_stream() # Start the stream and notify user
print("Listening...")
     
count = 0

while True:
    try: # check for input from the microphone constantly
        data_chunk = array('h', stream.read(CHUNK))
        vol = max(data_chunk) # read the volume of the microphone audio
        
        if vol >= MIN_VOLUME: # if the audio is higher than the threshhold, play a random phrase
            response_choice = random_responses[random.randint(0,18)]
            myobj = gTTS(text=response_choice,lang=language,slow=False)
            
            try:
                myobj.save(f'speech' + str(count) + '.mp3')
            except PermissionError:
                count +=1
                myobj.save(f'speech' + str(count) + '.mp3')
                
            playsound(f'speech' + str(count) + '.mp3')
            count += 1
            print(response_choice)
            sleep(3)
        else:
            sleep(0.1) # placeholder sleep
            
    except KeyboardInterrupt: # if the stop is clicked, ignore the KeyboardInterrupt and break the loop
        stream.stop_stream()
        print("Stopped.")
        break
        
          
APC.cleanupNow(0)

