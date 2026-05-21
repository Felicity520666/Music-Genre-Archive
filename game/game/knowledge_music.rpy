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
                text "Extra Information: saxophone, trumpet, and double bass." size 36
                text "These are some core instruments in jazz, grouped into the genre's two main roles: the horn section (melody) and the rhythm section (foundation)." size 26
                textbutton "Saxophone":
                    action [SetVariable("instrument_page", "saxophone"), Show("instrument_info_popup")]

                textbutton "Trumpet":
                    action [SetVariable("instrument_page", "trumpet"), Show("instrument_info_popup")]

                textbutton "Double Bass":
                    action [SetVariable("instrument_page", "double_bass"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()
                    
            elif genre == "blues":
                text "Extra Information: guitar, harmonica, and piano." size 36
                text "Guitar, harmonica, and piano are the foundational instruments of the blues." size 26
                textbutton "Guitar":
                    action [SetVariable("instrument_page", "guitar"), Show("instrument_info_popup")]

                textbutton "Harmonica":
                    action [SetVariable("instrument_page", "harmonica"), Show("instrument_info_popup")]

                textbutton "Piano":
                    action [SetVariable("instrument_page", "piano"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()
                    
            elif genre =="country":
                text "Extra Information: guitar, banjo, and fiddle." size 36
                text "They are country music's literal DNA. Each one represents a different culture thread that came together in the American South to create the genre we know today." size 26
                textbutton "Guitar":
                    action [SetVariable("instrument_page", "guitar"), Show("instrument_info_popup")]

                textbutton "Banjo":
                    action [SetVariable("instrument_page", "banjo"), Show("instrument_info_popup")]

                textbutton "Fiddle":
                    action [SetVariable("instrument_page", "fiddle"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()
                    
            elif genre =="rock":
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