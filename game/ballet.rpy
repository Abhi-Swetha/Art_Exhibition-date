define e = Character("Laura",color="#ffeba9")
define y = Character("You", color="#ffffff")

$ global h
$ global x

label ballet:
    scene ballet
    with fade
    e "This is beautiful! I love the way the ballerina is captured in mid-air. The colors are so vibrant and the movement is so graceful."
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
            if h==3:
                e"are you alright? if you are tired we can sit and rest for a while"
            if h>3:
                e"are you sure ?"
                y"uhhh..."
                y"(i think se asked smt abt the paintin's meaning )"
                call ex
                e"so you {b}{i}DID{/b}{/i} think there was more to it! "
                e"i thought you were nodding to everything i said cuz you were tired"
                y"ofc ! Dude we have been friends for allmost our entire lives, what makes you think {b}{i}I{/i}{/b} would be bored in an {i}Art exhibition!{/i}. -_- ?"
                e"yea , you're right. hehehe"
                e "lets go to the next one!"
                jump artgallerys

            "Actually...":
                call ex
                jump artgallerys

label ex:
    y"Actualy.. i think it might also apply to ourselves, like how we are controled by the invisible thread of socital rules and thoughts of how we might be persived"
    e"That is also there, espeacially with the standing crowd seemingly unmoved by her tears because to them the elegance and grace of the movements is more importent!"
    e"or to us!"
    y":)"
    e"but both ways..."
    "You and Laura" "This piece represents resstriction of a persons will!"
    y"i think.."
    e"i am sure there is a better way to phrase it but , --\(`_`/--)"
