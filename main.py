import speech_recognition as sr
import os
import webbrowser

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
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

        if "open facetime".lower() in query.lower():
            os.system("open /System/Applications/FaceTime.app")

        

        # say()
