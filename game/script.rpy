# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Laura",color="#ffeba9")
define y = Character("You", color="#ffffff")

#all sprites
image L straighthappy = "images/L straighthappy.png"
image L straighttalk = "images/L straighttalk.png" 
image L straightsmile = "images/L straightsmile.png"
image L sidetalk = "images/L sidetalk.png" 
image L sidesmile = "images/L sidesmile.png"
image L sidehappy = "images/L sidehappy.png"
image L closedsmile = "images/L closedsmile.png"
image L closedhappy = "images/L closedhappy.png"


#all backgrounds
image bg room = "images/bg mainplain.png"
image bg artgallery = "images/bg nodoor.png"

#artworks
image ballet= "images/bg ballet.png"
image candle = "images/bg candle.png"
image field = "images/bg field.png"
image invert = "images/bg invert.png"
image invertpt2 = "images/bg invertp2.png"
image sea = "images/bg sea.png"
image sunpencil = "images/bg sunpencil.png"
image slime= "images/bg slime.png"
image uravity = "images/bg uravity.png"

# The game starts here.
default l = 0
default h=0
default x=1
default art=0

$ global h
$ global x

screen artgallerys():
    add "bg artgallery"
    modal True

    imagebutton :
        auto "art_options/ballet_%s.png"
        focus_mask True
        hovered SetVariable("ballet", "ballet")
        unhovered SetVariable("ballet", None)
        action Jump("b_c")

    imagebutton :
        auto "art_options/candle_%s.png"
        focus_mask True
        hovered SetVariable("candle", "candle")
        unhovered SetVariable("candle", None)
        action Jump ("c_c")
        
    imagebutton :
        auto "art_options/field_%s.png"
        focus_mask True
        hovered SetVariable("field", "field")
        unhovered SetVariable("field", None)
        action Jump("f_c")

    imagebutton :
        auto "art_options/invert_%s.png"
        focus_mask True
        hovered SetVariable("invert", "invert")
        unhovered SetVariable("invert", None)
        action Jump("i_c")

    imagebutton :
        auto "art_options/door_%s.png"
        xalign 0.5
        yalign 1
        focus_mask True
        hovered SetVariable("door", "door")
        unhovered SetVariable("door", None)
        action Jump("door_c")

    imagebutton :
        auto "art_options/sea_%s.png"
        focus_mask True
        hovered SetVariable("sea", "sea")
        unhovered SetVariable("sea", None)
        action Jump("S_c")
 
    imagebutton :
        auto "art_options/sunpencil_%s.png"
        focus_mask True
        hovered SetVariable("sunpencil", "sunpencil")
        unhovered SetVariable("sunpencil", None)
        action Jump("sp_c")

    imagebutton :
        auto "art_options/slime_%s.png"
        focus_mask True
        hovered SetVariable("slime", "slime")
        unhovered SetVariable("slime", None)
        action Jump("sl_c")

    imagebutton :
        auto "art_options/uravity_%s.png"
        focus_mask True
        hovered SetVariable("uravity", "uravity")
        unhovered SetVariable("uravity", None)
        action Jump("u_c")

label start:
    scene bg room
    with fade
    
    show L straighthappy 
    y and e " hehe"
    e "I Can't believe we are finally here! This is going to be my next new favorite place!"
    show L straightsmile 

    y "I am glad you like it! I have been here with my friends before and the food is amazing!"

    show L straighttalk
    e"really? you saying it definetly means its awesome! "
    show L straightsmile

    y"They changed the art gallery a bit since the last time I was here, so I am excited to see what they have now!"

    show L straighttalk
    y"This time its also completely new artworks from the last time I was here...>///<"
    y"i thought it would be cool if i seemed like i knew what i was talking about, but i really dont know much about art"
    show L straightsmile
    show L closedhappy
    e"Half the fun of going to an art gallery is just looking at the art and seeing what you like and dont like! You dont have to know anything about art to enjoy it!"
    show L straightsmile
    show L closedhappy
    e"Still , i am happy you put so much thought into this, "
    show L sidetalk
        

    e"and here i thought your confession was a mean prank you pulled, and you agreed to the date to clear your name "
    show L sidesmile
    y"(;><)     \n Well, I expected as much when you agreed to date me if today went well, but I really wanted to ask you out on a date. I really like you, and I wanted to spend time with you..."
    show L closedsmile
    y"i will prove it to you by making this date the best date ever!"
    show L straightsmile
    show L straighthappy
    e"Thanks.."
    e"Then why dont we get started? I am so excited to see what the inside looks like!"
    show L sidehappy
    e" i cant wait to look at all the diffrent kinds of artworks they have here! I heard they have some really cool stuff!"
    scene bg room
    show L straighthappy
    e"but What do you wanna do first? look at the art or go eat?"
    show L straightsmile

    menu:
        "Look at the art first":
            y "Alright, lets go look at the art first!"
            $ l += 1
            jump artgallerys
        "Go eat first":
            y "Alright, lets go eat first!"
            jump food

    return

label food:
    scene bg room
    show L straighttalk 
    e"Alright...."
    scene bg room 
    jump artgallery

label artgallery:
    scene bg artgallery 
    with fade
    show L straighthappy 
    e "Wow, this place is amazing! I can't wait to see all the different kinds of art they have here!"
    show L straighttalk

label artgallerys:
    scene bg artgallery 
    call screen artgallerys 

label alreadyseen:
        y "(didn't we already see that one?)"
        y "(lets choose smt else)"
        jump artgallerys

label doorno:
        y "(Right now?)"
        y "(lets go to eat after veiwing at least 4 artworks!)"
        jump artgallerys

#check if seen
label door_c:
        if art >= 4:
            jump end
        else:
            y "(leave already??, we haven't even seen 4 artworks yet)"
            y "(we can leave after a while)"
            y "(lets see what artwork to look at next!)"
            jump artgallerys

default b_see=False
default c_see=False
default f_see=False
default i_see=False
default s_see=False
default Sp=False
default Sl=False
default u_see =False

label b_c:
    if not b_see:
        $ b_see = True
        $ art +=1
        jump ballet
    else:
        jump alreadyseen

label c_c:
    if not c_see:
        $ c_see = True
        $ art +=1
        jump candle
    else:
        jump alreadyseen

label f_c:
    if not f_see:
        $ f_see = True
        $ art +=1
        jump field
    else:
        jump alreadyseen

label i_c:
    if not i_see:
        $ i_see = True
        $ art +=1
        jump invert
    else:
        jump alreadyseen

label S_c:
    if not s_see:
        $ s_see = True
        $ art +=1
        jump sea
    else:
        jump alreadyseen

label sl_c:
    if not Sl:
        $ Sl = True
        $ art +=1
        jump slime
    else:
        jump alreadyseen

label sp_c:
    if not Sp:
        $ Sp = True
        $ art +=1
        jump sunpencil
    else:
        jump alreadyseen

label u_c:
    if not u_see:
        $ u_see = True
        $ art +=1
        jump uravity
    else:
        jump alreadyseen    

label end:
    e"this the end"
    "pp-[l]"
    "mimimimimimimi"