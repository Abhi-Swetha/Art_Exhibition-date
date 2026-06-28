screen endings():
    tag menu

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        #style "game_menu_outer_frame"
        xalign 0.5
        yalign 1.0
        default page = 1
        hbox:
            spacing 20
            xalign 0.5
            xoffset -30
            yoffset 870
            textbutton "Page 1" action SetScreenVariable("page",1)
            textbutton "Page 2" action SetScreenVariable("page",2)

        hbox:
            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"
        if page == 1 :     
            textbutton _(">") action SetScreenVariable("page",2):
                text_size 140
                xalign 0.5
                yalign 0.5
                xoffset 900
        elif page == 2 :     
            textbutton _("<") action SetScreenVariable("page",1):
                text_size 140
                xalign 0.5
                yalign 0.5
                xoffset -900

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            if page == 1:
                grid 3 2:
                    spacing 30
                    add gallery.make_button(name="ballet",unlocked="cg/ballet.png",locked="cg/locked.png")
                    add gallery.make_button(name="sea",unlocked="cg/sea.png",locked="cg/locked.png")
                    add gallery.make_button(name="slime",unlocked="cg/slime.png",locked="cg/locked.png")
                    add gallery.make_button(name="sunpencil",unlocked="cg/sun.png",locked="cg/locked.png")
                    add gallery.make_button(name="field",unlocked="cg/field.png",locked="cg/locked.png")
                    add gallery.make_button(name="invert",unlocked="cg/filp.png",locked="cg/locked.png")

            elif page==2:
                grid 2 2:
                    yoffset 200
                    spacing 30
                    add gallery.make_button(name="uravity",unlocked="cg/uravity.png",locked="cg/locked.png")
                    add gallery.make_button(name="candle",unlocked="cg/candle.png",locked="cg/locked.png")
    use gallery_nav
    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label "Album"

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

screen Album():
    tag menu

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"
        xalign 0.5
        yalign 1.0
        hbox:
            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            grid 2 2:
                spacing 30
                add gallery.make_button(name="ballet",unlocked="cg/ballet.png",locked="cg/locked.png")
                add gallery.make_button(name="sea",unlocked="cg/sea.png",locked="cg/locked.png")

                #add gallery.make_button(name="Friends",unlocked="cg/friend.png",locked="cg/locked.png")
                #add gallery.make_button(name="Lovers",unlocked="cg/love.png",locked="cg/locked.png")
    use gallery_nav
    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label "Album"

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")