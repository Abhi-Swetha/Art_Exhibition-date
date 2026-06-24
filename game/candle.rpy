define e = Character("Laura",color="#ffeba9")
define y = Character("You", color="#ffffff")
$ global h
$ global x
$ global art

label candle:
    $art+=1
    scene candle
    with fade
    e "i love the use of watercolor for the background!"
    e"it adds a lot of dimention and creates a soft vibe around the painting"
    e"what do you think?"

    menu:
        "hmmm.... ":
            
            y"(shii.. i completely zoned out, but staying up late to reserve this place was worth it tho )"
            y"(you can push through it !)"
            y"('you gotta agree with everything the girl says'-how to get a girlfriend 101)"
            y"I am not sure, i am sure its whatever you said !"
            e"oh..."
            e"well... it could be just a simple painting..."
            y"yeaa, definetly\n ;;-_- \n haha...."

            $ l += (x-h*0.25)
            $ h+=1

            if h>3:
                e"but still dont you think there might be more to it?"
                y"uhhh..."
                y"(i think i may have seemed uninterseted, fak... )"


            jump artgallerys