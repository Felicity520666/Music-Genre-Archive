default instrument_page = None
screen music_genre_popup(genre):
    model True

    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)

        vbox:
            spacing 20

            if genre == "classical":
                text "Extra Information: violin, piano, and cello." size 36
                text "Those three instruments are foundational pillars of Western classical music." size 26
                textbutton "Violin":
                    action [SetVariable("instrument_page", "violin"), Show("instrument_info_popup")]

                textbutton "Piano":
                    action [SetVariable("instrument_page", "piano"), Show("instrument_info_popup")]

                textbutton "Cello":
                    action [SetVariable("instrument_page", "cello"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()
                    
            elif genre == "jazz":
                text "Extra Information: violin, piano, and cello." size 36
                text "Those three instruments are foundational pillars of Western classical music." size 26
                textbutton "Violin":
                    action [SetVariable("instrument_page", "violin"), Show("instrument_info_popup")]

                textbutton "Piano":
                    action [SetVariable("instrument_page", "piano"), Show("instrument_info_popup")]

                textbutton "Cello":
                    action [SetVariable("instrument_page", "cello"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()
                    
            elif popup_page == "blues":
                text "Extra Information: violin, piano, and cello." size 36
                text "Those three instruments are foundational pillars of Western classical music." size 26
                textbutton "Violin":
                    action [SetVariable("instrument_page", "violin"), Show("instrument_info_popup")]

                textbutton "Piano":
                    action [SetVariable("instrument_page", "piano"), Show("instrument_info_popup")]

                textbutton "Cello":
                    action [SetVariable("instrument_page", "cello"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()
                    
            elif popup_page =="country":
                text "Extra Information: violin, piano, and cello." size 36
                text "Those three instruments are foundational pillars of Western classical music." size 26
                textbutton "Violin":
                    action [SetVariable("instrument_page", "violin"), Show("instrument_info_popup")]

                textbutton "Piano":
                    action [SetVariable("instrument_page", "piano"), Show("instrument_info_popup")]

                textbutton "Cello":
                    action [SetVariable("instrument_page", "cello"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()
                    
            elif popup_page =="rock":
                text "Extra Information: violin, piano, and cello." size 36
                text "Those three instruments are foundational pillars of Western classical music." size 26
                textbutton "Violin":
                    action [SetVariable("instrument_page", "violin"), Show("instrument_info_popup")]

                textbutton "Piano":
                    action [SetVariable("instrument_page", "piano"), Show("instrument_info_popup")]

                textbutton "Cello":
                    action [SetVariable("instrument_page", "cello"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()
                        
            elif popup_page =="soul":
                text "Extra Information: violin, piano, and cello." size 36
                text "Those three instruments are foundational pillars of Western classical music." size 26
                textbutton "Violin":
                    action [SetVariable("instrument_page", "violin"), Show("instrument_info_popup")]

                textbutton "Piano":
                    action [SetVariable("instrument_page", "piano"), Show("instrument_info_popup")]

                textbutton "Cello":
                    action [SetVariable("instrument_page", "cello"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()
                  
            elif popup_page =="funk":
                text "Extra Information: violin, piano, and cello." size 36
                text "Those three instruments are foundational pillars of Western classical music." size 26
                textbutton "Violin":
                    action [SetVariable("instrument_page", "violin"), Show("instrument_info_popup")]

                textbutton "Piano":
                    action [SetVariable("instrument_page", "piano"), Show("instrument_info_popup")]

                textbutton "Cello":
                    action [SetVariable("instrument_page", "cello"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()

            elif popup_page =="reggae":
                text "Extra Information: violin, piano, and cello." size 36
                text "Those three instruments are foundational pillars of Western classical music." size 26
                textbutton "Violin":
                    action [SetVariable("instrument_page", "violin"), Show("instrument_info_popup")]

                textbutton "Piano":
                    action [SetVariable("instrument_page", "piano"), Show("instrument_info_popup")]

                textbutton "Cello":
                    action [SetVariable("instrument_page", "cello"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()

            elif popup_page =="electronic":
                text "Extra Information: violin, piano, and cello." size 36
                text "Those three instruments are foundational pillars of Western classical music." size 26
                textbutton "Violin":
                    action [SetVariable("instrument_page", "violin"), Show("instrument_info_popup")]

                textbutton "Piano":
                    action [SetVariable("instrument_page", "piano"), Show("instrument_info_popup")]

                textbutton "Cello":
                    action [SetVariable("instrument_page", "cello"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()

screen instrument_info_popup():
    model True

    frame:
    xalign 0.5
    yalign 0.5
    padding (40, 40)

    vbox:
    spacing 20

    if instrument_page == "violin":