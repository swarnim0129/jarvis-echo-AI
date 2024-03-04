import speech_recognition as sr
import os
import webbrowser
import ai_api_key
from groq import Groq
import random
from gtts import gTTS 


chatStr=""
def chat(query):
    global chatStr
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY")
    )
    text = f"OpenAI response for Prompt:- {query} \n\n"
    chatStr += f"Swarnim: {query}\n Echo: "
    # print(chatStr)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": chatStr,
            }
        ],
        model="mixtral-8x7b-32768",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    # Extract the response from the 'choices' list
    chatStr += f"{chat_completion.choices[0].message.content}\n"
    print(chatStr)
    say(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content

def ai(prompt):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY")
    )
    text = f"OpenAI response for Prompt:- {prompt} \n\n"

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="mixtral-8x7b-32768",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    # Extract the response from the 'choices' list
    text += chat_completion.choices[0].message.content


    
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)
             
    file_path=f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt"
    with open(file_path, "r") as file:
        content = file.read()
        print(content)



# def say_from_file(file_path):
#     if os.path.exists(file_path):
#         with open(file_path, "r") as file:
#             content = file.read()
#             say(content)
#     else:
#         print(f"File not found: {file_path}")

def say(text):
    os.system(f'say "{text}"')


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language="en-uk")
            # print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured, Sorry from Echo" 

if __name__ == '__main__':
    say("Hello, I am Echo A.I.")
    while True:
        print("Listening")
        query=takeCommand()
        sites = [
                    ["youtube", "https://www.youtube.com"],
                    ["google", "https://www.google.com"],
                    ["facebook", "https://www.facebook.com"],
                    ["instagram", "https://www.instagram.com"],
                    ["wikipedia", "https://www.wikipedia.org"],
                    ["twitter", "https://www.twitter.com"],
                    ["linkedin", "https://www.linkedin.com"],
                    ["reddit", "https://www.reddit.com"],
                    ["amazon", "https://www.amazon.com"],
                    ["stackoverflow", "https://www.stackoverflow.com"],
                    ["github", "https://www.github.com"],
                    ["netflix", "https://www.netflix.com"],
                    ["spotify", "https://www.spotify.com"],
                    ["microsoft", "https://www.microsoft.com"],
                    ["apple", "https://www.apple.com"],
                    ["yahoo", "https://www.yahoo.com"],
                    ["bing", "https://www.bing.com"],
                    ["quora", "https://www.quora.com"],
                    ["ebay", "https://www.ebay.com"],
                    ["wordpress", "https://www.wordpress.com"],
                    ["adobe", "https://www.adobe.com"]
                ]
        for site in sites:

            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir..")
                webbrowser.open(f"{site[1]}")
        import subprocess

        if "play music" in query:
            say("Playing music, sir...")
            music_path = "/Users/swarnimsachinbane/Downloads/Let-Her-Go(PagalWorld).mp3"
            
            # Use subprocess.run to play music using the default player
            subprocess.run(["open", music_path], check=True)

        elif "open facetime".lower() in query.lower():
            os.system("open /System/Applications/FaceTime.app")


        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "quit ".lower() in query.lower():
            say("Goodbye Sir...")
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr=""

        else:
            print("Chatting...")
            chat(query)

