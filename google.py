import pyautogui as py
import time as ti
a=True
while a == True:
    print ("1. AniCloud")
    print ("2. Spotify")
    print ("3. Chrunchyroll")
    print ("4. Twitter (+18)")
    print ("5. Übersetzer")
    print ("6. Word")
    print ("7. Discord logo")
    print ("8. Netflix")
    print ("9. GitHub ")
    print ("10. Iserv")
    print ("11. YouTube")
    print ("12. Whats App")

    User_input=input ()
    if User_input == '1':
        py.moveTo (x=1263, y=16)
        py.click ()
        ti.sleep (1)
        py.moveTo (2533, y=112)
        ti.sleep (1)
        py.click ()
        py.moveTo (x=2471, y=159)
        ti.sleep (1)
        py.click ()
        py.write ('https://aniworld.to/')
        ti.sleep (1)
        py.press ('enter')
    elif User_input == '2':
        py.moveTo (x=1263, y=16)
        py.click ()
        ti.sleep (1)
        py.moveTo (2533, y=112)
        ti.sleep (1)
        py.click ()
        py.moveTo (x=2471, y=159)
        ti.sleep (1)
        py.click ()
        py.write ('https://open.spotify.com/collection/tracks')
        py.sleep (1) 
        py.press ('enter')
    elif User_input == '3':
        py.moveTo (x=1263, y=16)
        py.click ()
        ti.sleep (1)
        py.moveTo (2533, y=112)
        ti.sleep (1)
        py.click ()
        py.moveTo (x=2471, y=159)
        ti.sleep (1)
        py.click ()
        py.write ('https://www.crunchyroll.com/de')
        py.sleep (1) 
        py.press ('enter')
    elif User_input == '4':
        py.moveTo (x=1263, y=16)
        py.click ()
        ti.sleep (1)
        py.moveTo (2533, y=112)
        ti.sleep (1)
        py.click ()
        py.moveTo (x=2471, y=159)
        ti.sleep (1)
        py.click ()
        py.write ('https://twitter.com/home')
        py.sleep (1) 
        py.press ('enter')
    elif User_input == '5':
        py.moveTo (x=1263, y=16)
        py.click ()
        ti.sleep (1)
        py.moveTo (2533, y=112)
        ti.sleep (1)
        py.click ()
        py.moveTo (x=2471, y=159)
        ti.sleep (1)
        py.click ()
        py.write ('https://translate.google.com/')
        py.sleep (1) 
        py.press ('enter')
    elif User_input == '6':
        py.moveTo (x=1263, y=16)
        py.click ()
        ti.sleep (1)
        py.moveTo (2533, y=112)
        ti.sleep (1)
        py.click ()
        py.moveTo (x=2471, y=159)
        ti.sleep (1)
        py.click ()
        py.write ('https://www.office.com/launch/word?auth=2&home=1')
        py.sleep (1) 
        py.press ('enter')
    elif User_input == '7':
        py.moveTo (x=1263, y=16)
        py.click ()
        ti.sleep (1)
        py.moveTo (2533, y=112)
        ti.sleep (1)
        py.click ()
        py.moveTo (x=2471, y=159)
        ti.sleep (1)
        py.click ()
        py.write ('https://auto.creavite.co/icons')
        py.sleep (1) 
        py.press ('enter')
    elif User_input == '8':
        py.moveTo (x=1263, y=16)
        py.click ()
        ti.sleep (1)
        py.moveTo (2533, y=112)
        ti.sleep (1)
        py.click ()
        py.moveTo (x=2471, y=159)
        ti.sleep (1)
        py.click ()
        py.write ('https://www.netflix.com/browse')
        py.sleep (1) 
        py.press ('enter')
        py.sleep (2)
        py.moveTo (x=707, y=742)
        py.click ()
    elif User_input == '9':
        py.moveTo (x=1263, y=16)
        py.click ()
        ti.sleep (1)
        py.moveTo (2533, y=112)
        ti.sleep (1)
        py.click ()
        py.moveTo (x=2471, y=159)
        ti.sleep (1)
        py.click ()
        py.write ('https://github.com/')
        py.sleep (1) 
        py.press ('enter')
    elif User_input == '10':
        py.moveTo (x=1263, y=16)
        py.click ()
        ti.sleep (1)
        py.moveTo (2533, y=112)
        ti.sleep (1)
        py.click ()
        py.moveTo (x=2471, y=159)
        ti.sleep (1)
        py.click ()
        py.write ('https://kgs-wtm.de/iserv/app/login?target=%2Fiserv%2Fmail')
        py.sleep (1) 
        py.press ('enter')
        ti.sleep (3)
        py.press ('enter')
    elif User_input == '11':
        py.press ('win')
        ti.sleep (0.5)
        py.write ('youtube')
        py.press ('enter')
    elif User_input == '12':
        py.moveTo (x=1263, y=16)
        py.click ()
        ti.sleep (1)
        py.moveTo (2533, y=112)
        ti.sleep (1)
        py.click ()
        py.moveTo (x=2471, y=159)
        ti.sleep (1)
        py.click ()
        py.write ('https://web.whatsapp.com/')
        py.sleep (1) 
        py.press ('enter')
    elif User_input == 'Lena':
        break