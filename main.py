import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests, json, sys
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def set_alarm():
    from playsound import playsound
    alarmHour = int(input("Enter Hour in 24 hr format: "))
    alarmMin = int(input("Enter Minutes: "))
    #alarmAM = input("am / pm : ")

   # if alarmAM == "pm":
    #    alarmHour += 12

    while True:
        if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
            print("Playing...")
            playsound('C:\\Users\\sqs\\PycharmProjects\\MydearAlexa\\Iphone_Bgm_Remix.mp3')
            break

def weather(city):
    # Enter your API key here
    api_key = "<YOUR API KEY"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name
    city_name = city

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]

        # store the value corresponding
        # to the "pressure" key of y
        # current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        # current_humidiy = y["humidity"]

        # store the value of "weather"
        # key in variable z
        # z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        # weather_description = z[0]["description"]
        return str(current_temperature)

        # print following values
        '''print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description)) 
    else: 
        print(" City Not Found ")
        '''

def take_command():
    try:
        with sr.Microphone() as source:
            print('Im listening go ahead')
            talk('Im listening go ahead')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'dude' in command:
                command = command.replace('dude', '')
                print(command)
    except:
        pass
    return command

def run_dude():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing '+ song)
        # print('New Command is' +command)
        # print('The bot is telling us: Playing' +command)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('Current time is '+time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'sing' in command:
        print('Im ur personal assistant... im here to help you... i can search for you... and have fun with you... I am your personal assistan tu tu tu tu')
        talk('Im ur personal assistant... im here to help you... i can search for you... and have fun with you... I am your personal assistan tu tu tu tu')
    elif 'date' in command:
        talk('sorry my dear, i have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'hi, hello' in command:
        talk('Hi... Nice to see u here')
    elif 'how are you' in command:
        talk('I am good... Thanks for asking')
    elif 'beautiful' in command:
        talk('U r as beautiful as the piece of the moon.')
    elif 'alarm' in command:
        talk('Please enter the below details:')
        set_alarm()
    elif 'weather' in command:
        talk('Please tell the name of the city')
        city = input()
       # city = user_command()
            # weather_api = weather('Hong Kong')
        weather_api = weather(city)
        talk(weather_api + 'degree fahreneit')
    elif 'stop' in command:
        sys.exit()
    else:
        talk('Please say the command again')

while True:
    run_dude()
