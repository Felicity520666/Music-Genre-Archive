default instrument_page = None
default selected_music_genre = None

screen music_genre_popup(genre):
    modal True

    on "show" action SetVariable("selected_music_genre", genre)

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
                    action [SetVariable("instrument_page", "violin"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Piano":
                    action [SetVariable("instrument_page", "piano"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Cello":
                    action [SetVariable("instrument_page", "cello"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()

            elif genre == "jazz":
                text "Extra Information: saxophone, trumpet, and double bass." size 36
                text "These are some core instruments in jazz, grouped into the genre's two main roles: the horn section (melody) and the rhythm section (foundation)." size 26
                textbutton "Saxophone":
                    action [SetVariable("instrument_page", "saxophone"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Trumpet":
                    action [SetVariable("instrument_page", "trumpet"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Double Bass":
                    action [SetVariable("instrument_page", "double_bass"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()

            elif genre == "blues":
                text "Extra Information: guitar, harmonica, and piano." size 36
                text "Guitar, harmonica, and piano are the foundational instruments of the blues." size 26
                textbutton "Guitar":
                    action [SetVariable("instrument_page", "guitar"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Harmonica":
                    action [SetVariable("instrument_page", "harmonica"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Piano":
                    action [SetVariable("instrument_page", "piano"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()

            elif genre =="country":
                text "Extra Information: guitar, banjo, and fiddle." size 36
                text "They are country music's literal DNA. Each one represents a different culture thread that came together in the American South to create the genre we know today." size 26
                textbutton "Guitar":
                    action [SetVariable("instrument_page", "guitar"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Banjo":
                    action [SetVariable("instrument_page", "banjo"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Fiddle":
                    action [SetVariable("instrument_page", "fiddle"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()

            elif genre =="rock":
                text "Extra Information: electric guitars, drums, and bass." size 36
                text "Electric guitars, drums, and bass form the foundational blueprint of rock music. Together, they create the Rhythm Section." size 26
                textbutton "Electric Guitar":
                    action [SetVariable("instrument_page", "electric_guitar"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Drums":
                    action [SetVariable("instrument_page", "drums"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Bass":
                    action [SetVariable("instrument_page", "bass"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()

            elif genre =="soul":
                text "Extra Information: saxophone, drums, and keyboard." size 36
                text "They represent the three pillars of the genre: the saxophone brings vocal-like emotional expression, the drums establish the driving groove and backbeat, and the keyboard delivers the rich, gospel-rooted harmonies." size 26
                textbutton "Saxophone":
                    action [SetVariable("instrument_page", "saxophone"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Drums":
                    action [SetVariable("instrument_page", "drums"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Keyboard":
                    action [SetVariable("instrument_page", "keyboard"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()

            elif genre =="funk":
                text "Extra Information: bassline, electric guitars, and drums." size 36
                text "In funk, the bassline, electric guitars, and drums act as interlocking parts of a single, rhythmic machine." size 26
                textbutton "Bassline":
                    action [SetVariable("instrument_page", "bassline"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Electric Guitar":
                    action [SetVariable("instrument_page", "electric_guitar"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Drums":
                    action [SetVariable("instrument_page", "drums"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()

            elif genre =="reggae":
                text "Extra Information: guitar, bass, drums, and keyboard." size 36
                text "Those instruments create the signature syncopated, bouncing groove of the genre, with the bass and drums functioning as the absolute heartbeat while the guitar and keyboard provide harmonic and rhymic texture." size 26
                textbutton "Guitar":
                    action [SetVariable("instrument_page", "guitar"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Bass":
                    action [SetVariable("instrument_page", "bass"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Drums":
                    action [SetVariable("instrument_page", "drums"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Keyboard":
                    action [SetVariable("instrument_page", "keyboard"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()

            elif genre =="electronic":
                text "Extra Information: synthesizers, drum machines, and digital audio workstations." size 36
                text "Those three instruments are the foundational building blocks of electronic music." size 26
                textbutton "Synthesizers":
                    action [SetVariable("instrument_page", "synthesizers"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Drum Machines":
                    action [SetVariable("instrument_page", "drum_machines"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Digital Audio Workstations":
                    action [SetVariable("instrument_page", "digital_audio_workstations"), Hide("music_genre_popup"), Show("instrument_info_popup")]

                textbutton "Close":
                    action Return()

screen instrument_info_popup():
    modal True


    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)

        vbox:
            spacing 20

            if instrument_page == "violin":
                text "{b}Violin{/b} —— The Queen of Instruments" size 32
                text "A violin, sometimes referred to as a fiddle, is a wooden chordophone, and is the smallest, and thus hightest-pitched instrument in regular use in the violin family. Violins are important instruments in a wide variety of musical genres. They are most prominent in the Western classical tradition, both in ensembles and as solo instruments. Violins are also important in many varieties of folk music, including country music, bluegrass music, and in jazz." size 24
            elif instrument_page == "piano":
                text "{b}Piano{/b} —— The King of Instruments" size 32
                text "A piano is a keyboard instrument that produces sound when its keys are pressed, activating an action mechanism where hammers strike strings. Most modern pianos have a row of 88 black and white keys. Two main types of pianos are the grand piano and the upright piano. The grand piano offers better sound and more precise key control while the upright piano is more commonly used because of its smaller size and lower cost." size 24
            elif instrument_page == "cello":
                text "{b}Cello{/b} —— The Human Voice of the Strings" size 32
                text "The violoncello, commonly abbreviated as cello, is a medium-low pitched bowed string instrument of the violin family. This instrument enjoys a large solo repertoire with and without accompaniment, as well as numerous concerti. As a solo instrument, the cello uses its whole range, from bass to soprano, and in chamber music, such as string quartets and the orchestra;s string section, it often plays the bass part, where it may be reinforced an octave lower by the double basses." size 24
            elif instrument_page == "saxophone":
                text "{b}Saxophone{/b} —— The Voice of Jazz" size 32
                text "The saxophone, often referred to colloquially as the sax, is a type of single-reed woodwind instrument with a connical body, usually made of brass. The saxophone is used in a wide range of musical styles, including classical music, military bands, marching bands, jazz, and contemporary music. The saxophone os also used as a solo and melody instrument or as a member of a horn section in some styles of rock and roll and popular music." size 24
            elif instrument_page == "trumpet":
                text "{b}Trumpet{/b} —— The Royal Instrument" size 32
                text "The trumpet is a brass instrument. The most common type of trumpet is a transposing instrument in B♭, with pitches sounding a whole step lower than written. Trumpets are used in art music styles, appearing in orchestras, concert bands, chamber music groups, and jazz ensembles. They are also common in popular music and are generally included in school bands. Since the late 15th century, trumpets have primarily been constructed of brass tubing, usually bent twice into a rounded rectangular shape." size 24
            elif instrument_page == "double_bass":
                text "{b}Double Bass{/b} —— The Bass Fiddle" size 32
                text "The double bass, also known as the upright bass, the acoustic bass, the bull fiddle, the bass fiddle, the string bass, the contrabass, or simplt the bass, is the largest and lowest-pitched chordophone in the modern symphony orchestra. It has four or five strings, and its constructions is in between that of the gamba and the violin family. The bass is a standard member of the orchestra's string section, along with violins, violas, and cellos, as well as the concert band, and is featured in concertos, solo, and chamber music in Western classical music. The bass is used in a range of other genres, like jazz, blues, rock and roll, rockabilly, country music, bluegrass, tango, folk music, and certain types of film and vedio game soundtracks." size 24
            elif instrument_page == "guitar":
                text "{b}Guitar{/b} —— The Axe" size 32
                text "The guitar is a stringed musical instrument that is usually fretted and typically has six or twelve strings. It's usually held flat against the player's body and played by strumming or plucking the strings with the dominant hand, while simultaneously pressing selected strings against frets with the fingers of the opposite hand. The three main types of modern guitar are the classical guitar, the steel-string acoustic guitar or electric guitar, and the Hawaiian guitar. The guitar is classified as a chordophone, meaning the sound is produced by a vibrating string stretched between two fixed points." size 24
            elif instrument_page == "harmonica":
                text "{b}Harmonica{/b} —— The Mouth Organ" size 32
                text "The harmonica, also know as a French harp, is a free reed wind instrument used worldwide in many musical genres, notably in blues, American folk music, classical music, jazz, country, and rock. The many types of harmonica include diatonic, chromatic, tremolo, octave, orchestral, and bass versions. The harmonica is played by using the lips and tongue to direct air inro or out of one or more holes along a mouthpiece. The basic parts of the harmonica are the combs, reed plates, and cover plates. The harmonica was developed in Europe in the early part of the 19th century. Playing the harmonica requires inhaling and exhaling strongly against resistance. This action helps develop a strong diaphragm and deep breathing using the entire lung volume." size 24
            elif instrument_page == "banjo":
                text "{b}Banjo{/b} —— The Bucka-Bucka" size 32
                text "The banjo is a stringed instrument with a thin membrane stretched over a frame or cavity to form a resonator. The membrane is typically circular, and in modern forms is usually made of BOPET, whereearly emebranes were made of goat skin. Early forms of the instrument were fashioned by African Americans and had AFrican antecedents, and the instrument was strongly associated with black people. By the early 20th century, the banjo was most frequently associated with folk, cowboy music, and country music. HIstorically, the banjo occupied a central place in Black American traditional music and rural folk culture before entering the mainstream via the minstrel shows of the 19th century." size 24
            elif instrument_page == "fiddle":
                text "{b}Fiddle{/b} —— The Devil's Box" size 32
                text "The fiddle is a bowed string musical instrument, most often a violin or a bass. Fiddle is a colloquial term for the violin, used by players in all genres, including classical msuic. Although in many cases violin and fiddle are essentially synonymous, the style of the music played may determine specific construction differences between fiddles and classical violins. Among musical styles, fiddling tends to produce rhythms that focus on dancing, with associated quick note changes, whereas classical music tends to contain more vibrato and sustained notes. Fiddling is also open to improvisation and embellishment with ornamentation at the player's discretion, in contrast to orchestral performances, which adhere to the composer's notes to reproduce a work faithfully." size 24
            elif instrument_page == "electric_guitar":
                text "{b}Electric Guitar{/b} —— The Voice of a Generation" size 32
                text "An electric guitar is a guitar that requires external electric sound  amplification to be heard at typical performance volumes. Invented in 1932, the electric guitar was adopted bu jazz guitar players, who wanted to play single-note guitar solos in large big bands ensembles. During the 1950s and 1960s, teh electric guitar became the most important instrument in popular music. It has evolved into an instrument that is capable of a multitude of sounds and styles in genres ranging from pop and rock to folk to country music, blues and jazz. It served as a major component in the development of teh electric blues and many other genres of music. The three main types of electric guitar are the solid-body, semi-hollow, and hollow-body." size 24
            elif instrument_page == "drums":
                text "{b}Drums{/b} —— The Heartbeat of Music" size 32
                text "A drum is a member of the percussion droup of musical instruments. Drums consist of at least one membrane, called a drumhead or drum skin, that is stretched over a shell and struck, either directly with the player's hands, or with a percussion mallet, to produce sound. Drums are usually played by striking with the hand, a beater attached to a pedal, or with one or two sticks with or without padding. A wide variety of sticks are used, including wooden sticks and sticks with soft beaters of felt on the end. In jazz, some drummers use brushes for a smoother, quieter sound. In popular music and jazz, \"drums\" usually refers to a drum kit or a set of drums, with some cymbals, or in the case of harder rock music genres, many cymbals." size 24
            elif instrument_page == "bass":
                text "{b}Bass{/b} —— The Low End" size 32
                text "The bass guitar, also known as the electric bass, is the lowest-pitched member of teh guitar family. It is similar in appearance and construction to an electric guitar but with a longer neck and scale length. Teh electric bass guitar most commonly had four strings, thought five-, six-, and seven-stringed models are also built. Because the electric bass guitar is a quiet instrument acousitically, it requires external amplification, generally via electromagnetic or piezo-electric pickups. It can be used with direct input boxes, audio interfaces, mixing consoles, computers, or bass-effects processors which offer headphone jacks." size 24
            elif instrument_page == "keyboard":
                text "{b}Keyboard{/b} —— The Orchestra in a Box" size 32
                text "It's a musical instrument played using a keyboard, a row of levers that are pressed by the fingures. Keyboards typically work by translating the physical act of pressing keys into electrical signals that produce sound. UNder the fingures of a sensitive performer, the keyboard may also be used to control dynamics, phrasing, shading, articulation, and other elements of expression, depending on the design and inherent capabilities of the instrument. Modern keyboards, especially digital ones, can simulate a wode range of sounds betond traditional piano tones, thanks to advanced sound stnthesis techniques and digital sampling." size 24
            elif instrument_page == "bassline":
                text "{b}Bassline{/b} —— The Pulse" size 32
                text "Bassline is the term used in many styles of music, such as blues, jazz, funk, dub, and electronic, traditional, and classical music, for the low-pitched instrumental part or line played by a rhythm section instrument such as the electric bass, double bass, cello, tuba or keyboard. In unaccompanied solo performance, bassline may simply be played in the lower register of any instrumen while melody and further accompanimeny os provided in the middle or upper register. In solo music for piano and pipe organ, these instruments have an excellent lower register that can be used to play a deep bassline." size 24
            elif instrument_page == "synthesizers":
                text "{b}Synthesizers{/b} —— The Sound Lab" size 32
                text "A synthesizer is an electronic musical instrument that generates audio sugnals. Synthesizers typically create sounds by generating waveforms through methods including subtractive synthesis, additive synthesis, ad frequency modulation synthesis. These sounds may be altered by components such as filters, which cut or boost frequencies; envelopes, which control articulation, or how notes begin and end; and low-frequency oscillators, which modulate parametres such as pitch, volume, or filter characteristics affetcing timbre. Synthesizers are typically played with keyboards or controlled by sequencers, software or other instruments, and can be synchronized to other equipment via MIDI." size 24
            elif instrument_page == "drum_machines":
                text "{b}Drum Machines{/b} —— The Infinite Groove" size 32
                text "A drum machine is an electronic musical instrument that creates percussion sounds, drum beats, and patterns. Drum machines may imitate drum kits or other percussion instruments, or produce unique sounds, such as synthesized electrinic tones. A drum machine often has pre-programmed beats and patterns for popular genres and styles, auch as pop music, rock music, and dance music. Drum machines have had a lasting ompact on popular music in the 20th century. The Roland TR-808, introduced in 1980, significantly influced the development of dance music, especially elevtronic dance music and hip hop, and has been widely used in popular music since then." size 24
            elif instrument_page == "digital_audio_workstations":
                text "{b}Digital Audio Workstations{/b} —— The Studio in a Laptop" size 32
                text "A DAW is an electronic device or application software used for recording, editing and producing audio files. DAWs come in a wide variety of configurations, from a single software program on a laptop, to an integrated stand-alone unit, all the way to a highly complex configuration of numerous components controlled by a central computer. Traditionally, a computer-based DAW has four basic components: a computer, a sound card or other audio interface, and at least one user input device for adding and modifying data." size 24

            textbutton "Back":
                action [Hide("instrument_info_popup"), Show("music_genre_popup", genre=selected_music_genre)]

            textbutton "Close":
                action [Hide("instrument_info_popup"), Hide("music_genre_popup"), Return()]
