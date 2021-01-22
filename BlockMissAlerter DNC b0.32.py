# BlockMissAlerter DNC b0.32


# LIBRARYS
# ------------------------------------------------------------------------------
import urllib.request
import json
import time
try:
    import winsound
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
            print ('To get sound-alerts on MacOS and Linux, install: "pip install playsound" or "pip3 install playsound')
            pass
        
# -----> To get sound-alerts on MacOS and Linux, install: "pip install playsound" or "pip3 install playsound"  #


# PARAMETERS
# ------------------------------------------------------------------------------
MaxMissedBlocks = 50
MyConsAddress = develandcoConsAddress
maxErrorsAlert = 10

# MAIN
# ------------------------------------------------------------------------------
print ('Welcome, BlockMissAlerter DNC b0.32 is now RUNING')
sound()

while True :    
    try:        
        with urllib.request.urlopen("https://tradescan.switcheo.org/slashing/signing_infos?limit=100") as url:
            info = json.loads(url.read().decode())

            GetValConsInfo =[d for d in info["result"] if d['address'] == MyConsAddress]
            for d in GetValConsInfo:
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
