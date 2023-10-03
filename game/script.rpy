define a = Character("Aarón")
define n = Character(what_italic = True)

define j = Character("Joana")
define r = Character("Raquel")
define c = Character("Carlos")
define e = Character("Eric")


transform toLeft:
    xalign 0.5 yalign 1.0
    linear 1 xalign 0.0
    
transform toRight:
    xalign 0.5 yalign 1.0
    linear 1 xalign 1.0

transform fadeOut:
    alpha 1.0
    linear 3 alpha 0.0
# El juego comienza aquí.

label start:

    scene bg room

    n "Suena la alarma y te despiertas."
    n "Sales de entre las sábanas y te diriges al baño."

    n "¿Qué ves?"

    show d_fem pose:
        toLeft
    show d_masc pose:
        toRight

    menu:
        "Chico":
            hide d_fem with dissolve
            python:
                gen = "d_masc"
            
        "Chica":
            hide d_masc with dissolve
            python:
                gen = "d_fem"

    n "Tienes lagunas después de haberte destruido a beber anoche y tienes que esforzarte por recordar tu nombre."

    python: 
        nombre = renpy.input("¿Cómo te llamabas?")
        nombre = nombre.strip() or "Noah"

    define d = Character( name = "[nombre]", image = "[gen]" )

    n "Terminas de lavarte la cara y procedes a desayunar, cuando de repente suena el teléfono."

    d "¿Sí? ¿Quién es?"

    a "Buenos días [nombre], ¿cómo vas?"

    d "Podría estar mejor, pero no puedo quejarme."

    a "Vas a estar mejor, te traigo buenas noticias: tengo un caso para ti."

    d "¿Qué? Pensaba que después del último iban a quitarme la placa..."

    a "Y así debería de haber sido, pero tengo buenos contactos."
    a "Ahora escucha:\nha muerto un chaval en una casa de campo a las afueras, posiblemente ahogado, pero la autopsia todavía está en proceso."
    a "Estamos completamente seguros de que el asesino es uno de las personas con las que residía ya que nadie se ha acercado a esa casa desde que ellos la alquilaron."
    a "Te he mandado por email toda la información disponible, ponte ya mismo a leer las fichas de los sospechosos y ve a la escena del crimen en cuanto estés listo."
    
    d "Muchas gracias, tío. Te debo una."

    a "Esto cuenta por bastante más que una, me estoy jugando el pellejo confiándote un caso después de que metieses la pata estrepitosamente con el anterior..."
    a "Pero bueno, hoy por ti, mañana por mí. Buena suerte."

    n "La llamada termina"
    n "Dejas el teléfono en la encimera, te preparas un café y te sientas delante del ordenador: efectivamente, ahí estaba el mensaje."
    n "Lo abres y encuentras cinco fichas, los cuatro sospechosos y la víctima, además de la ubicación de la escena del crimen."

    
    menu fichas:
        "Joana":
            n "lorem ipsum"
            jump fichas

        "Raquel":
            n "lorem ipsum"
            jump fichas

        "Eric":
            n "lorem ipsum"
            jump fichas

        "Carlos":
            n "lorem ipsum"
            jump fichas

        "Lucas":
            n "lorem ipsum"
            jump fichas

        "Viajar a la escena del crimen":
            n "lorem ipsum definitivo"
            jump escenaDelCrimen

    return

# ----------------- Escena del crimen ------------------

menu escenaDelCrimen:
    "Interrogar a Joana":
        jump JoanaInt

    "Interrogar a Raquel":
        jump RaquelInt

    "Interrogar a Eric":
        jump EricInt

    "Interrogar a Carlos":
        jump CarlosInt

    "Cerrar el caso":
        n "lorem ipsum definitivo"
        jump acusaciones

# ----------------- ------ --- ------ ------------------

# ----------------- Escena del crimen ------------------

menu acusaciones:
    "Acusar a Joana":
        n "lorem ipsum"
        jump JoanaEnd

    "Acusar a Raquel":
        n "lorem ipsum"
        jump RaquelEnd

    "Acusar a Eric":
        n "lorem ipsum"
        jump EricEnd

    "Acusar a Carlos":
        jump CarlosEnd

    "Volver":
        n "lorem ipsum definitivo"

# ----------------- ------ --- ------ ------------------

# ----------------- Inte. Carlos -----------------


define carlosBranch1 = True
define carlosBranch2 = True
define carlosBranch3 = True

