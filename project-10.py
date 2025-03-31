# Project-10 : AI CHATGPT API
# Codesphered01010

import requests
import pyfiglet
import itertools
import threading
import time
import sys

url = "https://luminai.my.id"


headers = {
    "content-type": "application/json",
    "API-Key": "YOUR-API-KEY",
    "API-Host": "https://luminai.my.id"
}


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r' + c)
        sys.stdout.flush()
        time.sleep(0.1)

    sys.stdout.write('\r')
    sys.stdout.flush()


def ask(question):
    payload = {"question": question}
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get("answer")


if __name__ == "__main__":
    print(pyfiglet.figlet_format("ChatGPT"))
    print("Enter the question to ask:")
    print()
    while True:
        question = str(input(">>  "))
        if (question == 'q'):
            print(">>  Bye! Thanks for Using...")
            break
        done = False
        t = threading.Thread(target=animate)
        t.start()
        answer = ask(question)
        time.sleep(5)
        done = True
        t.join()
        print(">> ", answer)
        print()
