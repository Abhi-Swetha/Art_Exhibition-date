define e = Character("Laura",color="#ffeba9")
define y = Character("You", color="#ffffff")
$ global h
$ global x

label field:
    scene field
    with fade
    e "Although, the sturation seems a bit high for the colors to me, i am not sure it its a stylistic choice or not.."
    y"the clouds look th ebest in my opinion"
    e "I wonder what the artist intention was, I dont know how to think of this piece.."
    e"what about you?"

    menu:
        "explain how it feels to you":
            $ l+=2
            call fex
            jump artgallerys

        "not suree":
            y"I am not sure...."
            e"oh..."
            e"well... it could be just a simple painting..."
            y"yeaa, definetly\n ;;-_- \n haha...."
            y"sorry,i wasnt paying attention..., anyway lets move on dude-I mean Laura!"
            e"alright, you must be pretty tired. dw worry too much "

            $ l += (x-h*0.25)
            $ h+=1
            if h>=3:
                e"are you alright? if you are tired we can sit and rest for a while"
                y"yea, ofc! i am fine dont worry abt me dud-Laura"
                e"..."
                e"alright"
            if h>3:
                e"but still dont you think there might be more to it?"
                y"uhhh..."
                y"(i think i may have seemed uninterseted... )"
                y"well..."
                call fex
                e"so you {b}{i}DID{/b}{/i} think there was more to it! "
                e"i thought you were nodding to everything i said cuz you were bored"
                y"ofc not! Dude we have been friends for almost our entire lives, what makes you think {b}{i}I{/i}{/b} would be bored in an {i}Art exhibition!{/i}. -_- ?"
                e"yea , you're right. hehehe"
                e "lets go to the next one!"
                $ h=1
                jump artgallerys
    return
        
label fex:
    y"I think the intent of this piece must be to give off a cool summer vibe?  "
    e"i can see that, but if that was the intention wouldnt the colors saturation be a {b}{i}bit{/i}{/b} less saturated?, whatcha think?"
    y"hmmm...well what we consider a summer vibe may be diffrent from their interpretation of it, yk?"
    y"like how both us may have diffrent idea of what an ideal season is?"
    e"ahhh, that makes sense! may to them {b}summer{/b} must be birght sun and criket sound?"
    y"smt like that!, afterall don't think the best part viewing artworks is to see how diffrent people have diffrent interpratations about the {i}same{/i} exact thing!"
    return