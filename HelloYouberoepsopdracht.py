import datetime

script = True
while True:
    print("Mijn naam is Nisa, ik ben 20 jaar oud en ik ga samen met mijn broertje vluchten uit Syrië.")
    print("Ons leven is heel moeilijk, er is veel oorlog in dit land en we kunnen nauwelijks geld verdiennen voor één week.")
    print("Ik heb aan mijn broer gevraagd of hij mee gaat en hij wil mee, omdat onze familie woont heel ver weg en hij wil niet alleen wonen in dit land.")
    print("Morgen avond, om 22:00 ga ik samen met m'n spullen en mijn broer van 17 Amir vluchten uit het land.")
    print("Ik kan nog maar één ding meenemen, zal ik de zaklamp meenenemen of de kaart?")
    inputText = input()
    if inputText == "kaart":
        print("Oké, ik neem de kaart mee. Nu dan wachten voor de nacht te vallen.")
        print("(5 uur later) Oké, de nacht is gevallen. Laten we opweg zijn, volg mij.")
        print("PAS OP!! Daar komt een truck aan met gewapende demonstranten, verstop je SNEL!")
        print("Grote rots of struik?")
        inputText = input()
        if inputText == "Grote rots":
            print("Je verstopt je achter de rots")
            print("De demonstranten rijden door zonder je te zien, nadat ze weg reden ging je door lopen met Nisa.")
            print("(2 uur later) Als ik het goed heb moeten we volgens de kaart naar het westen, daar staat een boot die ons naar Europa brengt.")
            print("Ze kwamen bij de boot aan en kregen de keuze om naar Spanje te gaan of Italië, welke deden ze?")
            inputText = input()
            if inputText == "Spanje":
                print("Ze namen de boot naar Spanje")
                print("Na een paar ruige dagen op de boot kwamen ze aan in Spanje, met een warme welkom kregen ze daar hulp.")
                print("In het asiel kregen ze eten en drinken, na een paar dagen kregen ze een baan aangeboden.")
                print("Accepteerden ze deze 2 banen aangeboden, ja of nee?")
                inputText = input()
                if inputText == "ja":
                    print("Nisa en Amir namen met plezier de baan aan. Ze gingen werken in de boerderij industrie op een boerderij.")
                    print("De familie bij wie ze woonden was heel aardig en lief. De familie had een opa, oma, vader, moeder en 3 zonen en 2 dochters.")
                    print("Nisa en Amir leefden lang en gelukkig op de boerderij ver weg van de oorlog.")
                    print("Ze leefden een goed leven en waren ontzettend blij.")
                    print("")
                    print("The Neutral Ending")
                elif inputText == "nee":
                    print("Ze bedankte voor het aanbod, maar ze willen naar Nederland gaan.")
                    print("Degene die hun hulp aanbood hielp Nisa en Amir een ticket te hebben om met de vliegtuig naar Nederland te gaan.")
                    print("Na 2 dagen vertrokken Nisa en Amir naar Nederland op een vliegtuig, een paar uur later kwamen ze aan in Nederland.")
                    print("Zodra ze zijn geland pakten ze hun spullen en gingen dan met de taxi of naar Amsterdam voor een baan of naar Haarlem voor een plek om te wonen?")
                    inputText = input()
                    if inputText == "Amsterdam":
                        print("Ze gingen met een taxi naar Amsterdam om te zoeken naar een baan.")
                        print("Toen ze aankwamen in Amsterdam, gingen ze kijken bij meerdere grote of kleine bedrijven of ze daar kunnen werken.")
                        print("Ze kregen een baan aangeboden bij een bakkerij waar ze geen opleiding voor nodig hadden, de aanbod staat altijd open.")
                        print("Nemen jullie de baan wel of niet aan?")
                        inputText = input()
                        if inputText == "Wel":
                            print("Ze namen met plezier en dankbaarheid de baan aan en omdat ze met z'n tweeën zijn mochten ze daar ook wonen, eten en slapen.")
                            print("Ze hadden blijkbaar ruimte over en ze vonden de extra gezelschap niet erg.")
                            print("Op de 1e dag ging het een beetje verkeerd(heel erg eigenlijk), maar op de 2e en 3e dag gingen het beter en de eigenaars zijn heel vriendelijk en aardig.")
                            print("De volledige familie die hier woont zijn de vader en moeder(de eigenaars) en hun 2 dochters, de dcohters zijn een tweeling en af en toe vervelend van tijd to tijd.")
                            print("Na 2 weken hier werken mochten we permanent blijven, we waren zo blij mijn zus en ik. We hadden een feestje gevierd die avond.")
                            print("Ze vonden het bakken leuk en de familie aardig en gezellig, ze konden voor geen betere toekomst wensen.")
                            print("")
                            print("The Baked Ending")
                        elif inputText == "Niet":
                            print("Ze vonden het aardig maar ze namen het niet aan; 'Het aanbod staat altijd open.' zeiden de eigenaars van de bakkerij.")
                            print("(5 uur later) Na een lange tijd zoeken zijn ze gewoon gaan slapen in een steegje en zoeken ze het wel de volgende ochtend uit.")
                            print("De volgende ochtend werden ze wakker gemaakt door een net persoon, ze mochten in zijn berdijf ontbijten en ze zeiden dat ze een baan zoeken.")
                            print("De meneer biedde hun de banen aan als obers in zijn bedrijf; 'Nemen jullie het aan, ja of nee.' zei de nette geklede meneer.")
                            inputText = input()
                            if inputText == "Ja":
                                print("Ja, we nemen jullie aangebode baan graag aan. We hebben toch geen zin meer om te zoeken.")
                                print("'Goed, jullie werken allebei als in obers in mijn restaurant. Jij werkt bij de restaurant van mij vrouw en jij bij mij.'zei de meneer.")
                                print("'Jullie mogen nu afscheid nemen, daarna gaan jullie gelijk aan het werk'zei de meneer. Na een hartverscheurende afscheid gaan jij en je zus op jullie eigen pad op weg.")
                                print("(15 jaar later) Na een lange tijd zie jij je zus weer in de flesh, jullie gaan samen uit eten en vertellen de avonturen die jullie gehad hebben de laatste 15 jaar.")
                                print("Nisa is een manager geworden door haar harde en goede werk en jij bent een kok geworden. Ze hadden allebei gehoord dat de meneer en zijn vrouw beide restaurants gaan samenvoegen in één grote restaurant.")
                                print("Nisa en Amir zijn allebei dolsblij sinds ze nu samen gaan werken in dezelfde restaurant, ze prooste op de feit dat ze samen gaan werken en binnenkort gaan samen wonen.")
                                print("Ze leefden nog lang en gelukkig.")
                                print("")
                                print("The Happy Ending")
                            elif inputText == "Nee":
                                print("Nee zeiden ze, ze werden na het ontbijt naar buiten gebracht en gingen ze zelf opweg.")
                                print("(5 dagen later) Op een nacht kwamen ze 2 rare figuren tegen, OPEENS uit het niets worden ze allebei in de buik gestoken door 1 van de figuren.")
                                print("Nadat ze allebei op de grond lagen te bloeden, werden hun spullen gestolen en lieten de figuren hun achter.")
                                print("Hun telefoons waren gepakt en er was niemand op straat die hun kon helpen. 1 uur en 23 minuten later zijn Nisa en Amir allebei doodgebloed.")
                                print("")
                                print("The Stab Ending")
                    elif inputText == "Haarlem":
                        print("Ze gingen met de taxi naar Haarlem opzoek naar een plek om te wonen en slapen.")
                        print("Toen ze daar aankwamen, vonden ze gelijk een vluchteling asiel.")
                        print("Ze kwamen daar binnen en vroegen of ze ergens een slaap plek konden vinden.")
                        print("Het asiel bood bij hun een slaap plek aan of bij een huis, welke kies je?")
                        inputText = input()
                        if inputText == "asiel":
                            print("Jullie wilden graag slapen bij het asiel, want daar voelen jullie je veilig.")
                            print("De volgende ochtend nadat jullie hebben ontbeten zijn jullie opzoek gegaan naar werk.")
                            print("Jullie konden allebei een krantenwijk doen waar jullie per week 16,50 euro konden verdiennen. Nisa en Amir namen de banen aan en ging hard werken.")
                            print("(5 1/2 jaar later) Nisa heeft nu een part-time job als business manager en Amir heeft een fulltime job als de eigenaar van een comic-book winkel.")
                            print("6 jaar nadat Nisa werkte als een business manager kwam ze in een auto ongeluk, ze kan haar benen nooit meer gebruiken.")
                            print("Nisa woont alleen thuis samen met haar man George die goed voor haar zorgt. Amir komt in het weekend telkens langs om te kijken hoe het gaat.")
                            print("Nisa en Amir hebben eindelijk een goed leven na zo'n lange tijd, en we hopen dat meerdere vluchtelingen hetzelfde kunnen hebben.")
                            print("")
                            print("The Live Long and Prosper Ending")
                        elif inputText == "huis":
                            print("Jullie wilden liever slapen in een huis, zodat je wat meer thuis voelt. Jullie kregen wat te eten en daarna gingen jullie naar bed en gingen jullie slapen.")
                            print("De volgende ochtend werden ze wakker gemaakt en kregen ze ontbijt. Kort na het ontbijt gingen ze naar een school om te leren en op school kregen ze ook een toets doen om te kijken hoe slim ze waren.")
                            print("Op het eind van de dag kreeg Nisa en Amir een opleiding aangeboden, Nisa kreeg Software developer aangeboden en Amir kreeg een opleiding Schilderen aangeboden.")
                            print("Nemen jullie de aangeboodde opleidingen wel of niet aan?")
                            inputText = input()
                            if inputText == "wel":
                                print("Na goed nadenken namen Nisa en Amir de opleidingen aan.")
                                print("(1 1/2 week later) Nisa en Amir startte met hun opleiding en ging hard aan het werk. Na de school dag gingen ze naar huis bij het asiel en daar aan hun huiswerk als ze dat hadden.")
                                print("(4 maanden later) Het gaat steeds beter met Nisa's en Amirs opleiding en hun zelf worden ook steeds beter. Ze werken elke dag hard en zorgen ervoor dat ze alle doelen behalen met de opdrachten die ze krijgen.")
                                print("(4 jaar later) Nisa en Amir's belangrijke week is er, de examen week. Als ze dit slagen kunnen ze gelijk ergens werken en een eigen leven beginnen.")
                                print("Een paar weken na het examen kregen ze de uitslag, ZE ZIJN ALLEBEI GESLAAGD!!!")
                                print("Nu kunnen ze ergens werken en geld verdienen. Nisa gaat werken bij Guerrilla Games, waar ze games maken. Amir is een schilder geworden en maakt prachtige schilderijen en heeft als bijbaantje werken in een supermark.")
                                print("")
                                print("The Succesfull Ending")
                            if inputText == "niet":
                                print("Na goed nadenken namen Nisa en Amir de beslissing om ze niet te nemen.")
                                print("Inplaats daarvan vroegen ze of ze bij het asiel konden werken, zodat ze meer vluchtelingen als hun zelf konden helpen.")
                                print("De asielwerker aan wie ze het vroegen ging het vragen aan haar baas, ze schreef het op en ging toen opweg om een andere vluchteling te helpen.")
                                print("(Een paar uur later) Nisa en Amir werden gevraagd of ze mee konden gaan naar de baas van het asiel, want daar werden ze een paar vragen gesteld.")
                                print("'Kunnen jullie koken?'vroeg de baas, Nisa zei 'Ik kan koken en mijn broertje kan goed bakken'. De baas zei 'Goed, Nisa jij gaat koken in de keuken voor het asiel en jij Amir gaat bakken op de 2e verdieping van dit gebouw. Jullie kunnen allebei in het huis blijven wonen en hier komen werken'.")
                                print("'We kunnen altijd de extra hulp gebruik met het helpen van vluchtelingen'zei de baas. Nisa en Amir bdeankte de baas en gingen opweg naar hun werk.")
                                print("Nisa en Amir hebben de laatste 45 jaar vluchtelingen geholpen, toen Nisa met pensioen ging stopte Amir met werken zodat hij voor haar kan zorgen. Ze hebben veel vluchtelingen geholpen en hopen dat het zo doorgaat.")
                                print("")
                                print("The Saviors Ending")
   
            elif inputText == "Italië":
                print("Ze namen de boot naar Italië.")
                print("Na een paar rustige dagen varen, kwamen ze aan in Italië. Helaas zijn ze daar niet welkom en werden ze gelijk uit het land gegooid.")
                print("Ze probeerden het land daarnaast en gelukkig laten ze daar wel vluchtelingen toe, het land waar ze in mochten was Frankrijk.")
                print("Vanaf Frankrijk konden ze of naar Engeland gaan of in Frankrijk blijven, welk land kiezen jullie?")
                inputText = input()
                if inputText == "Engeland":
                    print("Ze gingen naar het Noord-westen van Frankrijk en vanuit daar gingen ze naar Engeland.")
                    print("Ze kwamen aan in een haven en konden nog net optijd op de boot komen, kort daarna ging de boot opweg naar Engeland.")
                    print("Na 1 uur en 13 minuten varen kwam er een zeer zware storm en onweer. Doordat kon de boot niet goed zien waar ze vaarden en raakte een hele grootte rif, er ontstond een groot gat in het ruim.")
                    print("De boot zinkte snel en na 5 minuten zit al meer dan de helft van de boot onderwater, Nisa en Amir kunnen niet zwemmen dus proberen ze een bootje te vinden.")
                    print("Maar alle rubberen boten zijn los gegaan en op zee gevallen door de botsing of zitten al met mensen in het water.")
                    print("Helaas konden Nisa en Amir niet uit de boot zwemmen dus gingen ze samen met de boot naar de bodem van de zee en verdronken ze.")
                    print("")
                    print("The Sunken Ending")
                elif inputText == "Frankrijk":
                    print("Ze besloten om in Frankrijk te blijven, ze gingen hier opzoek naar werk en een nieuwe huis.")
                    print("Na een paar dagen stuitten ze op het lifeguard baan aanbieding, ze gingen naar de Headquarters van de lifeguards en vroegen of ze daar konden werken.")
                    print("Jullie mochten daar werken als jullie eerst jullie zelf bewijzen, zodat we weten dat jullie gemaakt zijn voor deze baan.")
                    print("Na een paar moeilijke tests zijn jullie geslaagd en konden jullie werken als lifeguards, na 2 maanden werken konden jullie een huis kopen vlakbij werk en de strand.")
                    print("Nisa en Amir werkte en woonde voor de rest van hun leven in Frankrijk, ze zijn gelukkig en blij dat ze de overtocht naar vrijheid hebben overleefd.")
                    print("Ze hopen dat elke vluchteling die er bestaat hetzelfde kan krijgen.")
                    print("")
                    print("The Croissant Ending")

        elif inputText == "Struik":
            print("Je verstopt je achter een struik.")
            print("De truck reed langzamer, je hoorde stemmen en voetstappen. De voetstappen werden luider en luider.")
            print("Uiteindelijk stopte de voetstappen, het was stil voor een momemt. TOEN pakte een demonstrant je en tilde je op en richte zijn wapen op jouw.")
            print("Nisa rende naar je toe en pakte je hand en trok je weg en jullie renden same weg.")
            print("De demonstrante schoten op jullie en raakte Nisa in de longen en knie en mijzelf in de been, schouder en pols.")
            print("Ze ontsnapten de demonstranten en gingen ergens zitten, ze probeerde het bloed te stoppen maar het lukt niet.")
            print("Nisa en Amir hielden elkaar vast en stierven in vrede...ze hadden geen spijt om te proberen te vluchten.")
            print("")
            print("The Bad Ending")

    elif inputText == "zaklamp":
        print("Oké, ik zal de zaklamp meenemen. Ik denk dat we nu dan moeten wachten voor de avond.")
        print("(5 uur later) Oké, de nacht is gevallen. Laten we opweg zijn, volg mij.")
        print("PAS OP!! Daar komt een truck aan met gewapende demonstranten, verstop je SNEL!")
        print("Grote rots of struik?")
        inputText = input()
        if inputText == "Grote rots":
            print("Je verstopt je achter de rots.")
            print("De demonstranten rijden verder zonder dat ze jullie zagen. Toen ze weg waren gingen Nisa en Amir verder opweg.")
            print("Ze wisten niet waar ze heen moetsen dus gingen ze opzoek naar een weg. Na een paar dagen lopen op een weg naaer een stad, zien ze opeens een auto in de verte.")
            print("De auto stopte voor hun en bracht hun ergens heen, na 2 uur rijden kwamen ze aan in een kwamp. Ze ontdekken het pas te laat als ze zien dat het een demonstranten kamp is, de demonstranten sturen hun terug naar hun huis met bewaking erbij.")
            print("Nisa en Amir hebben mislukt om te ontsnappen en nu worden ze ook 24/7 bewaakt door demonstranten.")
            print("...Ontsnappen is nu onmogelijk...")
            print("")
            print("The Failed Escape Ending")
        elif inputText == "struik":
            print("Je verstopt je achter een struik.")
            print("De truck reed langzamer, je hoorde stemmen en voetstappen. De voetstappen werden luider en luider.")
            print("Uiteindelijk stopte de voetstappen, het was stil voor een moment. OPEENS pakte een demonstrant je, tilde je op en richtte zijn wapen op jouw.")
            print("Nisa pakte de zaklamp en scheen op de ogen van de demonstranten, zodat ze niet konden zien en schieten waar ze zaten. Nisa pakte Amir en rende samen zo snel en ver mogelijk weg van de demonstranten.")
            print("Na een paar uur rennen en sne lopen, gingen ze uit rusten. Ze kwamen pas nadat ze stopte om te rusten uit dat hun water flessen leeg zijn.")
            print("Na een paar dagen lopen vielen ze allebei flauw, doordat ze geen water hebben kunnen drinken.")
            print("")
            print("wakker worden of slapen?")
            inputText = input()
            if inputText == "wakker worden":
                print("Je hoord geluiden en stemmen, je beslist om word wakker in een bed in een huis. Er ligt een glas water naast je bed.")
                print("Je pakt het op en drinkt het op in een snelle tijd.")
                print("Je stapt uit bed en je gaat naar de deur en opent het, zodra je buiten komt zie je een stad met een haven.")
                print("Na een tijdje zoeken vind je Nisa, na 5 minuten met elkaar praten pakken jullie je spallen en ga je naar de haven.")
                print("Bij de haven pakken jullie de boot, pakken jullie de boot naar Rusland of naar Griekenland?")
                inputText = input()
                if inputText == "Rusland":
                    print("Jullie nemen de boot naar Rusland.")
                    print("Binnen een week zijn jullie aangekomen in Rusland, vanaf daar zijn jullie opzoek gegaan naar werk.")
                    print("Na een paar dagen zoeken hebben jullie een baan gevonden in de samenleving. De baan betaalt jullie goed, nu gaan jullie opzoek naar een plek om te wonen.")
                    print("Jullie vinden een appartement die goedkoop is, jullie nemen de appartement omdat jullie hoorden dat er een sneeuwstorm eraan gaat komen.")
                    print("Op een dag terwijl jullie aan het werk waren, viel de stroom opeens uit. Jullie keken naar buiten en zag de grote voorspelde sneeuwstorm.")
                    print("De wind was sterk, zo sterk dat er een boom viel op het bedrijf waar Nisa en Amir werken. De ingang werd geblokkeerd door de boom.")
                    print("De gat die omgevallen boom heeft gemaakt zorge ervoor dat de kou binnenkwam, in een paar minuten bevroor alle apparatuur.")
                    print("Nisa en Amir omhelsden elkaar en hoopten dat ze het zouden overleven...")
                    print("")
                    print("De volgende ochten kwame de politie, de brandweer enambulance. Een paar mensen hebben het nog net overleeft in de nacht, maar helaas hebben veel mensen het niet overleefd.")
                    print("Mensen zoals Nisa en Amir.")
                    print("")
                    print("The Cold Ending")
                elif inputText == "Griekenland":
                    print("Jullie nemen de boot naar Griekenland.")
                    print("Na een paar dagen varen komen jullie aan in Griekenland, zodra jullie op land waren werden Nisa en Amir naar het asiel gebracht.")
                    print("Daar mochten jullie blijven totdat jullie terug kunnen naar jullie eigen land. Nisa en Amir accepteerden het gewoon, ze kregen een slaapplek, eten en drinken en kleding.")
                    print("15 jaar later")
                    print("Nisa en Amir keren terug naar hun land, toen ze bij hun oude huis kwamen kregen ze tranen in hun ogen. Na zo'n lange tijd zijn ze eindelijk weer thuis.")
                    print("")
                    print("The True Ending")
            elif inputText == "slapen":
                print("Je hoort geluiden en stemmen, maar je bent te moe om wakker te worden.")
                print("Dus je beslist om te blijven slapen.")
                print("Een paar uur later word je wakker, stap je uit bed en ga je opzoek naar Nisa.")
                print("Na een halfuur zoeken heb je haar gevonden, jullie omhelsen elkaar, daarna bedanken jullie de verzorgers, pakken jullie je spullen en gaan opzoek naar transportatie.")
                print("Jullie vinden een vliegtuig en een auto, welke nemen jullie?")
                inputText = input()
                if inputText == "vliegtuig":
                    print("Jullie beslissen de vliegtuig te nemen naar Amerika.")
                    print("Jullie stappen in de vliegtuig en gaan naar Amerika, na 13 uur gaan jullie landen totdat OPEENS de linker motoren uitvallen en in brand vliegen van de linker vleugel.")
                    print("De piloten gingen een noodlanding maken, maar dat werd moeilijk door de harde en sterke wind.")
                    print("De vliegtuig lande met veel moeite, maar kan moeilijk stoppen en gaat rechtstreeks op een hangar af waar meerdere vliegtuigen staan.")
                    print("De vliegtuig crasht in de andere vliegtuigen en explodeert, waardoor Nisa en Amir helaas overlijden.")
                    print("")
                    print("The Malfunction Ending")
                elif inputText == "auto":
                    print("Jullie beslissen de auto te nemen naar Oostenrijk.")
                    print("Na een lange tijd rijden jullie door de gebergte heen, de benzine van de auto was bijna leeg. 'Kijk, daar is een huisje'zei Amir. Nisa reed nu richting een houten huis.")
                    print("Jullie komen aan in het huisje en vinden dat niemand er woont, jullie besluiten om hier maar te wonen sind er blijkbaar toch niemand woont.")
                    print("Terwijl Nisa terug ging naar de stad voor eten, drinken en benzine. Maakte Amir het huis schoon en maakte alles picobello.")
                    print("In de avond gingen jullie pizza eten, terwijl jullie pizza aten proosten jullie op de feit dat jullie een huis hebben en een kleine, goedbetaalde baan in de supermarkt.")
                    print("Nisa en Amir bleven voor de rest van hun leven in Oostenrijk wonen.")
                    print("")
                    print("The 'Cabin In The Woods' Ending")

    print("Do you want to repeat?")
    inputText = input()
    print("input:", inputText)
    if inputText == "no":
        break