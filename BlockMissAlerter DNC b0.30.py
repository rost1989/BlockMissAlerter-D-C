# BlockMissAlerter DNC b0.31


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
born2stakeConsAddress = "swthvalcons1xvpttgc3fjwwlefl5axvap5dsq8td67vvxxm5k"
s3ValConsAddress = "swthvalcons1cdu6u5eq7kxxne2macdv0um5tkvwzjl49jqpaf"
degenConsAddress = "swthvalcons1q0a0pk2kjxd8xdjrf2mg6afuwdh4mrp9xst7dk"
seraphConsAddress = "swthvalcons1d0t99ynnfrfd9p79chln3n3wv2ch8ytvga8lh9"
neoeconomyConsAddress = "swthvalcons17k08ukmdwyvcwy64myuv4pe4xsz9usjyuf2lc3"#ERROR?


# FUNCTIONS
# ------------------------------------------------------------------------------
def sound():
    try:
        winsound.Beep(1800, 1000)
    except:
        try:
            playsound(wavFile)
        except:
            pass


# PARAMETERS
# ------------------------------------------------------------------------------
MaxMissedBlocks = 50
MyConsAddress = develandcoConsAddress
maxErrorsAlert = 10
###### -----> To get sound-alerts on MacOS and Linux, install: "pip install playsound" or "pip3 install playsound"  ######


# MAIN
# ------------------------------------------------------------------------------
print ('Welcome, BlockMissAlerter DNC b0.30 is now RUNING')
sound()
while True :    
    try:        
        with urllib.request.urlopen("https://tradescan.switcheo.org/slashing/signing_infos?") as url:
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
        print("Error:", checkErrorCount, "---- 15 sec before next try")
        time.sleep(15)
        
        if int(checkErrorCount) > int(maxErrorsAlert):
            print ('*********MAX ERRORS REACHED*********')
            sound()
        pass
