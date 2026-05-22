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
                text "Extra Information: electric guitars, drums, and bass." size 36
                text "Electric guitars, drums, and bass form the foundational blueprint of rock music. Together, they create the Rhythm Section." size 26
                textbutton "Electric Guitar":
                    action [SetVariable("instrument_page", "electric_guitar"), Show("instrument_info_popup")]

                textbutton "Drums":
                    action [SetVariable("instrument_page", "drums"), Show("instrument_info_popup")]

                textbutton "Bass":
                    action [SetVariable("instrument_page", "bass"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()
                        
            elif genre =="soul":
                text "Extra Information: saxophone, drums, and keyboard." size 36
                text "They represent the three pillars of the genre: the saxophone brings vocal-like emotional expression, the drums establish the driving groove and backbeat, and the keyboard delivers the rich, gospel-rooted harmonies." size 26
                textbutton "Saxophone":
                    action [SetVariable("instrument_page", "saxophone"), Show("instrument_info_popup")]

                textbutton "Drums":
                    action [SetVariable("instrument_page", "drums"), Show("instrument_info_popup")]

                textbutton "Keyboard":
                    action [SetVariable("instrument_page", "keyboard"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()
                  
            elif genre =="funk":
                text "Extra Information: bassline, electric guitars, and drums." size 36
                text "In funk, the bassline, electric guitars, and drums act as interlocking parts of a single, rhythmic machine." size 26
                textbutton "Bassline":
                    action [SetVariable("instrument_page", "bassline"), Show("instrument_info_popup")]

                textbutton "Electric Guitar":
                    action [SetVariable("instrument_page", "electric_guitar"), Show("instrument_info_popup")]

                textbutton "Drums":
                    action [SetVariable("instrument_page", "drums"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()

            elif genre =="reggae":
                text "Extra Information: guitar, bass, drums, and keyboard." size 36
                text "Those instruments create the signature syncopated, bouncing groove of the genre, with the bass and drums functioning as the absolute heartbeat while the guitar and keyboard provide harmonic and rhymic texture." size 26
                textbutton "Guitar":
                    action [SetVariable("instrument_page", "guitar"), Show("instrument_info_popup")]

                textbutton "Bass":
                    action [SetVariable("instrument_page", "bass"), Show("instrument_info_popup")]

                textbutton "Drums":
                    action [SetVariable("instrument_page", "drums"), Show("instrument_info_popup")]

                textbutton "Keyboard":
                    action [SetVariable("instrument_page", "keyboard"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()

            elif genre =="electronic":
                text "Extra Information: synthesizers, drum machines, and digital audio workstations." size 36
                text "Those three instruments are the foundational building blocks of electronic music." size 26
                textbutton "Synthesizers":
                    action [SetVariable("instrument_page", "synthesizers"), Show("instrument_info_popup")]

                textbutton "Drum Machines":
                    action [SetVariable("instrument_page", "drum_machines"), Show("instrument_info_popup")]

                textbutton "Digital Audio Workstations":
                    action [SetVariable("instrument_page", "digital_audio_workstations"), Show("instrument_info_popup")]

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