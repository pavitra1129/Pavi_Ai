import speech_recognition as sr
import os 
# cli ai 
print('''
_______  _______          __________________ _______  _______    _______ _________            __       _______ 
(  ____ )(  ___  )|\     /|\__   __/\__   __/(  ____ )(  ___  )  (  ___  )\__   __/  |\     /|/  \     (  __   )
| (    )|| (   ) || )   ( |   ) (      ) (   | (    )|| (   ) |  | (   ) |   ) (     | )   ( |\/) )    | (  )  |
| (____)|| (___) || |   | |   | |      | |   | (____)|| (___) |  | (___) |   | |     | |   | |  | |    | | /   |
|  _____)|  ___  |( (   ) )   | |      | |   |     __)|  ___  |  |  ___  |   | |     ( (   ) )  | |    | (/ /) |
| (      | (   ) | \ \_/ /    | |      | |   | (\ (   | (   ) |  | (   ) |   | |      \ \_/ /   | |    |   / | |
| )      | )   ( |  \   /  ___) (___   | |   | ) \ \__| )   ( |  | )   ( |___) (___    \   /  __) (_ _ |  (__) |
|/       |/     \|   \_/   \_______/   )_(   |/   \__/|/     \|  |/     \|\_______/     \_/   \____/(_)(_______)
    ''')
os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('welcome to pavitra ai version one point O thank you for using pavitra ai');"''')
os.system("cls")
print('''Hello there here is a long cheatsheet of all the commands you can use in pavitra ai:
"hello"
"how are you"
"hi"
"what is your name"
"what is your age"
"what is your favorite colour "
"open browser"
"open chrome"
"open internet explorer"
"open edge"
"open calc"
"open calendar"
"open clock"
"open youtube"
"open gmail"
"open kali"
"open camera"
"open music Player"
"open maps"
"open mail"
"open messaging"
"open microsoft store"
"open movies and tv"
"open photos"
"open weather"
"what is the date"
"what is the time"
"do a addition"
"do a subtraction"
"do a division"
"do a multiplication"
"make a google search"
"what can you do for me"
"how can you help me"
"help me"
"hello how are you"
"who are you"
"tell me a joke"
"exit"
"bye"
''')
recording = sr.Recognizer()
with sr.Microphone() as source: 
    recording.adjust_for_ambient_noise(source)
    print("(speak engine speak a command from the above cheatsheet)")
    audio = recording.listen(source)
try:
    inn = recording.recognize_google(audio)
    print("You said:"+inn) 
except Exception as e:
            print(e)
# commands
expect = "hello"
expect2 = "how are you"
expect3 = "hi"
expect4 = "what is your name"
expect5 = "what is your age"
expect6 = "what is your favorite colour"
expect7 = "open browser"
expect8 = "open Chrome"
expect9 = "open internet explorer"
expect10 = "open edge"
expect11 = "open calc"
expect12 = "open calendar"
expect13 = "open clock"
expect14 = "open YouTube"
expect15 = "open Gmail"
expect16 = "open Kali"
expect17 = "open camera"
expect18 = "open music player"
expect19 = "open maps"
expect20 = "open mail"
expect21 = "open messaging"
expect22 = "open Microsoft store"
expect23 = "open movies and tv"
expect24 = "open photos"
expect25 = "open weather"
expect26 = "whatsapp web"
expect27 = "what is the date"
expect28 = "what is the time"
expect29 = "do a addition"
expect30 = "do a subtraction"
expect31 = "do a division"
expect32 = "do a multiplication"
expect33 = "make a Google search"
expect34 = "how can you help me"
expect35 = "what can you do for me"
expect36 = "help me"
expect37 = "hello how are you"
expect38 = "who are you"
expect39 = "tell me a joke"
expect40 = "exit"
expect41 = "bye"

#Main code 
if inn==expect :
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('hello how can i help');"''')
    print("HELLO, HOW CAN I HELP")
elif inn==expect2 :
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('i am as cool as pavitra jha');"''')
    print("I am as cool as Pavitra Jha")
elif inn==expect3 :
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('hi how can i help');"''')
    print("Hi, HOW CAN I HELP")
elif inn==expect4 :
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('my name is pavitra ai');"''')
    print("My name is pavitra_ai")
elif inn==expect5 :
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('dosent matter');"''')
    print("dosen't matter")
elif inn==expect6 :
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('black and green is my favorite color');"''')
    print("Black & green")
elif inn==expect7 :
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('which browser do you want to open chrome edge or i net explorer');"''')
    print("Which browser")
    print("1-(CHROME)")
    print("2-(EDGE)")
    print("3-(internet explorer)")
    inp = input(">> ")
    exp = "1"
    exp2 = "2"
    exp3 = "3"
    if inp == exp :
        import os
        os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening chrome');"''')
        print("opening Chrome")
        os.system("cd C:\Program Files\Google\Chrome\Application")
        os.system("start chrome.exe")
    elif inp == exp2 :
        import os
        os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening edge');"''')
        print("opening edge")
        os.system("start msedge")
    elif inp == exp2 :
        import os 
        os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening internet explorer');"''')
        print("opening internet explorer")
        os.system("cd C:\Program Files (x86)\Internet Explorer")
        os.system("start iexplore.exe")
elif inn==expect8 :
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening chrome');"''')
    print("opening Chrome")
    os.system("cd C:\Program Files\Google\Chrome\Application")
    os.system("start chrome.exe")
elif inn==expect9:
    import os 
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening internet explorer');"''')
    print("opening internet explorer")
    os.system("cd C:\Program Files (x86)\Internet Explorer")
    os.system("start iexplore.exe")
