cloudy = True
boring = True

if cloudy == True and boring == True:
    print("Since it's cloudy and we're bored let's go watch a film")
if cloudy == False or boring == False:
    print("This won't run")
boring = not(boring)
if not(boring):
    print("Now we're not bored")
