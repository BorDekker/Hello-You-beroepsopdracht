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
                    print("The End")
                elif inputText == "nee":
                    print("Ze bedankte voor het aanbod, maar ze wouden naar Nederland gaan")
                    print("Degene die hun hulp aanbood hielp Nisa en Amir een ticket te hebben om met de vliegtuig naar Nederland te gaan")
                    print("Na 2 dagen vertrokken Nisa en Amir naar Nederland op een vliegtuig, een paar uur later kwamen ze aan in Nederland")
                    
   
            elif inputText == "Italië":
                print("Ze namen de boot naar Italië")

        elif inputText == "Struik":
            print("Je verstopt je achter een struik")
            print("De truck reed langzamer, je hoorde stemmen en voetstappen. De voetstappen werden luider en luider")
            print("Uiteindelijk stopte de voetstappen, het was stil voor een momemt. TOEN pakte een demonstrant je en tilde je op en richte zijn wapen op jouw")
            print("Nisa rende naar je toe en pakte je hand en trok je weg en jullie renden same weg")
            print("De demonstrante schote op jullie en raakte Nisa in de longen en knie en mijzelf in de been, schouder en pols")
            print("Ze ontsnapten de demonstranten en gingen ergens zitten, ze probeerde het bloed te stoppen maar het lukt niet")
            print("Nisa en Amir hielden elkaar vast en stierven in vrede...ze hadden geen spijt om te proberen te vluchten")
            print("The End")

    elif inputText == "zaklamp":
        print("Oké, ik zal de zaklamp meenemen. Ik denk dat we nu dan moeten wachten voor de avond")
        print("(5 uur later) Oké, de nacht is gevallen. Laten we opweg zijn, volg mij.")
        print("PAS OP!! Daar komt een truck aan met gewapende demonstranten, verstop je SNEL!")
        print("Grote rots of struik?")
        inputText = input()
        if inputText == "Grote rots":
            print("Je verstopt je achter de rots")
        elif inputText == "Struik":
            print("je verstopt je achter een struik")
    
    
    print("Do you want to repeat?")
    inputText = input()
    print("input:", inputText)
    if inputText == "no":
        break