elif inn==expect10:
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening edge');"''')
    import os
    print("opening edge")
    os.system("start msedge")
elif inn==expect11:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening calculator');"''')
    print("opening calculator")
    os.system("start calculator:")
elif inn==expect12:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening calendar');"''')
    print("opening calendar")
    os.system("start outlookcal:")
elif inn==expect13:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening clock');"''')
    print("opening Clock")
    os.system("start ms-clock:")
elif inn==expect14:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening youtube');"''')
    print("opening Youtube")
    os.system("cd C:\Program Files\Google\Chrome\Application")
    os.system("start chrome.exe youtube.com")
elif inn==expect15:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening gmail');"''')
    print("opening gmail")
    os.system("cd C:\Program Files\Google\Chrome\Application")
    os.system("start chrome.exe gmail.com")
elif inn==expect16:
    import os 
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('starting your hackgod hacking machine');"''')
    print("starting you hacking kali machine")
    os.system("kali")
elif inn==expect17:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening camera');"''')
    print("opening Camera")
    os.system("start microsoft.windows.camera:")
elif inn==expect18:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening music player');"''')
    print("opening Music")
    os.system("start mswindowsmusic:")
elif inn==expect19:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening maps');"''')
    print("opening Maps")
    os.system("start bingmaps:")
elif inn==expect20:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening mail');"''')
    print("opening Mail")
    os.system("start outlookmail:")
elif inn==expect21:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('no such app installed');"''')
    print("opening Messaging ")
    os.system("start ms-chat")
elif inn==expect22:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening microsoft store');"''')
    print("opening Ms-Store")
    os.system("start ms-windows-store")
elif inn==expect23:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening movie and tv');"''')
    print("opening Movies & TV")
    os.system("start mswindowsvideo:")
elif inn==expect24:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening photos');"''')
    print("opening Photos")
    os.system("start ms-photos:")
elif inn==expect25:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening weather');"''')
    print("opening Weather")
    os.system("start bingweather:")
elif inn==expect26:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('opening whatsapp web');"''')
    print("opening whatsapp web")
    os.system("cd C:\Program Files\Google\Chrome\Application")
    os.system("start chrome.exe whatsapp.web.com")
elif inn==expect27:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('The date is');"''')
    print("The Date is :")
    os.system("date /t")
elif inn==expect28:
    import os
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('the time is');"''')
    print("The Time is:")
    os.system("time /t")
elif inn==expect29:
    add = int(input("first digit to add>> "))
    add2 = int(input("second digit to add>> "))
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('the answer is');"''')
    ans = add+add2
    print("the answer is: ",ans)
elif inn==expect30:
    sub = int(input("first digit to sub>> "))
    sub2 = int(input("second digit to sub>> "))
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('the answer is');"''')
    ans = sub-sub2
    print("the answer is: ",ans)
elif inn==expect31:
    div = int(input("first digit to div>> "))
    div2 = int(input("second digit to div>> "))
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('the answer is');"''')
    ans = div//div2
    print("the answer is: ",ans)
elif inn==expect32:
    multiply = int(input("first digit to multiply>> "))
    multiply2 = int(input("second digit to multiply>> "))
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('the answer is');"''')
    ans = multiply*multiply2
    print("the answer is: ",ans)
elif inn==expect33 :
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('what do you want to search just type it but remember do not leave any space in between');"''')
    incle = input("pavi_ai search-# ")
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('searching');"''')
    os.system("cd C:\Program Files\Google\Chrome\Application")
    search = "start chrome.exe https://www.google.com/search?q="+incle
    os.system(search)
elif inn==expect34:
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('i can help you in many ways like opening youtube,telling a joke and doing a google search i have a whole cheatsheet of it above');"''')
    print('''i can help you in many ways like opening youtube,telling a joke and doing a google search i have a whole 
    cheatsheet of it above''')
elif inn==expect35:
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('i can help you in many ways like opening youtube,telling a joke and doing a google search i have a whole cheatsheet of it above');"''')
    print('''i can help you in many ways like opening youtube,telling a joke and doing a google search i have a whole 
    cheatsheet of it above''')
elif inn==expect36:
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('i can help you in many ways like opening youtube,telling a joke and doing a google search i have a whole cheatsheet of it above');"''')
    print('''i can help you in many ways like opening youtube,telling a joke and doing a google search i have a whole 
    cheatsheet of it above''')
elif inn==expect37:
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('i am as cool as pavitra jha');"''')
    print("I am as cool as Pavitra Jha")
elif inn==expect38:
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('i am pavitra ai coded by pavitra jha');"''')
    print("I am as cool as Pavitra ai coded by pavitra jha")
elif inn==expect39:
    import random
    i1 =  os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('there were two friends the first friend said hey whats up then the second friend tells nothing much converting oxygen into carbon dioxide first friend says ohh man how are you able to do that second friend breathing dude ha ha ha');"''')
    i2 =   os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('there were two friends the first friend said hey what are you holding in your hand second friend its a very presious thing if it is not present then all the living civilization will be dead the first friend says bro what is it say fast second friend bro oxygen bro oxygen Hui Hui Hui Hui Hui');"''')
    number = random.randint(1,2)
elif inn==expect40:
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('exiting');"''')
    exit()
elif inn==expect41:
    os.system('''PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('bye bye have a awesome day');"''')
    print("bye!bye!")
    exit()
else :  
    print("its not in my command list so please make sure that you have not said it too fast")
#End Of The Code