label CarlosInt:
    d "Buenos días, Carlos."
    d "¿Podrías decirme qué ocurrió anoche?"

    c "Yo no sé nada, ha sido Raquel quién lo ha encontrado muerto en la piscina."

    d "¿Estuviste presente cuando Raquel lo encontró?"

    c "No, yo estaba en mi habitación. Estaba dormido. Me despertó su grito."

    d "Y entonces acudiste a la cocina."

    c "Así es."

    menu CarlosIntMenu:
    
        "¿Cómo era tu relación con Lucas? ¿Os llevábais bien?" if carlosBranch1 == True:
            c "Era un buen amigo. Se llevaba bien con todos."
            c "Una pena su pérdida."

            d "Entiendo que él y Joana eran pareja. ¿Qué me podrías decir sobre eso?"

            c "Joana ha tenido varios problemas a lo largo de su vida:"
            c "perdió a su madre cuando tenía quince años y, al ser la mayor tuvo que cuidar de sus hermanos pequeños"
            c "Su padre entró en depresión tras el fallecimiento y ya nada fue igual en su casa"
            c "Está un poquillo loca, la verdad. No se qué hacían esos dos juntos."
            c "Ahora, ¿su relación? Casi no se nada de ella. Lucas apenas se abría y no me creo nada de lo que dice Joana"
            c "Creo que miente más que otra cosa" 
            
            menu CarlosQ1:
                "Conoces demasiado bien la vida de Joana...":
                    c "Nos llevábamos bien. Llegamos a estar bastante unidos"

                    d "¿Y ahora ya no?"

                    c "Las cosas han cambiado desde la muerte de su madre."
                    c "Ya nunca fue la misma."

                    d "¿Llegaste a tener sentimientos hacia ella?"
                    
                    c "No veo cómo ese dato es relevante al caso"

                    d "Todo es relevante"

                    c "No. No llegué a sentir nada por ella."

                "Casi no has hablado de Lucas...": 
                    c "No hay mucho de qué hablar. Era buena gente, un santo diría yo."
                    c "No todo el mundo sería capaz de soportar a Joana."
                    c "En resumidas cuentas: se llevaba bien con todo el mundo."
                    c "Nadie le haría daño a no ser que se la tuviesen bien guardada."

                    d "¿Qué insinuas?"

                    c "Como he dicho antes, Joana nunca fue igual desde la pérdida de su madre."
                    c "Su mente no funciona muy bien."
                    c "A veces cuenta cosas que no han pasado y nos intenta convencer de que sí."
                    c "Lo dicho, un poco loca..."

                    d "¿Crees que ella podría haber hecho algo así?"

                    c "Eh, yo no he dicho nada de eso. Pero descubrirlo es parte de tu trabajo. "
                    
            python:
                carlosBranch1 = False
            jump CarlosIntMenu

        "Cuéntame con todo lujo de detalles lo que ocurrió anoche." if carlosBranch2 == True:
            c "Pues a ver..."
            c "Estábamos jugando juegos de mesa y pasando un buen rato, cuando de repente Lucas se mosqueó por una tontería. Al rato fue Joana a hablar con él."
            c "No sabemos de qué hablaron pero se les escuchó discutor."
            c "Después Joana se unió al grupo, cosa que no entiendo, mientras que Lucas se quedó solo un rato más antes de decirnos que se iba a dormir."
            c "No se tú, pero yo resolvería los problemas con mi pareja antes de volver al grupo y hacer como si nada..."

            d "Continúa"

            c "Pues tampoco hay mucho más."
            c "Seguimos todos de charreta y pasándolo bien hasta que decidimos irnos a dormir."
            c "Bueno, y como dije antes, Lucas se fue a dormir antes que nosotros."
            c "Nadie le presionó ni hizo comentarios al respecto. Ya hablaría cuando estuviese preparado. "

            menu CarlosQ2:
                "¿Y todos os fuisteis a dormir en ese momento?":
                    c "Sí"

                    d "¿Escuchaste algo raro esa noche?"

                    c "No, tengo un sueño muy profundo."

                "Continúa, por favor":
                    c "Nos despedimos, nos dimos las buenas noches y cada uno se fue a su cuarto."

                    d "¿No ocurrió nada más?"

                    c "Que me despertó el grito de Raquel."
                     
            python:
                carlosBranch2  = False
            jump CarlosIntMenu



        "¿Sabes si alguien se llevaba mal con Lucas?" if carlosBranch3 == True:
            c "¿Te refieres a que si sé quiénl o ha podido matar?"
            c "Pues no, no lo sé. Lucas se llevaba bien con todos."
            c "No creo que nadie quisiera hacerle daño"

            d "¿Crees que ha podido ser un accidente?"

            c "¿Accidente o sucuidio?"

            d "¿Tenía motivos para suicidarse?"

            c "Ni idea."

        "Muchas gracias. Con esto es suficiente.":
            jump escenaDelCrimen
    


# ----------------- ----- ------ -----------------

# ----------------- Inte. Eric -----------------

label EricInt:
menu EricIntMenu:
    d "Buenos días, Joana. "
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "Terminar":
        jump escenaDelCrimen

# ----------------- ----- ---- -----------------

# ----------------- Inte. Raquel -----------------

label RaquelInt:
menu RaquelIntMenu:
    d "Buenos días, Joana. "
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "Terminar":
        jump escenaDelCrimen

# ----------------- ----- ------ -----------------

# ----------------- Inte. Joana -----------------

label JoanaInt:
menu JoanaIntMenu:
    d "Buenos días, Joana. "
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "¿Dónde estabas tú la noche del asesinato?":
        j "Durmiendo"
    "Terminar":
        jump escenaDelCrimen

# ----------------- ----- ----- -----------------
