import datetime

script = True
while True:
    print("Mijn naam is Nisa, ik ben 20 jaar oud en ik ga vluchten uit Syrië")
    print("Morgen avond, om 22:00 ga ik samen met m'n spullen en mijn broer van 17 Amir vluchten uit het land")
    print("Ik kan nog maar één ding meenemen, zal ik de zaklamp meenenemen of de kaart?")
    inputText = input()
    if inputText == "kaart":
        print("Oké, ik neem de kaart mee. Nu dan wachten voor de nacht te vallen")
        print("(5 uur later) Oké, de nacht is gevallen. Laten we opweg zijn, volg mij.")
        print("PAS OP!! Daar komt een truck aan met gewapende demonstranten, verstop je SNEL!")
        print("Grote rots of struik?")
        inputText = input()
        if inputText == "Grote rots":
            print("Je verstopt je achter de rots")
            print("De demonstranten rijden door zonder je te zien, nadat ze weg reden ging je door lopen met Nisa")
            print("(2 uur later) Als ik het goed heb moeten we volgens de kaart naar het westen, daar staat een boot die ons naar Europa brengt")
            print("Ze kwamen bij de boot aan en kregen de keuze om naar Spanje te gaan of Italië, welke deden ze?")
            inputText = input()
            if inputText == "Spanje":
                print("Ze namen de boot naar Spanje")
                print("Na een paar ruige dagen op de boot kwamen ze aan in Spanje, met een warme welkom kregen ze daar hulp")
                print("In het asiel kregen ze eten en drinken, na een paar dagen kregen ze een baan aangeboden.")
                print("Accepteerden ze deze 2 banen aangeboden, ja of nee?")
                inputText = input()
                if inputText == "ja":
                    print("Nisa en Amir namen met plezier de baan aan. Ze gingen werken in de boerderij industrie op een boerderij")
                    print("De familie bij wie ze woonden was heel aardig en lief. De familie had een opa, oma, vader, moeder en 3 zonen en 2 dochters")
                    print("Nisa en Amir leefden lang en gelukkig op de boerderij ver weg van de oorlog")
                    print("Ze leefden een goed leven en waren ontzettend blij")
                    print("The Neutral Ending")
                elif inputText == "nee":
                    print("Ze bedankte voor het aanbod, maar ze willen naar Nederland gaan")
                    print("Degene die hun hulp aanbood hielp Nisa en Amir een ticket te hebben om met de vliegtuig naar Nederland te gaan")
                    print("Na 2 dagen vertrokken Nisa en Amir naar Nederland op een vliegtuig, een paar uur later kwamen ze aan in Nederland")
                    print("Zodra ze zijn geland pakten ze hun spullen en gingen dan met de taxi of naar Amsterdam voor een baan of naar Haarlem voor een plek om te wonen?")
                    inputText = input()
                    if inputText == "Amsterdam":
                        print("Ze gingen met een taxi naar Amsterdam om te zoeken naar een baan")
                        print("Toen ze aankwamen in Amsterdam, gingen ze kijken bij meerdere grote of kleine bedrijven of ze daar kunnen werken")
                        print("Ze kregen een baan aangeboden bij een bakkerij waar ze geen opleiding voor nodig hadden, de aanbod staat altijd open")
                        print("Nemen jullie de baan wel of niet aan?")
                        inputText = input()
                        if inputText == "Wel":
                            print("Ze namen met plezier en dankbaarheid de baan aan en omdat ze met z'n tweeën zijn mochten ze daar ook wonen, eten en slapen")
                            print("Ze hadden blijkbaar ruimte over en ze vonden de extra gezelschap niet erg")
                            print("Op de 1e dag ging het een beetje verkeerd(heel erg eigenlijk), maar op de 2e en 3e dag gingen het beter en de eigenaars zijn heel vriendelijk en aardig")
                            print("De volledige familie die hier woont zijn de vader en moeder(de eigenaars) en hun 2 dochters, de dcohters zijn een tweeling en af en toe vervelend van tijd to tijd")
                            print("Na 2 weken hier werken mochten we permanent blijven, we waren zo blij mijn zus en ik. We hadden een feestje gevierd die avond")
                            print("")
                            print("Ze vonden het bakken leuk en de familie aardig en gezellig, ze konden voor geen betere toekomst wensen")
                            print("The Baked Ending")
                        elif inputText == "Niet":
                            print("Ze vonden het aardig maar ze namen het niet aan; 'Het aanbod staat altijd open.' zeiden de eigenaars van de bakkerij")
                            print("(5 uur later) Na een lange tijd zoeken zijn ze gewoon gaan slapen in een steegje en zoeken ze het wel de volgende ochtend uit")
                            print("De volgende ochtend werden ze wakker gemaakt door een net persoon, ze mochten in zijn berdijf ontbijten en ze zeiden dat ze een baan zoeken")
                            print("De meneer biedde hun de banen aan als obers in zijn bedrijf; 'Nemen jullie het aan, ja of nee.' zei de nette geklede meneer")
                            inputText = input()
                            if inputText == "Ja":
                                print("Ja, we nemen jullie aangebode baan graag aan. We hebben toch geen zin meer om te zoeken")
                                print("'Goed, jullie werken allebei als in obers in mijn restaurant. Jij werkt bij de restaurant van mij vrouw en jij bij mij.'zei de meneer")
                                print("'Jullie mogen nu afscheid nemen, daarna gaan jullie gelijk aan het werk'zei de meneer. Na een hartverscheurende afscheid gaan jij en je zus op jullie eigen pad op weg")
                                print("(15 jaar later) Na een lange tijd zie jij je zus weer in de flesh, jullie gaan samen uit eten en vertellen de avonturen die jullie gehad hebben de laatste 15 jaar")
                                print("Nisa is een manager geworden door haar harde en goede werk en jij bent een kok geworden. Ze hadden allebei gehoord dat de meneer en zijn vrouw beide restaurants gaan samenvoegen in één grote restaurant")
                                print("Nisa en Amir zijn allebei dolsblij sinds ze nu samen gaan werken in dezelfde restaurant, ze prooste op de feit dat ze samen gaan werken en binnenkort gaan samen wonen")
                                print("")
                                print("Ze leefden nog lang en gelukkig")
                                print("The Happy Ending")
                            elif inputText == "Nee":
                                print("Nee zeiden ze, ze werden na het ontbijt naar buiten gebracht en gingen ze zelf opweg")
                                print("Op een nacht kwamen ze 2 rare figuren tegen, kort daarna werden ze allebei in de buik gestoken door 1 van de figuren")
                                print("Nadat ze allebei op de grond lagen te bloeden, werden hun spullen gestolen en lieten de figuren hun achter")
                                print("Hun telefoons waren gepakt en er was niemand op straat die hun kon helpen. 1 uur en 23 minuten later zijn Nisa en Amir allebei doodgebloed")
                                print("The Stab Ending")
                    elif inputText == "Haarlem":
                        print("Ze gingen met de taxi naar Haarlem opzoek naar een plek om te wonen en slapen")
                        print("Toen ze daar aankwamen, vonden ze gelijk een vluchteling asiel")
                        print("Ze kwamen daar binnen en vroegen of ze ergens een slaap plek konden vinden")
                        print("Het asiel bood bij hun een slaap plek aan of bij een huis, welke kies je?")
                        inputText = input()
                        if inputText == "asiel":
                            print("Jullie wilden graag slapen bij het asiel, want daar voelen jullie je veilig")
                            print("De volgende ochtend nadat jullie hebben ontbeten zijn jullie opzoek gegaan naar werk")
                            print("Jullie konden allebei een krantenwijk doen waar jullie per week 16,50 euro konden verdiennen. Nisa en Amir namen de banen aan en ging hard werken")
                            print("(5 1/2 jaar later) Nisa heeft nu een part-time job als business manager en Amir heeft een fulltime job als de eigenaar van een comic-book winkel")
                            print("6 jaar nadat Nisa werkte als een business manager kwam ze in een auto ongeluk, ze kan haar benen nooit meer gebruiken")
                            print("Nisa woont alleen thuis samen met haar man George die goed voor haar zorgt. Amir komt in het weekend telkens langs om te kijken hoe het gaat")
                            print("Nisa en Amir hebben eindelijk een goed leven na zo'n lange tijd, en we hopen dat meerdere vluchtelingen hetzelfde kunnen hebben")
                            print("The Live Long and Prosper Ending")
                        elif inputText == "huis":
                            print("Jullie wilden liever slapen in een huis, zodat je wat meer thuis voelt")
   
            elif inputText == "Italië":
                print("Ze namen de boot naar Italië")
                print("Na een paar rustige dagen varen, kwamen ze aan in Italië. Helaas zijn ze daar niet welkom en werden ze gelijk uit het land gegooid")
                print("Ze probeerden het land daarnaast en gelukkig laten ze daar wel vluchtelingen toe, het land waar ze in mochten was Frankrijk")
                print("Vanaf Frankrijk konden ze of naar Engeland gaan of in Frankrijk blijven, welk land kiezen jullie?")
                inputText = input()
                if inputText == "Engeland":
                    print("Ze gingen naar het Noord-westen van Frankrijk en vanuit daar gingen ze naar Engeland")
                elif inputText == "Frankrijk":
                    print("Ze besloten om in Frankrijk te blijven, ze gingen hier opzoek naar werk en een nieuwe huis")

        elif inputText == "Struik":
            print("Je verstopt je achter een struik")
            print("De truck reed langzamer, je hoorde stemmen en voetstappen. De voetstappen werden luider en luider")
            print("Uiteindelijk stopte de voetstappen, het was stil voor een momemt. TOEN pakte een demonstrant je en tilde je op en richte zijn wapen op jouw")
            print("Nisa rende naar je toe en pakte je hand en trok je weg en jullie renden same weg")
            print("De demonstrante schote op jullie en raakte Nisa in de longen en knie en mijzelf in de been, schouder en pols")
            print("Ze ontsnapten de demonstranten en gingen ergens zitten, ze probeerde het bloed te stoppen maar het lukt niet")
            print("Nisa en Amir hielden elkaar vast en stierven in vrede...ze hadden geen spijt om te proberen te vluchten")
            print("The Bad Ending")

    elif inputText == "zaklamp":
        print("Oké, ik zal de zaklamp meenemen. Ik denk dat we nu dan moeten wachten voor de avond")
        print("(5 uur later) Oké, de nacht is gevallen. Laten we opweg zijn, volg mij.")
        print("PAS OP!! Daar komt een truck aan met gewapende demonstranten, verstop je SNEL!")
        print("Grote rots of struik?")
        inputText = input()
        if inputText == "Grote rots":
            print("Je verstopt je achter de rots")
        elif inputText == "Struik":
            print("Je verstopt je achter een struik")
    
    
    print("Do you want to repeat?")
    inputText = input()
    print("input:", inputText)
    if inputText == "no":
        break