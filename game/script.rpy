# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default popup_page = "menu"
define f = Character("[povname]", color = "#e10072")
define m = Character("[povname]", color = "#66ff00") 
define s = Character("Serenity", color = "#ff5400")
default mc_gender = "girl"
transform smallleft:
    zoom 0.35
    xalign 0.0
    yalign 1.0

transform smallright:
    zoom 0.7
    xalign 1.6
    yalign 1.0

# The game starts here.

label start:
    play music "the_mountain-happy-happy-upbeat-496594.mp3" fadein 1.0
    scene s with fade
    show lucas normal at smallleft
    with dissolve
    show felisha glad at smallright
    with dissolve

    "Hello there! Before the game starts, please choose your character!"
    menu:
        "I'm a boy":
            $ mc_gender = "boy"
            $ persistent.player_gender = "boy"
            $ renpy.save_persistent()
        "I'm a girl":
            $ mc_gender = "girl"
            $ persistent.player_gender = "girl"
            $ renpy.save_persistent()

    $ mc = m if mc_gender == "boy" else f
    "And what do you want to be called?"
    $ povname = renpy.input("Enter your name here!", length = 32)
    $ povname = povname.strip()
    if not povname:
        $ povname = "Player"
    stop music fadeout 1.5
    
    scene inside with fade
    play sound "magic-03-278824.mp3"
    play music "sweet-acoustic-guitar-music-311691.mp3" fadein 3.0
    if mc_gender == "boy":
        show lucas pleasant at smallleft
        with dissolve
    else:
        show felisha confident at smallright
        with dissolve
    mc "Yeah, lucky me! I got into the school band!"
    if mc_gender == "boy":
        show lucas normal at smallleft
        with dissolve
    else:
        show felisha glad at smallright
        with dissolve
    mc "I bet I'll have so much fun learning and playing music there!"
    if mc_gender == "boy":
        show lucas embarrassed at smallleft
        with dissolve
    else:
        show felisha believe at smallright
        with dissolve
    mc "Um, the only problem is, everyone else in the band already knows a lot about music, and I'm the only beginner there..."
    if mc_gender == "boy":
        show lucas pleasant at smallleft
        with dissolve
    else:
        show felisha yes at smallright
        with dissolve
    mc "Oh! I know what I'll do! My friend Serenity is pretty experienced. I'll ask her to help me out!"
    if mc_gender == "boy":
        show lucas normal at smallleft
        with dissolve
    else:
        show felisha glad at smallright
        with dissolve
    mc "Hmmm, now, I think Serenity is working in the pet shop. I'll go there to find her!"


        
    stop music fadeout 1.0
    play sound "store-entrance-bell-188054.mp3"
    scene sphynx with fade
    play music "meow-meow-give-me-milk-version-1-317260.mp3" fadein 1.5
    show normal at smallright
    with moveinright
    play sound "hello-278029.mp3" volume 2.5
    s "Hello!"
    s "Oh! [povname]! What are you doing here?"
    menu:
        "I'm here to ask for your help with music!":
            jump teach
        "Oh of course I'm here to buy a pet!":
            s "What...? That's pretty sudden..."
            mc "Lol okay seriously, I need your help with music!"
            jump teach
        
    label teach:
        show smile at smallright
        with dissolve
        s "Sure! I heard you joined the school band, good job!"
        s "I personally think the most important thing for you to know right now is the different genres of music."
        mc "Um... why are they so important to know?"
        show normal at smallright with dissolve
        s "Well, it expands your musical vocabulary, so you can better understand what the teacher is saying."
        s "It also boosts technical skills and deepens your appreciation for diverse cultures and historical contexts."
        s "In a nutshell, it helps you better understand what's going on in music."
        s "So here we go!"
        stop music fadeout 1.5
        play sound "magic-03-278824.mp3"
    scene cl with fade
    play music "classical.mp3" fadein 2.0
    show normal at smallright
    with moveinleft
    s "First up, we have {b}classical{/b} music! It is a genre that encompasses a wide range of styles and compositions."
    s "It is primarily instrumental from the {i}Baroque{/i}, {i}Classical{/i}, and {i}Romantic{/i} periods."
   
    menu:
        "Do you want to learn more about the {i}Baroque{/i}, {i}Classical{/i}, and {i}Romantic{/i} periods?"
        "Learn more":
            $ popup_page = "menu"
            call screen knowledge_periods
        "Pass":
            pass

    s "Classical music is known for its structured forms, such as {i}Symphonies{/i}, {i}Concertos{/i}, and {i}Sonatas{/i}."
    menu:
        "Do you want to learn more about {i}Symphony{/i}, {i}Concerto{/i}, and {i}Sonata{/i}?"
        "Learn more":
            $ popup_page = "menu"
            call screen structure_info
        "Pass":
            pass
    hide normal with dissolve
    show vpc with dissolve
    s "Some instruments commonly used include the violin, piano, and cello."
    menu: 
        "Do you want to learn more about the instruments?"
        "Learn more":
            call screen music_genre_popup("classical")
        "Pass":
            pass
    hide vpc with dissolve
    show mbb with dissolve
    s "Lastly, famous composers like {i}Mozart{/i}, {i}Beethoven{/i}, and {i}Bach{/i} have left a significant impact on music history with their complex compositions and innovations."
    hide mbb with dissolve
    stop music fadeout 1.0
    scene jz with fade
    play music "jazz.mp3" fadein 1.5
    show smile at smallright
    s "And now, my favorite genre, {b}jazz{/b}!"
    show normal at smallright
    with dissolve
    s "Jazz is a pretty energetic and improvisational genre of music that originated in the African-American communities of New Orleans in the late 19th and early 20th centuries."
    hide normal
    show smile at smallright
    with dissolve
    s "It blends elements from {i}Blues{/i}, {i}Ragtime{/i}, and {i}European music{/i}."
    hide smile with dissolve
    show sax with dissolve
    s "Instruments like the saxophone, trumpet, and double bass are pivotal, alongside the piano and drums."
    menu: 
        "Do you want to learn more about the instruments?"
        "Learn more":
            call screen music_genre_popup("jazz")
        "Pass":
            pass
    scene mus with pushright
    s "Legendary artists such as Louis Armstrong, Duke Ellington, and Miles Davis have contributed to the genre's evolution with their innovative styles and techniques."
    s "Jazz is so cool that it instantly became my favorite genre! And after talking about my favorite two genres..."
    stop music fadeout 1.0
