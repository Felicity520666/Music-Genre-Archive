# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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
        s "I personally think the most important thing for you to know right now is the different music genres."
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
    s "Classical music is known for its structured forms, such as {i}Symphonies{/i}, {i}Concertos{/i}, and {i}Sonatas{/i}."
    hide normal with dissolve
    show vpc with dissolve
    s "Some instruments commonly used include the violin, piano, and cello."
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
    scene mus with pushright
    s "Legendary artists such as Louis Armstrong, Duke Ellington, and Miles Davis have contributed to the genre's evolution with their innovative styles and techniques."
    s "Jazz is so cool that it instantly became my favorite genre! And after talking about my favorite two genres..."
label choices:
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
        scene bm with blinds
        s "Artists like B.B. King, Muddy Waters, and Etta James are known for expressive vocals and instrumental skills that capture the essence of the Blues experience."
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
        scene cmus with pushleft
        s "Artists such as Johnny Cash, Dolly Parton, and Garth Brooks have shaped the genre, making it popular across the United States and beyond with their storytelling and distinctive twangs."
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
        hide roll with hpunch
        show smile at smallright
        with moveinleft
        s "It was a revolutionary sound that influences cultural movements!"
        hide smile with moveoutright
        show icons with hpunch
        s "Icons like Elvis Presley, Chuck Berry, and the Beatles were pivotal in popularizing the genre, blending elements of {i}Blues{/i}, {i}Jazz{/i}, and {i}Country Music{/i}."
        jump choices
    label soul:
        scene rab with squares
        play music "rb.mp3" fadein 1.0
        show normal at smallright
        with moveinright
        s "The {b}Soul{/b} music emerged in the African-American Community, combining elements of {i}Gospel{/i}, {i}Blues{/i}, and {i}Jazz{/i}!"
        show smile at smallright
        with dissolve
        s "It's known for emotional vocals, smooth rhythms, and instruments like the saxophone, drums, and keyboard."
        hide smile with moveoutright
        scene b with blinds
        s "Artists such as Aretha Franklin, Ray Charles, and Stevie Wonder have been instrumental in defining the soulful sound and emotional depth of the genre."
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
        s "Funk is characterized by a strong bassline, electric guitars, and drums."
        s "It emphasizes groove and rhythm."
        hide smile with moveoutright
        scene pp with zoomin
        s "James Brown, George Clinton, and the band Parliament-Funkadelic are among the key figures that brought Funk to the forefront with their energetic performances and rhythmic innovations."
        jump choices

    label reggae:
        scene jam with zoomin
        play music "jamaice.mp3" fadein 1.0
        show normal at smallright with moveinright
        s "Originating in Jamaica in the late 1960s, {b}Reggae{/b} is distinguished by its laid-back rhythm, offbeat accents, and association with Rastafarian culture!"
        hide normal with moveoutright
        show reg with squares
        s "Instruments like the guitar, bass, drums, and keyboard are staples in creating its distinctive sound."
        scene bob with pushleft
        s "Bob Marley, Peter Tosh, and Bunny Wailer are iconic in spreading reggae's messages of love, unity, and social justice worldwide!"
        jump choices
    label disco:
        scene do with blinds
        play music "disco.mp3" fadein 0.5
        show hap at smallright with moveinright
        s "{b}Disco{/b}, peaking in the late 1970s, is known for its upbeat dance music!"
        s "It is characterized by a steady four-on-the-floor beat, synthesized baselines, and string sections."
        hide hap 
        show smile at smallright
        with dissolve
        s "Nightclubs were the heart of the disco scene, with artists like Donna Summer, the Bee Gees, and Chic producing hits that defined the era's exuberant nightlife and dance culture!"
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
        scene elec with slideup
        s "Artists like Daft Punk, Calvin Harris, and Tiesto have been pioneers, creating music that energizes dance floors worldwide!"
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
        jump choices
    label pop:
        scene poppp with wipeleft
        play music "paulyudin-pop-dance-electric-swing-song-475324.mp3" fadein 1.0
        show smile at smallright with moveinright
        s "{b}Pop{/b} music is a broad genre that includes catchy, widely appealing songs often focused on romantic love, but it can also address many other themes!"
        s "It utilizes simple memorable melodies and hooks, synthesizers and production techniques to enhance its appeal."
        hide smile with moveoutright
        scene ts with pushleft
        s "Artists like Madonna, Michael Jackson, and Taylor Swift have dominated the charts with their pop hits, influencing countless other artists!"
        jump choices
    label metal:
        scene mt with vpunch
        play music "alexgrohl-metal-dark-matter-111451.mp3" 
        show hap at smallright with moveinright
        s "{b}Metal{/b} music is known for powerful amplified guitar sounds, complex compositions, and themes ranging from personal strife to fantasy and political issues."
        hide hap
        show normal with dissolve
        s "It includes subgenres like Heavy Metal, Death Metal, and Black Metal, each with its own distinct characteristics and dedicated fanbase."
        hide normal with moveoutright
        scene mr with hpunch 
        s "Bands like Metallica, Iron Maiden, and Black Sabbath have been pivotal in shaping the genre's aggressive sound and theatricality!"
        jump choices
    label pr:
        scene bjk with hpunch
        play music "alexgrohl-punk-rock-478794.mp3"
        show hap at smallright with moveinleft
        s "{b}Punk Rock{/b} emerged as a reaction against the perceived excesses of mainstream rock music."
        s "It promotes a DIY ethic with fast hard-edged music."
        hide hap
        show normal at smallright with dissolve
        s "It often features political or anti-establishment lyrics."
        hide normal with moveoutright
        scene ram with hpunch
        s "Bands like the Ramones, Sex Pistols, and The Clash are seminal figures in the punk movement, embodying its energy and independent spirit!"
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
    return

