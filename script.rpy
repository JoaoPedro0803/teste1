define a = Character("Ana")
define j = Character("Joao")
init python:
    x = True


image Joao feliz = 'images/Joao feliz.jpg'
image Ana feliz = 'images/Ana feliz.jpg'
image fundo1 = 'images/background1.jpg'
image fundo2 = 'images/fundo2.jpeg'
image 3 = 'images/mamando.png'




label start:

    scene fundo1 at truecenter:
        zoom 5.0
    with dissolve
    show Ana feliz at left:
        zoom 2.0
    with dissolve
    a "Oi, tudo bem?"
    show Joao feliz at right:
            zoom 2.0
    with dissolve
    j "Olá, tudo ótimo"
    hide Joao feliz
    with fade
    a "Uai, porque vc foi embora?"
    show Joao feliz at right:
        zoom 2.0
    with pixellate
    j "Eu fui para outra dimensão e voltei hehehehehe!!!"
    a "Já que votou, vamos tomar um sorvete?"
    j "Vamos demais uai!"
    hide fundo1
    with zoomout
    with fade
    scene fundo2 at truecenter:
        zoom 2.0
    with zoomin
    with dissolve
    show Ana feliz at left:
        zoom 2.0
    with dissolve
    a "Eu amo esse lugar!"
    show Joao feliz at right:
        zoom 2.0
    with pixellate
    j "Caramba, eu nunca tinha visto aqui, mas, de fato, parece ser um lugar topíssimo!!"
    a "E eu amo mais ainda a música que eles colocam aqui para tocar!"
    play music "audio/axl_piano_solo.mp3"
    queue music "audio/axl_piano_solo.mp3"
    j "Ououuuuu ela é realmente muito boa, quem está tocando é aquele cantor que tem o nome de uma marca de desodorante?"
    a "KKKKKKKKKK o AXL, simm seu bobo, é ele mesmo. Ele toca no Guns N' Roses!"
    j "É verdade, tem um amigo meu que é muito fã dessa banda, o JOUNAO xD"
    show 3 at truecenter
    j "Caramba olha quem chegou!"
    j "Eai cara vc está bem?"
    menu:
        'Po mano to benzao':
            $x = True
        'Po to mei ruim mano':
            $x = False
    if x == True:
        j 'Krai bom dms mano'
    else:
        j 'Relaxa q vai melhorar'
        j 'Mas eai como q vai a Facul?'
        menu:
            'Ta top mano':
                $x = True
            'Ta chatona':
                $x = False
        if x == True:
            j 'krai boto fe dms, seu curso eh fera'
        else:
            j 'Relaxa q c ta no começo do curso ainda'
    a ' Mas eai jounao, tava em casa vendo os meus cadernos do EM e deu mo saudade, vc tb tem?'
    menu:
        'Euuuu n dou é Graças a Deus que acabou!':
            $x = False
        'Clarooo que sinto, época boa da porr, a gnt era feliz e n sabia!':
            $x = True
    if x == False:
        hide Ana feliz
        with fade
        j 'Ishhhh bro acho q ela apelou, ela é mt sentimental quanto à escola'
    else:
        a 'Caramba verdade demais isso!'




        return