label choices:
    play music "kontraa-no-sleep-hiphop-music-473847.mp3" fadein 1.5
    scene s with irisin
    show smile at smallright
    s "[povname], which genre would you like to learn next?"
    $ genre_choice = renpy.call_screen("genre_scroll_menu")

    if genre_choice == "blues":
        jump blues
    elif genre_choice == "country":
        jump country
    elif genre_choice == "rock":
        jump rock
    elif genre_choice == "soul":
        jump soul
    elif genre_choice == "funk":
        jump funk
    elif genre_choice == "reggae":
        jump reggae
    elif genre_choice == "disco":
        jump disco
    elif genre_choice == "hiphop":
        jump hiphop
    elif genre_choice == "electronic":
        jump electronic
    elif genre_choice == "grunge":
        jump grunge
    elif genre_choice == "pop":
        jump pop
    elif genre_choice == "metal":
        jump metal
    elif genre_choice == "pr":
        jump pr
    elif genre_choice == "indie":
        jump indie
    elif genre_choice == "edm":
        jump edm
    elif genre_choice == "kpop":
        jump kpop
    elif genre_choice == "trap": 
        jump trap
    elif genre_choice == "lofi": 
        jump lofi
    else:
        return

    label blues:
        scene bb with wipeleft
        play music "blues.mp3" fadein 1.5
        show smile at smallright
        with moveinright
        s "The {b}blues{/b} genre is rooted in African-American history and expresses themes of sorrow, struggle, and soulful resilience."
        hide smile 
        show normal at smallright
        with dissolve
        s "Originating in the Deep South of the United States, it laid the foundation for modern rock and jazz."
        hide normal with dissolve
        show bl with vpunch
        s "The genre often features the guitar, harmonica, and piano."
        menu: 
            "Do you want to learn more about the instruments?"
            "Learn more":
                call screen music_genre_popup("blues")
            "Pass":
                pass
        scene bm with blinds
        s "Artists like B.B. King, Muddy Waters, and Etta James are known for expressive vocals and instrumental skills that capture the essence of the Blues experience."
        stop music fadeout 1.0
        jump choices
    label country:
        scene cb with fade
        play music "country.mp3" fadein 1.5
        show hap at smallright
        with moveinright
        s "{b}Country{/b}, with its roots in American folk and western music, tells stories of love, hardship, and life in rural America."
        hide hap with dissolve
        show yo with hpunch
        s "It often includes instruments like the guitar, banjo, and fiddle!"
        menu: 
            "Do you want to learn more about the instruments?"
            "Learn more":
                call screen music_genre_popup("country")
            "Pass":
                pass
        scene cmus with pushleft
        s "Artists such as Johnny Cash, Dolly Parton, and Garth Brooks have shaped the genre, making it popular across the United States and beyond with their storytelling and distinctive twangs."
        stop music fadeout 1.0
        jump choices
    label rock:
        scene rnr with hpunch
        play music "rock.mp3"
        show hap at smallright
        with moveinleft
        s "Ohhoho! Emerging in the 1950s, {b}Rock and Roll{/b} is characterized by... guess what?"
        hide hap with dissolve
        show roll with vpunch
        s "Its upbeat tempo and use of electric guitars, drums, and bass!"
        menu: 
            "Do you want to learn more about the instruments?"
            "Learn more":
                call screen music_genre_popup("rock")
            "Pass":
                pass
        hide roll with hpunch
        show smile at smallright
        with moveinleft
        s "It was a revolutionary sound that influences cultural movements!"
        hide smile with moveoutright
        show icons with hpunch
        s "Icons like Elvis Presley, Chuck Berry, and the Beatles were pivotal in popularizing the genre, blending elements of {i}Blues{/i}, {i}Jazz{/i}, and {i}Country Music{/i}."
        stop music fadeout 1.0
        jump choices
    label soul:
        scene rab with squares
        play music "rb.mp3" fadein 1.0
        show normal at smallright
        with moveinright
        s "{b}Soul{/b} music emerged in African-American communities, combining elements of {i}Gospel{/i}, {i}Blues{/i}, and {i}Jazz{/i}!"
        hide normal
        show smile at smallright
        with dissolve
        s "It's known for emotional vocals, smooth rhythms, and instruments like the saxophone, drums, and keyboard."
        menu: 
            "Do you want to learn more about the instruments?"
            "Learn more":
                call screen music_genre_popup("soul")
            "Pass":
                pass
        hide smile with moveoutright
        scene b with blinds
        s "Artists such as Aretha Franklin, Ray Charles, and Stevie Wonder have been instrumental in defining the soulful sound and emotional depth of the genre."
        stop music fadeout 1.0
        jump choices

    label funk:
        scene fk with vpunch
        play music "funk.mp3" fadein 0.5
        show hap at smallright
        with moveinleft
        s "Now, [povname], {i}Funk{/i} is a rhythm-driven musical genre that originated in the mid-1960s when African-American musicians blended {i}Soul{/i}, {i}Jazz{/i}, and {i}R&B{/i} into a danceable new form!"
        hide hap 
        show smile at smallright
        with dissolve
        s "It is characterized by a strong bassline, electric guitars, and drums."
    menu: 
        "Do you want to learn more about the instruments?"
        "Learn more":
            call screen music_genre_popup("funk")
        "Pass":
            pass
    s "Funk emphasizes groove and rhythm."
    hide smile with moveoutright
    scene pp with zoomin
    s "James Brown, George Clinton, and the band Parliament-Funkadelic are among the key figures that brought Funk to the forefront with their energetic performances and rhythmic innovations."
    stop music fadeout 1.0
    jump choices

    label reggae:
        scene jam with zoomin
        play music "jamaice.mp3" fadein 1.0
        show normal at smallright with moveinright
        s "Originating in Jamaica in the late 1960s, {b}Reggae{/b} is distinguished by its laid-back rhythm, offbeat accents, and association with Rastafarian culture!"
        hide normal with moveoutright
        show reg with squares
        s "Instruments like the guitar, bass, drums, and keyboard are staples in creating its distinctive sound."
    menu: 
        "Do you want to learn more about the instruments?"
        "Learn more":
            call screen music_genre_popup("reggae")
        "Pass":
            pass
    scene bob with pushleft
    s "Bob Marley, Peter Tosh, and Bunny Wailer are iconic in spreading reggae's messages of love, unity, and social justice worldwide!"
    stop music fadeout 1.0
    jump choices
    
    label disco:
        scene do with blinds
        play music "disco.mp3" fadein 0.5
        show hap at smallright with moveinright
        s "{b}Disco{/b}, peaking in the late 1970s, is known for its upbeat dance music!"
        s "It is characterized by a steady four-on-the-floor beat, synthesized basslines, and string sections."
        hide hap 
        show smile at smallright
        with dissolve
        s "Nightclubs were the heart of the disco scene, with artists like Donna Summer, the Bee Gees, and Chic producing hits that defined the era's exuberant nightlife and dance culture!"
        stop music fadeout 1.0
        jump choices
    label hiphop:
        scene hhh with wiperight
        play music "hpop.mp3"
        show normal at smallright with moveinright
        s "Here we go! {b}Hip Hop{/b} is definitely more than music!"
        hide normal
        show smile at smallright with dissolve
        s "It's a cultural movement that includes rapping, DJing, graffiti art, and dance, originating in the 1970s in New York City!"
        s "It features rhythmic speech or rapping over beats and tracks."
        hide smile with moveoutright
        scene artist with pushright
        s "Artists like Tupac Shakur, The Notorious B.I.G., and Jay-Z have been influential in expressing social and political issues through their lyrics."
        stop music fadeout 1.0
        jump choices
    label electronic:
        scene ee with vpunch
        play music "the_mountain-electronic-electronic-music-490598.mp3"
        show hap at smallright with moveinright
        s "{b}Electronic{/b}!!! This genre encompasses a broad range of percussive electronic music genres."
        hide hap
        show smile at smallright with dissolve
        s "It's primarily made for nightclubs, raves, and festivals."
        s "It includes subgenres like {i}HOUSE{/i}, {i}TECHNO{/i}, and {i}TRANCE{/i}!"
        hide smile with moveoutleft
        scene ar with blinds
        s "It uses synthesizers, drum machines, and digital audio workstations."
    menu: 
        "Do you want to learn more about the instruments?"
        "Learn more":
            call screen music_genre_popup("electronic")
        "Pass":
            pass
    scene elec with slideup
    s "Artists like Daft Punk, Calvin Harris, and Tiesto have been pioneers, creating music that energizes dance floors worldwide!"
    stop music fadeout 1.0
    jump choices
    
    label grunge:
        scene gr with slidedown
        play music "nightcast-grunge-diner-176898.mp3"
        show hap at smallright
        with moveinright
        s "{b}Grunge{/b} music, emerging in the late 1980s in Seattle, combines elements of Punk, Rock, and Heavy Metal!"
        hide hap
        scene ins with vpunch
        s "With raw, distorted guitar sounds and introspective lyrics, bands like Nirvana, Pearl Jam, and Soundgarden are known for their influential role in popularizing grunge, which later became the soundtrack for Generation X's disillusionment."
        stop music fadeout 1.0
        jump choices
    label pop:
        scene poppp with wipeleft
        play music "paulyudin-pop-dance-electric-swing-song-475324.mp3" fadein 1.0
        show smile at smallright with moveinright
        s "{b}Pop{/b} music is a broad genre that includes catchy, widely appealing songs often focused on romantic love, but it can also address many other themes!"
        s "It utilizes simple, memorable melodies and hooks, plus synthesizers and production techniques to enhance its appeal."
        hide smile with moveoutright
        scene ts with pushleft
        s "Artists like Madonna, Michael Jackson, and Taylor Swift have dominated the charts with their pop hits, influencing countless other artists!"
        stop music fadeout 1.0
        jump choices
    label metal:
        scene mt with vpunch
        play music "alexgrohl-metal-dark-matter-111451.mp3" 
        show hap at smallright with moveinright
        s "{b}Metal{/b} music is known for powerful amplified guitar sounds, complex compositions, and themes ranging from personal strife to fantasy and political issues."
        hide hap
        show normal with dissolve
        s "It includes subgenres like Heavy Metal, Death Metal, and Black Metal, each with its own distinct characteristics and dedicated fanbase."
    menu:
        "Do you want to learn more about the subgenres?"
        "Learn more":
            $ popup_page = "menu"
            call screen metal_subgenres
        "Pass":
            pass
    hide normal with moveoutright
    scene mr with hpunch 
    s "Bands like Metallica, Iron Maiden, and Black Sabbath have been pivotal in shaping the genre's aggressive sound and theatricality!"
    stop music fadeout 1.0
    jump choices

    label pr:
        scene bjk with hpunch
        play music "alexgrohl-punk-rock-478794.mp3"
        show hap at smallright with moveinleft
        s "{b}Punk Rock{/b} emerged as a reaction against the perceived excesses of mainstream rock music."
        s "It promotes a DIY ethic with fast, hard-edged music."
        hide hap
        show normal at smallright with dissolve
        s "It often features political or anti-establishment lyrics."
        hide normal with moveoutright
        scene ram with hpunch
        s "Bands like the Ramones, Sex Pistols, and The Clash are seminal figures in the punk movement, embodying its energy and independent spirit!"
        stop music fadeout 1.0
        jump choices
    label indie:
        scene ind with squares
        play music "nastelbom-indie-rock-513422.mp3"
        show smile at smallright with moveinright
        s "{b}Indie{/b} music is short for independent music, which is known for its diverse sound and rejection of mainstream music norms."
        hide smile
        show hap at smallright with dissolve
        s "It encompasses a wide range of music that is produced independently from major commercial record labels."
        hide hap with moveoutright
        scene sar with pushright
        s "Artists like The Smiths, Arcade Fire, and Arctic Monkeys are known for their innovative approaches to music and distinctive soundscapes!"
        stop music fadeout 1.0
        jump choices
    label edm:
        scene mmm with blinds
        play music "diogodasilvasimoes-forever-edm-trance-vibes-489439.mp3"
        show smile at smallright with moveinright
        s "{b}EDM{/b} is a set of percussive electronic music genres produced primarily for dance-based environments such as nightclubs and festivals."
        s "It emphasizes rhythm, bass, and the use of synthesizers and drum machines."
        hide smile with moveoutright
        scene nota with pushright
        s "Notable EDM artists include Avicii, Skrillex, and Deadmau5, who have been instrumental in bringing electronic music to a global audience."
        stop music fadeout 1.0
        jump choices
    label kpop:
        scene hello with squares
        play music "robloxsonges-x-kpop-demon-hunters-452914.mp3"
        show smile at smallright with moveinright
        s "{b}K-Pop{/b} is a music genre originating from South Korea, characterized by a wide variety of audiovisual elements."
        s "It includes a mix of Western sounds and African influences with Korean musical roots."
        hide smile with moveoutright
        scene bts with pushright
        s "Groups like BTS, BLACKPINK, and EXO are at the forefront, known for vibrant music, synchronized dance routines, and dedicated global fanbases."
        stop music fadeout 1.0
        jump choices
    label trap:
        scene traa with pushright
        play music "bombinsound-trap-512482.mp3" fadein 0.5
        show hap at smallright with moveinright
        s "Ladies and gentlemen, next up, we have {b}Trap{/b} music!!!"
        hide hap with moveoutright
        scene us with dissolve
        s "It originated in the early 2000s in the Southern United States."
        scene th with dissolve
        s "You know what, trap music is a subgenre of hip-hop!"
        scene iiiss with dissolve
        s "It is characterized by its lyrical content and sound, which includes 808 kick drums, hi-hats, and synthesized melodies."
        scene goes with dissolve
        s "Artists like T.I., Gucci Mane, and Migos have contributed to the genre's popularity, which often explores themes of street life and struggle."
        stop music fadeout 1.0
        jump choices
    label lofi:
        scene lowlow with wipeleft
        play music "mondamusic-lofi-lofi-girl-lofi-chill-512853.mp3" fadein 1.0
        show smile at smallright with moveinleft
        s "I don't know about you, but I personally listen to {b}Lo-fi{/b} a lot when I want to relax or focus on something."
        s "By looking at this popular Lo-fi Girl image and listening to the song, does it feel familiar to you? I bet you've listened to lo-fi music before, right?"
    menu:
        "I sure have ☕🎧🎶":
            s "Lol, that's what I thought!"
            jump continue
        "No, but I'll check it out 🌆📼☁️":
            s "Yeah! It's super chill and worth checking out!"
            jump continue
    label continue:
        hide smile
        show normal at smallright with dissolve
        s "Lo-fi music is short for low-fidelity music."
        s "It is a genre that embraces imperfections, often featuring mellow beats, a mix of analog warmth, and slight recording imperfections."
        hide normal with moveoutright
        scene capy with dissolve
        s "It's become popular for studying, relaxing, or creating a cozy atmosphere."
        scene pro
        s "Artists and producers like Nujabes, J Dilla, and ChilledCow, known for lo-fi hip-hop streams, have been pivotal in popularizing this genre's calming and atmospheric soundscapes."
        menu:
            "Do you want to learn more about these artists and producers?"
            "Learn more":
                $ popup_page = "menu"
                call screen lofi_artists
            "Pass":
                pass
        stop music fadeout 1.0
        jump choices

        screen knowledge_periods():
            modal True
            frame:
                xalign 0.5
                yalign 0.5
                padding (40, 40)
                vbox:
                    spacing 20
                    if popup_page == "menu":

                        text "Extra Information: Baroque, Classical, and Romantic Periods" size 36
                        text "In Western music history, the {b}Baroque{/b}, {b}Classical{/b}, and {b}Romantic{/b} periods are the three major musical eras. Each period has its own style, sound, and famous composers." size 26
                        textbutton "Baroque Period":
                            action SetVariable("popup_page", "baroque")

                        textbutton "Classical period":
                            action SetVariable("popup_page", "classical")

                        textbutton "Romantic period":
                            action SetVariable("popup_page", "romantic")
                    
                        textbutton "Close":
                            action Return()
                    
                    elif popup_page == "baroque":
                        text "{b}Baroque Period{/b} —— About 1600-1750" size 32
                        text "Baroque music is often fancy, dramatic, and complex. It uses many decorative notes and strong rhythms. Some famous composers are Bach, Handel, and Vivaldi." size 24
                        textbutton "Back":
                            action SetVariable("popup_page", "menu")

                        textbutton "Close":
                            action Return()
                    elif popup_page == "classical":
                        text "{b}Classical Period{/b} —— About 1750-1820" size 36
                        text "Classical music is usually clear, balances, and elegant. The melodies are easier to follow, and the structure is organized. Some famous composers are Mozard, Haydn, and Beethoven." size 24
                        textbutton "Back":
                            action SetVariable("popup_page", "menu")
                        textbutton "Close":
                            action Return()
                    
                    elif popup_page =="romantic":
                        text "{b}Romantic Period{/b} —— About 1820-1910" size 36
                        text "Romantic music focuses on strong emotions, imagination, and drama. It can sound powerful, dreamy, sad, or passionate. Some famous composers are Chopin, Tchaikovsky, and Liszt." size 24
                        textbutton "Back":
                            action SetVariable("popup_page", "menu")
                        textbutton "Close":
                            action Return()
        screen structure_info():
            modal True
            frame:
                xalign 0.5
                yalign 0.5
                padding (40, 40)
                vbox:
                    spacing 20
                    if popup_page == "menu":

                        text "Extra Information: Symphony, Concerto, and Sonata" size 36
                        text "These are three important structured forms in Classical music, primarily distinguished by who is playing and how many parts they have." size 26
                        textbutton "Symphony":
                            action SetVariable("popup_page", "symphony")

                        textbutton "Concerto":
                            action SetVariable("popup_page", "concerto")

                        textbutton "Sonata":
                            action SetVariable("popup_page", "sonata")

                        textbutton "Close":
                            action Return()
                    
                    elif popup_page == "symphony":
                        text "{b}Symphony{/b} —— whole orchestra" size 32
                        text "A symphony is a large piece of music for a full orchestra. It usually has several sections called movements." size 24
                        textbutton "Back":
                            action SetVariable("popup_page", "menu")

                        textbutton "Close":
                            action Return()
                    elif popup_page == "concerto":
                        text "{b}Concerto{/b} —— solo instrument with orchestra" size 36
                        text "A concerto is usually written for one solo instrument and an orchestra. For example, a piano concerto has a pianist playing the main part, while the orchestra plays the accompanying parts." size 24
                        textbutton "Back":
                            action SetVariable("popup_page", "menu")
                        textbutton "Close":
                            action Return()
                    
                    elif popup_page =="sonata":
                        text "{b}Sonata{/b} —— one or few instruments" size 36
                        text "A sonata is usually written for one or a small group of instruments. For example, a piano sonata may be played by only one pianist." size 24
                        textbutton "Back":
                            action SetVariable("popup_page", "menu")
                        textbutton "Close":
                            action Return()
        screen metal_subgenres():
            modal True
            frame:
                xalign 0.5
                yalign 0.5
                padding (40, 40)
                vbox:
                    spacing 20
                    if popup_page == "menu":

                        text "Extra Information: Heavy Metal, Death Metal, and Black Metal" size 32
                        text "These are the three important subgenres of Metal music, which all use loud electric guitars, strong drums, and intense energy, but they create different feelings." size 26
                        textbutton "Heavy Metal":
                            action SetVariable("popup_page", "heavy")

                        textbutton "Death Metal":
                            action SetVariable("popup_page", "death")

                        textbutton "Black Metal":
                            action SetVariable("popup_page", "black")

                        textbutton "Close":
                            action Return()
                    
                    elif popup_page == "heavy":
                        text "{b}Heavy Metal{/b} —— classic, powerful, and dramatic" size 32
                        text "Heavy Metal is the classic and original style of metal music. It usually has loud electric guitars, strong drums, powerful vocals, and dramatic energy. It can sound intense, heroic, or rebellious." size 24
                        textbutton "Back":
                            action SetVariable("popup_page", "menu")

                        textbutton "Close":
                            action Return()
                    elif popup_page == "death":
                        text "{b}Death Metal{/b} —— heavier, faster, and brutal" size 32
                        text "Death Metal is usually heavier, faster, and more aggressive than classic Heavy Metal. It often uses very low growling vocals, fast drums, complex guitar riffs, and dark themes." size 24
                        textbutton "Back":
                            action SetVariable("popup_page", "menu")
                        textbutton "Close":
                            action Return()
                    
                    elif popup_page =="black":
                        text "{b}Black Metal{/b} —— drak, cold, and mysterious" size 32
                        text "Black Metal often sounds cold, raw, dark, and atmosphric. It may use high screaming vocals, fast \"blast beat\" drums, tremolo-picked guitars, and mysterious or anti-mainstream themes." size 24
                        textbutton "Back":
                            action SetVariable("popup_page", "menu")
                        textbutton "Close":
                            action Return()
        screen lofi_artists():
            modal True
            frame:
                xalign 0.5
                yalign 0.5
                padding (40, 40)
                vbox:
                    spacing 20
                    if popup_page == "menu":

                        text "Extra Information: Nujabes, J Dilla, and ChilledCow" size 32
                        text "They are legendary, highly influential hip-hop prpducers widely considered the forefathers of the lo-fi hip-hop genre." size 24
                        textbutton "Nujabes":
                            action SetVariable("popup_page", "nujabes")

                        textbutton "J Dilla":
                            action SetVariable("popup_page", "dilla")

                        textbutton "ChilledCow":
                            action SetVariable("popup_page", "chilled")
                        
                        textbutton "Close":
                            action Return()

                    elif popup_page == "nujabes":
                        text "{b}Nujabes{/b} —— The Godfather of Lo-Fi Hip-Hop" size 32
                        text "Nujabes was a Japanese music producer best known for his atmospheric instrumental mixes sampling from hip-hop, soul, and jazz, as well as incorporating elements of trip hop, break beat, downtempo, and ambient music. Unfortunately, he died in a traffic collision at the age of 36 in 2010. Although relatively niche during his lifetime, he has since achieved posthumous acclaim and been referred as the godfather of lo-fi hip hop." size 24
                        textbutton "Back":
                            action SetVariable("popup_page", "menu")
                        textbutton "Close":
                            action Return()
                    elif popup_page == "dilla":
                        text "{b}J Dilla{/b} —— The Godfather of Modern Beatmaking" size 32
                        text "J Dilla was an American record producer, rapper, and composer. He emerged from the mid-1990s underground hip-hop scene in Detroit, Michigan, as a member of the group Slum Village. He was a founding member of the Soulquarians, a musical collective active during the late 1990s and early 2000s. He died at the age of 32 from a combination of TTP and lupus. Despite a short mainstream career, he is widely considered to be one of the most influential producers in hip-hop and popular music." size 24
                        textbutton "Back":
                            action SetVariable("popup_page", "menu")
                        textbutton "Close":
                            action Return()
                    elif popup_page == "chilled":
                        text "{b}ChilledCow{/b} —— The Lofi Girl" size 32
                        text "Lofi Girl, formerly known as ChilledCow until 2021, is a French YouTube channel and music label established in 2017. It provides livestreams of lo-fi hip hop music 24/7, accompanied by a Japanese-style animation of a girl, officially named Jade, studying or relaxing in her bedroom with a cat on the window. The channel offers several videos and livestreams of lo-fi music in hip hop style. The best known video is a live stream of lo-fi music that has run for several years." size 24
                        textbutton "Back":
                            action SetVariable("popup_page", "menu")
                        textbutton "Close":
                            action Return()





    return

