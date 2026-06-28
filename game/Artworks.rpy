image B ="cg3/ballet.png"
image S ="cg3/sea.png"
image Sl ="cg3/slime.png"
image F ="cg3/field.png"
image I ="cg3/filp.png"
image I2 ="cg3/filp2.png"
image Su ="cg3/sun.png"
image U ="cg3/uravity.png"
image C ="cg3/candle.png"
image locked="cg3/locked.png"

init python:
    gallery=Gallery()

    gallery.button("ballet")
    gallery.condition("persistent.ballet")
    gallery.unlock_image("ballet")
    gallery.image("B")
    
    gallery.button("sea")
    gallery.condition("persistent.sea")
    gallery.image("S")
    gallery.unlock_image("sea")
    
    gallery.button("slime")
    gallery.condition("persistent.slime")
    gallery.unlock_image("slime")
    gallery.image("Sl")

    gallery.button("sunpencil")
    gallery.condition("persistent.sun")
    gallery.unlock_image("sunpencil")
    gallery.image("Su")
    

    gallery.button("field")
    gallery.condition("persistent.field")
    gallery.unlock_image("field")
    gallery.image("F")
    

    gallery.button("invert")
    gallery.condition("persistent.invert")
    gallery.unlock_image("invert")
    gallery.image("I")
    gallery.unlock_image("invertpt2")
    gallery.image("I2")
    gallery.condition("persistent.invert2")
    

    gallery.button("uravity")
    gallery.unlock_image("uravity")
    gallery.image("U")
    gallery.condition("persistent.uravity")

    gallery.button("candle")
    gallery.unlock_image("candle")
    gallery.image("C")
    gallery.condition("persistent.candle")

    #gallery.button("Friends")
    #gallery.unlock_image imScale("cg/friend.png",540 , 304)
    #gallery.condition("persistent.bad_end")

    #gallery.button("Lovers")
    #gallery.unlock_image imScale("cg/lovers.png",540 , 304)
    #gallery.condition("persistent.good_end")
