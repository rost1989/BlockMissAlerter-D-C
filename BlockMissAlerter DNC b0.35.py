# BlockMissAlerter DNC b0.35


# LIBRARYS
# ------------------------------------------------------------------------------
import urllib.request
import json
import time
import platform

if platform.system().lower().startswith('win'): #Windows
    print (platform.system())
    from sound import Sound
    import winsound

elif platform.system().lower().startswith('lin'): #Linux
    print (platform.system())
    from subprocess import call
    
elif platform.system().lower().startswith('dar'): #MacOS
    print (platform.system())
    from playsound import playsound
else:
    pass

try:
    import schedule
except ImportError:
    pass
try:   
    from playsound import playsound
except ImportError:
    pass
    
# CONSTANTS
# ------------------------------------------------------------------------------
wavFile = "beep-a.wav" ### -----> "beep-b.wav" is also possible
checkErrorCount = 0

develandcoConsAddress = "swthvalcons1pqnlj0na6k8u9y27j3elrx584mt3380dal0j9s"
intsoLConsAddress = "swthvalcons1gdmnztf3lxdlj8wzu4629p9jlhv5dk9rhcuv4s"
pacificConsAddress = "swthvalcons1zgth3zfku58gqzayaewwtkd6j97jprmfvhzv5p"
guardiansConsAddress = "swthvalcons1yv4v5q0wygl4aypnsr63fkyyuz87vhyh76qzp7"
s3ValConsAddress = "swthvalcons1cdu6u5eq7kxxne2macdv0um5tkvwzjl49jqpaf"
born2stakeConsAddress = "swthvalcons1xvpttgc3fjwwlefl5axvap5dsq8td67vvxxm5k"
neoeconomyConsAddress = "swthvalcons17k08ukmdwyvcwy64myuv4pe4xsz9usjyuf2lc3"
solidstakeConsAddress = "swthvalcons1u2d7efu35r0kamv22z6wzaz3zlnhz3ug67t4aw"
degenConsAddress = "swthvalcons1q0a0pk2kjxd8xdjrf2mg6afuwdh4mrp9xst7dk"
seraphConsAddress = "swthvalcons1d0t99ynnfrfd9p79chln3n3wv2ch8ytvga8lh9"
blockhuntersConsAddress = "swthvalcons17m2ueqqqt8u0jz4rv5kvk4kg0teel4sckytjlc"
seraphstakingConsAddress = "swthvalcons1d0t99ynnfrfd9p79chln3n3wv2ch8ytvga8lh9"

# FUNCTIONS # here you can change the sound type and duration:
# ------------------------------------------------------------------------------
def sound():
    try: #Windows:
        winsound.Beep(1800, 1000) # winsound.Beep(FREQUENCY, DURATION 1SEC=1000)
    except:
        try: #Linux or MacOSX:
            playsound(wavFile) # Select a wav file on #Constants
            # NO MAXIMUM SOUND DURATION ON MACOSX AND LINUX, CHANGE THE WAV FILE IS POSSIBLE 
        except:
            print ('If No sound-alerts on MacOS and Linux, install: "pip install playsound')
            try: #Raspberry Pi:
                call(["aplay", (wavFile)])
            except:
                pass
            
def resetErrorCount():
    global checkErrorCount
    if checkErrorCount != 0:
        checkErrorCount = 0
        print("Reset Error Counter")

def mute():
    try: #Windows:
        Sound.volume_min() # winsound.Beep(FREQUENCY, DURATION 1SEC=1000)
        print("Sound Off")        
    except:
        try: #Linux or MacOSX:
            print("Sound Off")  
        except:
            print ('Get Linux Sound App')
        try: #Raspberry Pi:
            call(["amixer", "-D", "pulse", "sset", "Master", str(0)+"%"])
            print("Sound Off")
        except:
            pass

def unmute():
    try: #Windows:
        Sound.volume_set(volume)
        print('Sound On -- Volume set to:', volume, '%')
    except: 
        try: #Linux or MacOSX:
            print ('Sound On -- Volume set to:', volume, '%')
        except:
            print ('Get Linux Sound App')
        try: #Raspberry Pi:
            call(["amixer", "-D", "pulse", "sset", "Master", str(volume)+"%"])
            print ('Sound On -- Volume set to:', volume, '%')
        except:
            print ('Get Raspberry Sound App')
            pass

def scheduler():
    try:
        schedule.every().day.at(soundOff).do(mute)
        schedule.every().day.at(soundOn).do(unmute)
        schedule.every().day.at("00:00").do(resetErrorCount)
    except:
        print ('If you want to use the Volume Control, install: "pip3 install schedule')
        pass
    
def runPending():
    try:
        schedule.run_pending()
    except:
        pass

        
# -----> To get sound-alerts on MacOS and Linux, install: "pip install playsound" or "pip3 install playsound"  #
# -----> To get maxErrorsAlert clear, install: "pip install schedule"  #


# PARAMETERS
# ------------------------------------------------------------------------------
MaxMissedBlocks = 100
MyConsAddress = guardiansConsAddress
maxErrorsAlert = 10

# Sound Settings
soundOff = "06:00"
soundOn = "17:00"
volume = 50

# MAIN
# ------------------------------------------------------------------------------
print ('Welcome, BlockMissAlerter DNC b0.35 is now RUNING')
sound()
scheduler()



while True :    
    try:        
        with urllib.request.urlopen("https://tradescan.switcheo.org/slashing/signing_infos?limit=100") as url:
            info = json.loads(url.read().decode())

            GetValConsInfo =[d for d in info["result"] if d['address'] == MyConsAddress]
            for d in GetValConsInfo:
                runPending()
                time.sleep(2)
                print ('Height:', info["height"], '-- Missed:',(d['missed_blocks_counter']), '/', MaxMissedBlocks, 'max blocks alert', '-- Errors:', checkErrorCount)
                
                if int(d['missed_blocks_counter']) > MaxMissedBlocks:
                    print ('*********MAX BLOCKS REACHED*********')
                    sound()
                    
    except:       
        checkErrorCount = int(checkErrorCount + 1)
        print("Error:", checkErrorCount, "---- 10 sec before next try")
        time.sleep(10)
        
        if int(checkErrorCount) > int(maxErrorsAlert):
            print ('*********MAX ERRORS REACHED*********')
            sound()
        pass
