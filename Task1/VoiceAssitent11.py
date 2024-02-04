import pyttsx3
import wikipedia
import datetime

def say_hello():
    engine = pyttsx3.init()
    engine.say("Hello guy's! How can I assist you?")
    engine.runAndWait()

if __name__ == "__main__":
    say_hello()

def get_current_date_time():
    current_date_time = datetime.datetime.now()
    return current_date_time

# Example usage
current_date_time = get_current_date_time()
print(f"Current date and time: {current_date_time}")


voice = pyttsx3.init()
In = input("Searching wikipedia/google :")
result = wikipedia.summary(In,sentences = 2)
print(result)
voice.say(result)
voice.runAndWait()


