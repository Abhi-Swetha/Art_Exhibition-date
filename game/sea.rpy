define e = Character("Laura",color="#ffeba9")
define y = Character("You", color="#ffffff")
$ global h
$ global x

label sea:
    scene sea
    with fade
    e "Wow, this is beautiful! I love the way the ballerina is captured in mid-air. The colors are so vibrant and the movement is so graceful."
    e"the ballerina dosent seem so happy though,"
    e "I wonder what the artist was trying to convey with this painting. Maybe it's a commentary on the invisible struggles or ristricktion on those we admire?."
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