# BlockMissAlerter DNC b0.41 (Carbon)


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
try:
    from pygame import mixer
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
mikasaConsAddress = "swthvalcons1xg07uszmnvlxlkf6u4ymmfx2fzq67fa026l9g6"
neoecofundConsAddress = "swthvalcons1nzm34w4r5uu5r6yhs0zgdq0qhg0wuqrhsa9j72"
polarbearConsAddress = "swthvalcons1apz0qlw6c6yaq3afzqauaug2te7gujg32chqnw"

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
            try:
                mixer.init()
                mixer.music.load(wavFile)
                mixer.music.play()
            except:
                print ('If No sound-alerts on Raspberry Pi, install: "pip install pygame')
                pass
        
# -----> To get sound-alerts on MacOS and Linux, install: "pip install playsound" or "pip3 install playsound"  #


# PARAMETERS
# ------------------------------------------------------------------------------
MaxMissedBlocks = 100
MyConsAddress = develandcoConsAddress
maxErrorsAlert = 12

# MAIN
# ------------------------------------------------------------------------------
print ('BlockMissAlerter DNC b0.41 (Carbon) is now RUNING')
sound()

while True :    
    try:        
        with urllib.request.urlopen(f"http://65.21.135.250:1317/cosmos/slashing/v1beta1/signing_infos/{MyConsAddress}") as url:
            ##if IP adress doesnt work, find one there -> https://tm-api.carbon.network/dump_consensus_state
            info = json.loads(url.read().decode())

            GetValConsInfo = info["val_signing_info"]
            missedBlocks = GetValConsInfo['missed_blocks_counter']

            time.sleep(2)
            print ('Height:',GetValConsInfo["index_offset"],'-- Missed:',GetValConsInfo['missed_blocks_counter'],'/',MaxMissedBlocks,'max blocks alert','-- Errors:', checkErrorCount)
                
            if int(GetValConsInfo['missed_blocks_counter']) > MaxMissedBlocks:
                print ('*********MAX BLOCKS REACHED*********')
                sound()
                    
    except:       
        checkErrorCount = int(checkErrorCount + 1)
        print("Error:", checkErrorCount, "---- 20 sec before next try")
        time.sleep(20)
        
        if int(checkErrorCount) > int(maxErrorsAlert):
            print ('*********MAX ERRORS REACHED*********')
            sound()
        pass
