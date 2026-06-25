define e = Character("Laura",color="#ffeba9")
define y = Character("You", color="#ffffff")
$ global h
$ global x

label invert:
    scene invert
    with fade
    e "Wow, this is beautiful! the composition is also really good!"
    e"ohh! they have the fliped version as well!!"
    e"do you wanna go see it?"

    menu:
        "hmmm.... ":
            
            y"(shii.. i completely zoned out, but staying up late to reserve this place was worth it tho )"
            y"(you can push through it !)"
            y"('you gotta agree with everything the girl says'-how to get a girlfriend 101)"
            y"I am not sure, i am sure its whatever you said !"
            e"oh..."
            e"then , lets move on to the next one?"
            y"yeaa, definetly\n ;;-_- \n haha...."

            $ l += (x-h*0.25)
            $ h+=1

            if h>3:
                e"but still dont you think there might be more to it?"
                y"uhhh..."
                y"(i think i may have seemed uninterseted, fak... )"
                call iax
                jump artgallerys

        "go see the fliped version":
            $ l +=2
            call iax
            jump artgallerys
label  iax:
    scene invertpt2
    with fade
    e "wow, i can see the details in the girl so much better now !"
    y "yea, your ryt,"
    y "....."
    y "do-do you think that c-could be us?"
    y">///<"
    e "I , i am not sure,but i promised i would tell you at the end "
    e"^///^"